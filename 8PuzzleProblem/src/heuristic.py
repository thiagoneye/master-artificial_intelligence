# Imports

from puzzle import Puzzle


# Implementations


def index_to_coordinates(index: int) -> tuple:
    """
    Convert a 1D index (0-8) to 2D coordinates (row, column).
    """
    row = index // 3
    col = index % 3
    return row, col


def manhattan_distance(index1: int, index2: int) -> int:
    """
    Calculate the Manhattan distance between two indices.
    """
    row1, col1 = index_to_coordinates(index1)
    row2, col2 = index_to_coordinates(index2)
    return abs(row1 - row2) + abs(col1 - col2)


def local_objective(puzzle: Puzzle, value: int) -> int:
    """
    Calculate the difference between the current state of a index and the goal state of that index.
    """
    puzzle_index = puzzle.index(value)

    goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]
    goal_index = goal_state.index(value)

    return manhattan_distance(puzzle_index, goal_index)


def total_objective(puzzle: Puzzle) -> int:
    """
    Calculate the total objective function for the puzzle.
    """
    total_difference = 0
    for value in range(1, 9):
        total_difference += local_objective(puzzle, value)

    return total_difference


def text_to_move(puzzle: Puzzle, text: str) -> Puzzle:
    """
    Convert text input to a puzzle move.
    """
    moves = {
        "right": puzzle.switch_to_right,
        "left": puzzle.switch_to_left,
        "up": puzzle.switch_to_up,
        "down": puzzle.switch_to_down,
    }

    if text in moves.keys():
        moves[text]()

    return puzzle


class MovementHistory:
    """
    Creation of a linked list to enable recovery of the path (movements) taken to solve the problem.
    """

    def __init__(self, puzzle: Puzzle, predecessor=None):
        self.puzzle = puzzle.copy()
        self.predecessor = predecessor

        if predecessor is None:
            self._number_of_movements = 0
        else:
            self._number_of_movements = predecessor._number_of_movements + 1

        self.cost = self._number_of_movements + total_objective(self.puzzle)

    def __repr__(self):
        return f"State: {self.puzzle}, Moves: {self._number_of_movements}, Cost: {self.cost}"

    def __lt__(self, other):
        return self.cost < other.cost

    def __gt__(self, other):
        return self.cost > other.cost

    def print_history(self):
        """
        Prints the status history.
        """
        history_list = []
        current = self
        while current:
            history_list.append(current.puzzle)
            current = current.predecessor

        print("History of States:")
        for i, puzzle in enumerate(reversed(history_list)):
            print(f"Step {i}: {puzzle}")


class AStar:
    """
    A* algorithm to solve the 8-puzzle problem.
    """

    def __init__(self, puzzle):
        self.current_state = MovementHistory(puzzle)
        self._open_list = []  # Movement History List
        self._closed_list = [puzzle]  # Puzzle List

    def run(self):
        distance_to_the_target = total_objective(self.current_state.puzzle)

        while distance_to_the_target > 0:
            self._get_next_states()
            distance_to_the_target = total_objective(self.current_state.puzzle)

    def _get_next_states(self):
        possible_moves = ["right", "left", "up", "down"]

        for move in possible_moves:
            new_puzzle = self.current_state.puzzle.copy()
            new_puzzle = text_to_move(new_puzzle, move)

            if new_puzzle != self.current_state.puzzle:
                if new_puzzle not in self._closed_list:
                    self._open_list.append(
                        MovementHistory(new_puzzle, self.current_state)
                    )

        self._open_list = sorted(self._open_list)
        self.current_state = self._open_list.pop(0)
        self._closed_list.append(self.current_state.puzzle)
