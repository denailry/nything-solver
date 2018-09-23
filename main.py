import input_helper

print('file input: ', end="")
file_name = input()
print()

input_helper.init_board(file_name)
input_helper.display_board(input_helper.board)

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
