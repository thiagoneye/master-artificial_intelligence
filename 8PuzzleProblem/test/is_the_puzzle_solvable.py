# Imports

from ..src.puzzle import is_solvable


# Executation

if __name__ == "__main__":
    state_space = [[2, 1, 0], [3, 4, 5], [6, 7, 8]]

    print(f"Is the Puzzle solvable? {is_solvable(state_space)}!")
