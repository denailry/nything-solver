from random import randint

# available pieces to place on board
pieces = ['K','B','R','Q','k','b','r','q']

# randomPos : return tuple (x,y) , where x and y is random
def randomPos():
    return (randint(0,7),randint(0,7))

'''
# Given board, calculate how many board pieces are conflicting
def countConflicts(board):


'''


# Given the pieces type & location, return true if the first piece is attacking the second piece
# This function assumes that the two pieces are the same color
def isConflicting(first_type, first_loc_x, first_loc_y, second_x, second_y):
    if (first_type == 'B') or (first_type == 'b'):

        # bishop
    elif (first_type == 'K') or (first_type == 'k'):
        # knight
    elif (first_type == 'R') or (first_type == 'r'):
        # Rook
    else:
        # Queen

# current board state
board = [[] for i in range(8)]
for i in range(8):
    board[i] = ['' for i in range(8)]

# Initialize board - place/fill board randomly
for elm in pieces:
    valid = False
    while not valid:
        pos = randomPos()
        if (board[pos[1]][pos[0]] == ''):
            board[pos[1]][pos[0]] = elm
            valid = True

for row in board:
    for col in row:
        if (col == ''):
            print('.',end='')
        else:
            print(col,end='')
    print()
