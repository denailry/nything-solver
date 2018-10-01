from utils import input_helper
import utils.evaluator as eva
import algorithms.hill_climbing as hc
import algorithms.simulated_annealing as sa
import algorithms.genetic as gen

ALGO_HILL_CLIMBING = 1
ALGO_SIMULATED_ANNEALING = 2
ALGO_GENETIC_ALGORITHM = 3

# Ask for configuration filename
# and initialize board according to configuration file
def initialize_board():
    while (input_helper.is_board_empty):
        print('file input: ', end="")
        file_name = input()
        input_helper.init_board(file_name)

# Ask for algorithm
def get_algorithm():
    print('Choose algorithm: ')
    print('1. Hill Climbing')
    print('2. Simulated Annealing')
    print('3. Genetic Algorithm')

    algorithm = -1
    while (algorithm not in range(1, 4)):
        print('Your choice: ', end='')
        algorithm = int(input())
        if algorithm not in range(1,4):
            print('What is that? I just know algorithm number 1, 2, and 3.')

    return algorithm

# Solve the problem according to selected algorithm
def solve(selected_algo):
    if selected_algo == ALGO_HILL_CLIMBING:
        hc.solve(input_helper.board)
    elif selected_algo == ALGO_SIMULATED_ANNEALING:
        try:
            max_step = int(input("Set maximum steps (input anything else for 15000) : "))
        except:
            max_step = 15000
        try:
            temperature = int(input("Set temperature (input anything else for 10) : "))
        except:
            temperature = 10
        input_helper.board = sa.solve(input_helper.board,max_step,temperature)
    elif selected_algo == ALGO_GENETIC_ALGORITHM:
        input_helper.board = gen.solve(input_helper.pieces, 2000)

# Displaying board and conflict number
def display_state():
    input_helper.display_board(input_helper.board)
    print(eva.boardNumConflicting(input_helper.board))

if __name__ == "__main__":
    initialize_board()
    print()
    display_state()
    print()
    selected_algo = get_algorithm()
    print()
    solve(selected_algo)
    print()
    display_state()
