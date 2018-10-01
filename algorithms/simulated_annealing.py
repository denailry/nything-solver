from utils.input_helper import display_board
from utils.evaluator import boardNumConflicting
from random import choice, uniform
from copy import deepcopy
import math

initial_temperature = 0 # Initial temperature
possible_moves = [] # Possible moves of each steps

# Get current temperature. Temperature cools down using logarithmic function
def get_temperature(step):
    global initial_temperature
    return initial_temperature / (1 + (0.85 * math.log(1 + step)))

def reset_possible_moves():
    global possible_moves
    possible_moves = []

def swap(state, initial, target):
    temp_piece = state[target[1]][target[0]]
    state[target[1]][target[0]] = state[initial[1]][initial[0]]
    state[initial[1]][initial[0]] = temp_piece

# From current state, return a random state (by moving one piece to an adjacent block)
def get_random_next_state(current_state):
    global possible_moves
    new_state = deepcopy(current_state)

    if not possible_moves:
        # Scan the board for pieces
        for j in range(8):
            for i in range(8):
                if (current_state[j][i] != ''):
                    # Checking boundaries
                    if (j - 1 >= 0):
                        possible_moves.append([(i,j),(i,j-1)])
                    if (j + 1 <= 7):
                        possible_moves.append([(i,j),(i,j+1)])
                    if (i - 1 >= 0):
                        possible_moves.append([(i,j),(i-1,j)])
                    if (i + 1 <= 7):
                        possible_moves.append([(i,j),(i+1,j)])

    move_picked = choice(possible_moves)
    swap(new_state, move_picked[0], move_picked[1])
    possible_moves.remove(move_picked)
    return new_state


# Checks whether to accept 'worsening' step or not
def is_accept(current_score, new_score, temperature):
    cur_threshold = uniform(0.0, 1.0)
    if (math.exp((0 - (new_score[0] - current_score[0])) / temperature) > cur_threshold):
        return math.exp((0 - (new_score[1] - current_score[1])) / temperature) > cur_threshold
    else:
        return False

def solve(init_state, limit_step = 10000, temperature = 3.5):
    global initial_temperature
    # Initialize initial values
    initial_temperature = temperature
    current_state = init_state
    current_score = boardNumConflicting(current_state)
    current_solution = [] # Current solution [board,num_of_inter-color_conflicts]
    is_a_solution_found = False

    for step in range(limit_step):
        temp = get_temperature(step)
        reset_possible_moves()
        print("\rCurrently on step #" + str(step + 1) + " with current temp. " + str(temp),end="")
        try:
            has_stepped = False
            while not has_stepped:
                new_state = get_random_next_state(current_state)
                new_score = boardNumConflicting(new_state)

                # If "solution" is reached
                if (new_score[0] == 0):
                    current_state = new_state
                    current_score = new_score
                    # Compare it with current_solution
                    if current_solution:
                        if (current_solution[1] < new_score[1]):
                            current_solution[0] = new_state
                            current_solution[1] = new_score[1]
                    else:
                        current_solution = [new_state,new_score[1]]
                    has_stepped = True
                    # Print notification if (first) solution is found
                    if not is_a_solution_found:
                        print()
                        print("A solution has been found! Press Ctrl+C to stop search and output current best solution...")
                        is_a_solution_found = True
                # If new state is better than current state
                elif ((new_score[0] <= current_score[0]) and (new_score[1] >= current_score[1])):
                    current_state = new_state
                    current_score = new_score
                    has_stepped = True
                # If new state is worse than current state
                elif is_accept(current_score, new_score, temp):
                    current_state = new_state
                    current_score = new_score
                    has_stepped = True
        except KeyboardInterrupt:
            print()
            print("Ctrl+C received, stopping search...")
    print()

    if current_solution:
        current_state = current_solution[0]
    return current_state
