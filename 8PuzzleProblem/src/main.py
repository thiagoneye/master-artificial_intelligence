# Imports

from puzzle import is_solvable, Puzzle
from heuristic import total_objective, AStar

# Execution

if __name__ == "__main__":
    puzzle = Puzzle()
    puzzle.generate()

    while not is_solvable(puzzle):
        puzzle.generate()

    print(puzzle)
    print(f"The distance to the goal is {total_objective(puzzle)}.")
    print("\nIniciando busca!")

    astar = AStar(puzzle)
    astar.run()
    print("\nThe execution is complete.\n")
    astar.current_state.print_history()
