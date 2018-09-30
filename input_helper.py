from random import randint

# available pieces to place on board
pieces = []

# current board state
board = [['' for i in range(8)] for j in range(8)]
is_board_empty = True

str_white = "WHITE"
str_black = "BLACK"

def read_file(file_name):
    data_file = open(file_name, 'r')

    for row in data_file:
        arr_row = row.split()
        if (arr_row[0] == str_white):
            for i in range(0, int(arr_row[2])):
                pieces.append(arr_row[1][0])
        else:
            for i in range(0, int(arr_row[2])):
                pieces.append(arr_row[1][0].lower())


# randomPos : return tuple (x,y) , where x and y is random
def randomPos():
    return (randint(0,7),randint(0,7))


# Initialize board - place/fill board randomly
def init_board(file_name):
    global is_board_empty
    try:
        read_file(file_name);
    except FileNotFoundError:
        print("Oopps... Cannot open the file.");
        return;
        
    if (len(pieces) > 64):
        print("Number of pieces exceed board capacity!")
    else:
        random_board(board)
        is_board_empty = False

def random_board(board):
    for elm in pieces:
        valid = False
        while not valid:
            pos = randomPos()
            if (board[pos[1]][pos[0]] == ''):
                board[pos[1]][pos[0]] = elm
                valid = True

# Printing board to screen
def display_board(board):
    for row in board:
        print('|',end='')
        for col in row:
            if (col == ''):
                print('.',end='')
            else:
                print(col,end='')
            print('|',end='')
        print()
