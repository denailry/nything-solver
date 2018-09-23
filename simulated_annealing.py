def init_state():
    return None

def temperature(step):
    return None

def get_random_state():
    return None

def get_entropy(current_state, new_state):
    return None

def is_accept(entropy, temperature):
    return None

def simulated_annealing(init_state, limit_step):
    current_state = init_state

    for step in range(limit_step):
        temp = temperature(limit_step/step)

        if (temp > 0):
            new_state = get_random_state(current_state)
            entropy = get_entropy(current_state, new_state)

            if (entropy > 0):
                current_state = new_state
            elif is_accept(entropy, temp):
                current_state = new_state

    return current_state
    