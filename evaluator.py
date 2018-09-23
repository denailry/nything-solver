'''
# Given board, calculate how many board pieces are conflicting
def countConflicts(board):


'''

# Given the board and the evaluation position,
# calculate how many pieces the piece in the evalation position conflicts with
def numConflicting(board, eval_x, eval_y):
    num = 0
    type = '';
    if (board[eval_y][eval_x] == ''):
        type = board[eval_y][eval_x]
        num = -1
    if (type != ''):
        if (type == 'B') or (type == 'b'):
            # Bishop - Check it's diagonals
            # First diagonal
            i = eval_x + 1
            j = eval_y + 1
            found = False
            while ((i <= 7) and (j <= 7) and not found):
                if (board[j][i] != ''):
                    found = True
                else:
                    i += 1
                    j += 1
            if (found):
                num += 1

            # Second diagonal
            i = eval_x + 1
            j = eval_y - 1
            found = False
            while ((i <= 7) and (j >= 0) and not found):
                if (board[j][i] != ''):
                    found = True
                else:
                    i += 1
                    j -= 1
            if (found):
                num += 1

            # Third diagonal
            i = eval_x - 1
            j = eval_y - 1
            found = False
            while ((i >= 0) and (j >= 0) and not found):
                if (board[j][i] != ''):
                    found = True
                else:
                    i -= 1
                    j -= 1
            if (found):
                num += 1

            # Fourth diagonal
            i = eval_x - 1
            j = eval_y + 1
            found = False
            while ((i >= 0) and (j <= 7) and not found):
                if (board[j][i] != ''):
                    found = True
                else:
                    i -= 1
                    j -= 1
            if (found):
                num += 1

        elif (type == 'K') or (type == 'k'):
            # Knight

        elif (type == 'R') or (type == 'r'):
            # Rook - check it's row and column
            return ((first_x == second_x) or (first_y == second_y))
        else:
            # Queen - check it's row, column, and diagonals
            return ((first_x == second_x) or (first_y == second_y) or abs(first_x - first_y) == abs(second_x - second_y))
    return num
