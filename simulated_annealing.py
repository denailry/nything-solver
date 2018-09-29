from input_helper import display_board
from evaluator import boardNumConflicting
from random import choice, uniform
from copy import deepcopy
import math

init_temperature = 0 # Initial temperature
step_limit = 0 # The limit of allowed steps
poss_moves = [] # Possible moves of each steps

# Get current temperature. Temperature cools down using logarithmic function
def get_temperature(step):
    global init_temperature
    return init_temperature / (1 + (0.85 * math.log(1 + step)))

def resetPossMoves():
    global poss_moves
    poss_moves = []

# From current state, return a random state (by moving one piece to an adjacent block)
def get_random_next_state(current_state):
    global poss_moves
    new_state = deepcopy(current_state)

    if not poss_moves:
        # Scan the board for pieces
        for j in range(8):
            for i in range(8):
                if (current_state[j][i] != ''):
                    # Checking boundaries
                    if (j - 1 >= 0):
                        poss_moves.append([(i,j),(i,j-1)])
                    if (j + 1 <= 7):
                        poss_moves.append([(i,j),(i,j+1)])
                    if (i - 1 >= 0):
                        poss_moves.append([(i,j),(i-1,j)])
                    if (i + 1 <= 7):
                        poss_moves.append([(i,j),(i+1,j)])

    move_picked = choice(poss_moves)
    temp_piece = new_state[move_picked[1][1]][move_picked[1][0]]
    new_state[move_picked[1][1]][move_picked[1][0]] = current_state[move_picked[0][1]][move_picked[0][0]]
    new_state[move_picked[0][1]][move_picked[0][0]] = temp_piece
    poss_moves.remove(move_picked)
    return new_state

# Checks whether to accept 'worsening' step or not
def is_accept(current_score, new_score, temperature):
    cur_threshold = uniform(0.0, 1.0)
    if (math.exp((0 - (new_score[0] - current_score[0])) / temperature) > cur_threshold):
        return math.exp((0 - (new_score[1] - current_score[1])) / temperature) > cur_threshold
    else:
        return False

def simulated_annealing(init_state, limit_step = 10000, temperature = 3.2):
    global step_limit, init_temperature
    # Initialize initial values
    step_limit = limit_step
    init_temperature = temperature
    current_state = init_state
    current_score = boardNumConflicting(current_state)
    current_solution = [] # Current solution [board,num_of_inter-color_conflicts]

    for step in range(limit_step):
        temp = get_temperature(step)
        resetPossMoves()
        print("\rCurrently on step #" + str(step + 1) + " with current temp. " + str(temp),end="")

        hasStepped = False

        while not hasStepped:

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
                hasStepped = True
            # If new state is better than current state
            elif ((new_score[0] <= current_score[0]) and (new_score[1] >= current_score[1])):
                current_state = new_state
                current_score = new_score
                hasStepped = True
            # If new state is worse than current state
            elif is_accept(current_score, new_score, temp):
                current_state = new_state
                current_score = new_score
                hasStepped = True

    print()

    if current_solution:
        current_state = current_solution[0]
    return current_state
