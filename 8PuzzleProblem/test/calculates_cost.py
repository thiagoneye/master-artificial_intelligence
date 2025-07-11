# Imports

from ..src.puzzle import Puzzle
from ..src.heuristic import total_objective

# Implementations


def print_puzzle(puzzle):
    for row in puzzle._state_space:
        print(row)


# Execution

if __name__ == "__main__":
    state_space = [[5, 4, 6], [0, 7, 3], [2, 1, 8]]
    number_of_movements = 1

    puzzle = Puzzle()
    puzzle._state_space = state_space

    h = total_objective(puzzle)
    g = number_of_movements
    f = h + g

    print_puzzle(puzzle)
    print(f"The total cost is {f}!")
