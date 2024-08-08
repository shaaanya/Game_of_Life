import sys
import math
import pygame
import time

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (55, 55, 55)


def run_game(game):
    spacing = 1
    cell_size = min(1980 // game.cols, 720 // game.rows) - 2 * spacing
    border_size = 5
    screen_width = game.cols * (cell_size + spacing) + 2 * border_size
    screen_height = game.rows * (cell_size + spacing) + 2 * border_size
    screen_size = (screen_width, screen_height)

    pygame.init()
    screen = pygame.display.set_mode(screen_size)
    pygame.display.set_caption("Conway's Game of Life")

    clock = pygame.time.Clock()

    # Drawing phase
    drawing_start_time = time.time()
    drawing = True

    while drawing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEMOTION:
                mouse_x, mouse_y = event.pos
                col = (mouse_x - border_size) // (cell_size + spacing)
                row = (mouse_y - border_size) // (cell_size + spacing)
                if 0 <= row < game.rows and 0 <= col < game.cols:
                    game.toggle_cell(row, col)

        if time.time() - drawing_start_time >= 10:
            drawing = False

        display(screen, game.grid, cell_size, spacing, border_size)
        pygame.display.update()

    # Simulation phase
    start_time = time.time()
    running = True

    while time.time() - start_time <= game.game_length and running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        display(screen, game.grid, cell_size, spacing, border_size)
        game.step()
        pygame.display.update()
        clock.tick(game.frames)  # Control the frame rate

    pygame.quit()


def display(screen, grid, cell_size, spacing, border_size):
    adjusted_cell_size = cell_size - spacing
    screen.fill(BLACK)

    grid_width = len(grid[0]) * (cell_size + spacing)
    grid_height = len(grid) * (cell_size + spacing)
    pygame.draw.rect(screen, GRAY, pygame.Rect((screen.get_width() - grid_width) // 2 - border_size,
                                               (screen.get_height() - grid_height) // 2 - border_size,
                                               grid_width + 2 * border_size,
                                               grid_height + 2 * border_size), border_size)

    for row in range(len(grid)):
        for col in range(len(grid[row])):
            x = col * (cell_size + spacing) + (screen.get_width() - grid_width) // 2
            y = row * (cell_size + spacing) + (screen.get_height() - grid_height) // 2
            rect = pygame.Rect(x, y, adjusted_cell_size, adjusted_cell_size)
            color = WHITE if grid[row][col] else BLACK
            pygame.draw.rect(screen, color, rect)
    pygame.display.flip()
