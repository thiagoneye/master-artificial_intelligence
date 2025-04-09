# Implementation

def index_to_coordinates(index: int) -> tuple:
    """
    Convert a 1D index to 2D coordinates.
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
    Calculate the difference between the current state of a value and the goal state of that value.
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

def text_to_move(puzzle, text):
    """
    Convert text input to a puzzle move.
    """
    moves = {
        "right": puzzle.switch_to_right,
        "left": puzzle.switch_to_left,
        "up": puzzle.switch_to_up,
        "down": puzzle.switch_to_down
    }
    
    if text in moves:
        moves[text]()
    
    return puzzle

def greedy_algorithm(puzzle):
    """
    Greedy algorithm to solve the 8-puzzle problem.
    """
    pass
