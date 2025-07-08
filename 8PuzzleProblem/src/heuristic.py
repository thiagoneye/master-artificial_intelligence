# Imports

from puzzle import Puzzle


# Implementation


def index_to_coordinates(index: int) -> tuple:
    """
    Convert a 1D index (0-8) to 2D coordinates (row, column).
    """
    row = index // 3
    col = index % 3
    return row, col


def manhattan_distance(index1, index2) -> int:
    """
    Calculate the Manhattan distance between two indices.
    """
    row1, col1 = index_to_coordinates(index1)
    row2, col2 = index_to_coordinates(index2)
    return abs(row1 - row2) + abs(col1 - col2)


def local_objective(puzzle, value) -> int:
    """
    Calculate the difference between the current state of a index and the goal state of that index.
    """
    puzzle_index = puzzle.index(value)

    goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]
    goal_index = goal_state.index(value)

    return manhattan_distance(puzzle_index, goal_index)


def total_objective(puzzle) -> int:
    """
    Calculate the total objective function for the puzzle.
    """
    total_difference = 0
    for value in range(1, 9):
        total_difference += local_objective(puzzle, value)

    return total_difference


def text_to_move(puzzle, text) -> Puzzle:
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


class AStar:
    """
    A* algorithm to solve the 8-puzzle problem.
    """

    def __init__(self, puzzle):
        self.initial_state = puzzle
        self.current_state = puzzle
        self.movement_history = []
        self._closed_list = []

    def run(self):
        distance_to_the_target = total_objective(self.initial_state)

        while distance_to_the_target > 0:
            print("\n")
            print(f"Estado atual: {self.current_state}")
            print(f"Custo: {distance_to_the_target}")
            print(f"Histórico de movimentos: {self.movement_history}")
            self._get_next_states()
            distance_to_the_target = total_objective(self.current_state)

    def _get_next_states(self):
        open_dict = dict()
        self._open_list = list()

        possible_moves = ["right", "left", "up", "down"]
        for move in possible_moves:
            new_puzzle = self.current_state.copy()
            puzzle_moved = text_to_move(new_puzzle, move)

            if puzzle_moved._state_space != self.current_state._state_space:
                if puzzle_moved not in self._closed_list:
                    open_dict[move] = puzzle_moved

        self._get_minimum_cost_state(open_dict)

    def _get_minimum_cost_state(self, open_dict):
        for move, puzzle in open_dict.items():
            cost = total_objective(puzzle)
            self._open_list.append([cost, move, puzzle])

        self._open_list = sorted(self._open_list, key=lambda x: x[0])
        cost, move, puzzle = self._open_list[0]
        self.current_state = puzzle
        self._closed_list.append(puzzle)
        self.movement_history.append(move)
