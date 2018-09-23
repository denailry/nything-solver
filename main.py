import input_helper
import evaluator as eva
import hillclimbing as hc

print('file input: ', end="")
file_name = input()
print()

input_helper.init_board(file_name)
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
    input_helper.display_board(input_helper.board)


print(eva.boardNumConflicting(input_helper.board))