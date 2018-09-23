import input_helper

print('file input: ', end="")
file_name = input()
print()

<<<<<<< HEAD
input_helper.init_board(file_name)
input_helper.display_board()
=======
# input_helper.init_board(file_name)
# input_helper.display_board()
>>>>>>> 95053ef896eb9adefbaab7006af9f74b2a2f4f06

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