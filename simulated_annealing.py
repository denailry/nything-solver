from input_helper import random_board

def init_state():
    return None

def temperature(step):
    return step

def get_random_state(current_state):
    random_board(current_state)

def fitness_function(state):
    return 0

def get_entropy(current_state, new_state):
    return fitness_function(current_state) - fitness_function(new_state)

def is_accept(entropy, temperature):
    return None

def simulated_annealing(init_state, limit_step):
    current_state = init_state

    for step in range(limit_step):
        temp = temperature(limit_step/step)

        if (temp > 0):
            new_state = [['' for i in range(8)] for j in range('8')]
            get_random_state(new_state)

            entropy = get_entropy(current_state, new_state)

            if (entropy > 0):
                current_state = new_state
            elif is_accept(entropy, temp):
                current_state = new_state

    return current_state
    