from game_of_life import GameOfLife
import utils
import display


def main():
    rows, cols, state = utils.get_state()
    game = GameOfLife(rows=rows, cols=cols, initial_state=state)
    display.run_game(game)


if __name__ == '__main__':
    main()