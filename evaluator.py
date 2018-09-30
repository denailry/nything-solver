board = None;

# Given :
#   num, that is [x,y] , where :
#       x is the number of conflicting pieces with the same color
#       y is the number of conflicting pieces with different color
#   eval_type and target_type : type of new pieces that conflicted,
# increment the correct element of num based of eval_type & target_type color (which is represented by them being written lowercase/uppercase)
def incrementNum(num, eval_type, target_type):
    if eval_type.islower():
        if target_type.islower():
            num[0] += 1
        else:
            num[1] += 1
    else:
        if target_type.islower():
            num[1] += 1
        else:
            num[0] += 1

def evaluate_bishop(num, eval_x, eval_y, eval_type):
    # First diagonal
    i = eval_x + 1
    j = eval_y + 1
    found = False
    while ((i <= 7) and (j <= 7) and not found):
        if (board[j][i] != ''):
            found = True
            incrementNum(num,eval_type,board[j][i])
        else:
            i += 1
            j += 1

    # Second diagonal
    i = eval_x + 1
    j = eval_y - 1
    found = False
    while ((i <= 7) and (j >= 0) and not found):
        if (board[j][i] != ''):
            found = True
            incrementNum(num,eval_type,board[j][i])
        else:
            i += 1
            j -= 1

    # Third diagonal
    i = eval_x - 1
    j = eval_y - 1
    found = False
    while ((i >= 0) and (j >= 0) and not found):
        if (board[j][i] != ''):
            found = True
            incrementNum(num,eval_type,board[j][i])
        else:
            i -= 1
            j -= 1

    # Fourth diagonal
    i = eval_x - 1
    j = eval_y + 1
    found = False
    while ((i >= 0) and (j <= 7) and not found):
        if (board[j][i] != ''):
            found = True
            incrementNum(num,eval_type,board[j][i])
        else:
            i -= 1
            j -= 1

def evaluate_knight(num, eval_x, eval_y, eval_type):
    i = eval_x + 2
    j = eval_y + 1
    if ((i <= 7) and (j <= 7)):
        if (board[j][i] != ''):
            incrementNum(num,eval_type,board[j][i])

    i = eval_x + 2
    j = eval_y - 1
    if ((i <= 7) and (j >= 0)):
        if (board[j][i] != ''):
            incrementNum(num,eval_type,board[j][i])

    i = eval_x + 1
    j = eval_y - 2
    if ((i <= 7) and (j >= 0)):
        if (board[j][i] != ''):
            incrementNum(num,eval_type,board[j][i])

    i = eval_x - 1
    j = eval_y - 2
    if ((i >= 0) and (j >= 0)):
        if (board[j][i] != ''):
            incrementNum(num,eval_type,board[j][i])

    i = eval_x - 2
    j = eval_y - 1
    if ((i >= 0) and (j >= 0)):
        if (board[j][i] != ''):
            incrementNum(num,eval_type,board[j][i])

    i = eval_x - 2
    j = eval_y + 1
    if ((i >= 0) and (j <= 7)):
        if (board[j][i] != ''):
            incrementNum(num,eval_type,board[j][i])

    i = eval_x - 1
    j = eval_y + 2
    if ((i >= 0) and (j <= 7)):
        if (board[j][i] != ''):
            incrementNum(num,eval_type,board[j][i])

    i = eval_x + 1
    j = eval_y + 2
    if ((i <= 7) and (j <= 7)):
        if (board[j][i] != ''):
            incrementNum(num,eval_type,board[j][i])

def evaluate_rock(num, eval_x, eval_y, eval_type):
    # Check the left
    i = eval_x - 1
    found = False
    while((i >= 0) and not found):
        if (board[eval_y][i] != ''):
            found = True
            incrementNum(num,eval_type,board[eval_y][i])
        else:
            i -= 1

    # Check the right
    i = eval_x + 1
    found = False
    while((i <= 7) and not found):
        if (board[eval_y][i] != ''):
            found = True
            incrementNum(num,eval_type,board[eval_y][i])
        else:
            i += 1

    # Check up
    i = eval_y - 1
    found = False
    while((i >= 0) and not found):
        if (board[i][eval_x] != ''):
            found = True
            incrementNum(num,eval_type,board[i][eval_x])
        else:
            i -= 1

    # Check down
    i = eval_y + 1
    found = False
    while((i <= 7) and not found):
        if (board[i][eval_x] != ''):
            found = True
            incrementNum(num,eval_type,board[i][eval_x])
        else:
            i += 1
    
