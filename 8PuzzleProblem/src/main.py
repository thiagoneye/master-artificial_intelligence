# Imports

from puzzle import Puzzle
from heuristic import AStar, text_to_move

# Execution

if __name__ == "__main__":
    puzzle = Puzzle()
    astar = AStar(puzzle)
    astar.run()
