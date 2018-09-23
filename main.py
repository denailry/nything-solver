import input_helper

print('file input: ', end="")
file_name = input()

input_helper.init_board(file_name)
input_helper.display_board()