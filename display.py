import sys
import math
import pygame
import time

SCREEN_SIZE = 1280, 720
# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


def run_game(game):
    cell_size = min(SCREEN_SIZE) // max(game.rows, game.cols)
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)
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
                col = mouse_x // cell_size
                row = mouse_y // cell_size
                if 0 <= row < game.rows and 0 <= col < game.cols:
                    game.toggle_cell(row, col)

        if time.time() - drawing_start_time >= 10:
            drawing = False

        display(screen, game.grid, cell_size)
        pygame.display.update()
        clock.tick(game.frames)  # Limit to 60 frames per second

    # Simulation phase
    start_time = time.time()
    running = True

    while time.time() - start_time <= game.game_length and running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        display(screen, game.grid, cell_size)
        game.step()
        pygame.display.update()
        clock.tick(game.frames)  # Control the frame rate

    pygame.quit()


def display(screen, grid, cell_size):
    screen.fill(BLACK)
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            rect = pygame.Rect(col * cell_size, row * cell_size, cell_size, cell_size)
            color = WHITE if grid[row][col] else BLACK
            pygame.draw.rect(screen, color, rect)
    pygame.display.flip()
