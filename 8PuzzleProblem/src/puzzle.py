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
            self._state_space[int(idx/3)][idx%3] = value

    def index(self, value: int) -> int:
        for idx in range(9):
            if self._state_space[int(idx/3)][idx%3] == value:
                return idx
        return None

    def switch_to_right(self):
        blank_index = self.index(0)
        if blank_index % 3 != 2:
            self[blank_index], self[blank_index + 1] = self[blank_index + 1], self[blank_index]

    def switch_to_left(self):
        blank_index = self.index(0)
        if blank_index % 3 != 0:
            self[blank_index], self[blank_index - 1] = self[blank_index - 1], self[blank_index]

    def switch_to_up(self):
        blank_index = self.index(0)
        if blank_index // 3 != 0:
            self[blank_index], self[blank_index - 3] = self[blank_index - 3], self[blank_index]

    def switch_to_down(self):
        blank_index = self.index(0)
        if blank_index // 3 < 2:
            self[blank_index], self[blank_index + 3] = self[blank_index + 3], self[blank_index]

    def copy(self):
        return copy.copy(self)

    def __getitem__(self, index):
        return self._state_space[int(index/3)][index%3]
    
    def __repr__(self):
        return repr(self._state_space)
