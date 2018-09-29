import input_helper
import evaluator as eva
import hillclimbing as hc
import simulated_annealing as sa
import genetic as gen

print('file input: ', end="")
file_name = input()
print()

input_helper.init_board(file_name)
if not input_helper.is_board_empty:
    input_helper.display_board(input_helper.board)
    print(eva.boardNumConflicting(input_helper.board))

    print()
    print('choose algorithm: ')
    print('1. Hill Climbing')
    print('2. Simulated Annealing')
    print('3. Genetic Algorithm')
    print('Your choice: ', end='')

    selected_algo = int(input())

    if selected_algo in range(1,4):
        print('Loading...')
    else:
        print('Algorithm not found')

    if selected_algo == 1:
        hc.hillclimb(input_helper.board)
    elif selected_algo == 2:
        # input_helper.board = sa.get_random_next_state(input_helper.board)
        input_helper.board = sa.simulated_annealing(input_helper.board,15000,3.5)
    elif selected_algo == 3:
        input_helper.board = gen.geneticAlgorithm(input_helper.pieces)

    input_helper.display_board(input_helper.board)
    print(eva.boardNumConflicting(input_helper.board))
