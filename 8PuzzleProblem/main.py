# Imports

from puzzle import Puzzle
from heuristic import greedy_algorithm, prints_the_movement_history

# Execution

if __name__ == "__main__":
    puzzle = Puzzle()
    
    for value in range(1, 9):
        print(value)
    
    #moves, list_of_states = greedy_algorithm(puzzle)
    
    #print("\n\n\nO algoritmo finalizou!\n")
    
    #prints_the_movement_history(moves, list_of_states)
