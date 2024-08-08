import random


def get_state() -> tuple:
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of cols: "))
    state = [[False for _ in range(cols)] for _ in range(rows)]
    # state = place_random(state, int(0.1 * (rows * cols)))
    return rows, cols, state


def place_random(state, n):
    while n > 0:
        i = random.randint(0, len(state) - 1)
        j = random.randint(0, len(state[0]) - 1)
        if state[i][j] == 0:
            state[i][j] = True
            n -= 1

    return state
