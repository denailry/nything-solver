from random import randint

# available pieces to place on board
pieces = ['K','B','R','Q','k','b','r','q']

# randomPos : return tuple (x,y) , where x and y is random
def randomPos():
    return (randint(0,7),randint(0,7))

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

# Printing board to screen
for row in board:
    for col in row:
        if (col == ''):
            print('.',end='')
        else:
            print(col,end='')
    print()
