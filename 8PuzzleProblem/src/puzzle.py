# Imports

from random import shuffle
import copy

# Implementation


class Puzzle:
    def __init__(self):
        self._state_space = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

        default_values = list(range(9))
        shuffle(default_values)

        for idx, value in enumerate(default_values):
            self._state_space[int(idx / 3)][idx % 3] = value

    def index(self, value: int) -> int:
        for idx in range(9):
            if self._state_space[int(idx / 3)][idx % 3] == value:
                return idx
        return None

    def switch_to_right(self):
        blank_index = self.index(0)
        if blank_index % 3 != 0:
            self[blank_index], self[blank_index - 1] = (
                self[blank_index - 1],
                self[blank_index],
            )

    def switch_to_left(self):
        blank_index = self.index(0)
        if blank_index % 3 != 2:
            self[blank_index], self[blank_index + 1] = (
                self[blank_index + 1],
                self[blank_index],
            )

    def switch_to_up(self):
        blank_index = self.index(0)
        if blank_index // 3 < 2:
            self[blank_index], self[blank_index + 3] = (
                self[blank_index + 3],
                self[blank_index],
            )

    def switch_to_down(self):
        blank_index = self.index(0)
        if blank_index // 3 != 0:
            self[blank_index], self[blank_index - 3] = (
                self[blank_index - 3],
                self[blank_index],
            )

    def copy(self):
        new_puzzle = Puzzle()
        new_puzzle._state_space = copy.deepcopy(self._state_space)
        return new_puzzle

    def __getitem__(self, index):
        return self._state_space[int(index / 3)][index % 3]

    def __setitem__(self, index: int, value: int):
        row = int(index / 3)
        col = index % 3
        self._state_space[row][col] = value

    def __repr__(self):
        return repr(self._state_space)

    def __eq__(self, other):
        return isinstance(other, Puzzle) and self._state_space == other._state_space