def evaluate_queen(num, eval_x, eval_y, eval_type):
    # First diagonal
    i = eval_x + 1
    j = eval_y + 1
    found = False
    while ((i <= 7) and (j <= 7) and not found):
        if (board[j][i] != ''):
            found = True
            incrementNum(num,eval_type,board[j][i])
        else:
            i += 1
            j += 1

    # Second diagonal
    i = eval_x + 1
    j = eval_y - 1
    found = False
    while ((i <= 7) and (j >= 0) and not found):
        if (board[j][i] != ''):
            found = True
            incrementNum(num,eval_type,board[j][i])
        else:
            i += 1
            j -= 1

    # Third diagonal
    i = eval_x - 1
    j = eval_y - 1
    found = False
    while ((i >= 0) and (j >= 0) and not found):
        if (board[j][i] != ''):
            found = True
            incrementNum(num,eval_type,board[j][i])
        else:
            i -= 1
            j -= 1

    # Fourth diagonal
    i = eval_x - 1
    j = eval_y + 1
    found = False
    while ((i >= 0) and (j <= 7) and not found):
        if (board[j][i] != ''):
            found = True
            incrementNum(num,eval_type,board[j][i])
        else:
            i -= 1
            j += 1

    # Check the left
    i = eval_x - 1
    found = False
    while((i >= 0) and not found):
        if (board[eval_y][i] != ''):
            found = True
            incrementNum(num,eval_type,board[eval_y][i])
        else:
            i -= 1

    # Check the right
    i = eval_x + 1
    found = False
    while((i <= 7) and not found):
        if (board[eval_y][i] != ''):
            found = True
            incrementNum(num,eval_type,board[eval_y][i])
        else:
            i += 1

    # Check up
    i = eval_y - 1
    found = False
    while((i >= 0) and not found):
        if (board[i][eval_x] != ''):
            found = True
            incrementNum(num,eval_type,board[i][eval_x])
        else:
            i -= 1

    # Check down
    i = eval_y + 1
    found = False
    while((i <= 7) and not found):
        if (board[i][eval_x] != ''):
            found = True
            incrementNum(num,eval_type,board[i][eval_x])
        else:
            i += 1

# Given the board and the evaluation position,
# calculate how many pieces this piece conflicts with.
# This function returns [x,y] , where :
#   x is the number of conflicting pieces with the same color
#   y is the number of conflicting pieces with different color
# If this function returns [-1,-1], there is no piece in given position
def numConflicting(eval_x, eval_y, input_board=None):
    global board;

    if (input_board != None):
        board = input_board;

    # If no piece in (eval_x, eval_y)
    if (board[eval_y][eval_x] == ''):
        return [-1,-1]

    num = [0,0];
    eval_type = board[eval_y][eval_x];

    # Bishop - Check it's diagonals
    if (eval_type == 'B') or (eval_type == 'b'):
        evaluate_bishop(num, eval_x, eval_y, eval_type);
    # Knight - Check all 8 possible moves from a Knight
    elif (eval_type == 'K') or (eval_type == 'k'):
        evaluate_knight(num, eval_x, eval_y, eval_type);
    # Rook - check it's row and column
    elif (eval_type == 'R') or (eval_type == 'r'):
        evaluate_rock(num, eval_x, eval_y, eval_type);
    # Queen - check it's row, column, and diagonals
    else:
        evaluate_queen(num, eval_x, eval_y, eval_type);

    return num

def boardNumConflicting(input_board):
    global board;
    board = input_board;

    num = [0,0]
    for j in range(8):
        for i in range(8):
            if (board[j][i] != ''):
                tempNum = numConflicting(i,j)
                num[0] += tempNum[0]
                num[1] += tempNum[1]
    return num
