from evaluator import boardNumConflicting
from random import choice, uniform
from copy import copy
import math

init_temperature = 0 # Initial temperature
step_limit = 0 # The limit of allowed steps

# Get current temperature. Temperature cools down using logarithmic function
def get_temperature(step):
    global init_temperature
    return init_temperature / (1 + (0.85 * math.log(1 + step)))

# From current state, return a random state (by moving one or more pieces to an adjacent block)
def get_random_next_state(current_state):
    new_state = copy(current_state)
    rand_threshold = 0.8
    # Scan the board for pieces
    for j in range(8):
        for i in range(8):
            if (current_state[j][i] != ''):
                if (uniform(0.0,1.0) > rand_threshold):
                    poss_moves = []
                    # Evaluating if this piece can move somewhere
                    # Also, conditions like these are valid 'cause Python use lazy evaluations
                    if ((j - 1 >= 0) and new_state[j-1][i] == ''):
                        poss_moves.append((i,j-1))
                    if ((j + 1 <= 7) and new_state[j+1][i] == ''):
                        poss_moves.append((i,j+1))
                    if ((i - 1 >= 0) and new_state[j][i-1] == ''):
                        poss_moves.append((i-1,j))
                    if ((i + 1 <= 7) and new_state[j][i+1] == ''):
                        poss_moves.append((i+1,j))
                    if poss_moves:
                        next_loc = choice(poss_moves)
                        new_state[next_loc[1]][next_loc[0]] = new_state[j][i]
                        new_state[j][i] = ''
    return new_state

# Checks whether to accept 'worsening' step or not
def is_accept(current_score, new_score, temperature):
    cur_threshold = uniform(0.0, 1.0)
    if (math.exp((0 - (new_score[0] - current_score[0])) / temperature) > cur_threshold):
        return math.exp((0 - (new_score[1] - current_score[1])) / temperature) > cur_threshold
    else:
        return False

def simulated_annealing(init_state, limit_step = 10000, temperature = 3):
    global step_limit, init_temperature
    # Initialize initial values
    step_limit = limit_step
    init_temperature = temperature
    current_state = init_state
    current_score = boardNumConflicting(current_state)

    for step in range(limit_step):
        temp = get_temperature(step)
        print("\rCurrently on step #" + str(step + 1) + " with current temp. " + str(temp),end="")

        new_state = get_random_next_state(current_state)
        new_score = boardNumConflicting(new_state)

        # If "solution" is reached
        if (new_score[0] == 0):
            current_state = new_state
            current_score = new_score
            break
        # If new state is better than current state
        elif ((new_score[0] <= current_score[0]) and (new_score[1] >= current_score[1])):
            current_state = new_state
            current_score = new_score
        # If new state is worse than current state
        elif is_accept(current_score, new_score, temp):
            current_state = new_state
            current_score = new_score

    print()
    return current_state
