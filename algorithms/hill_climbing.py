import utils.evaluator as ev
import random

'''
For this module, the piece score will be 
[same_color_conflict, 64 - diff_color_conflict]

The second value is made as such to make sorting easier
Generally, the lesser the value of the scores, the better. 
So, best possible score in this module is [0,0]

The score will be normalize using normalize_scoring function
'''

EMPTY_TILE = ''

def normalize_scoring(score):
    score[1] = 64 - score[1]
    return score

# Find the scores of each individual piece, 
# Return sorted score, start from the worst (highest value of score)
def find_piece_scores(board):
    pieceScores = []
    for i in range(8):
        for j in range(8):
            if board[i][j] != EMPTY_TILE:
                score = normalize_scoring(ev.numConflicting(j, i, board))
                pieceScores.append({'pos':[i,j], 'scr':score})
    pieceScores.sort(key=lambda piece: piece['scr'], reverse=True)
    return pieceScores

# Return any possible moves which have the BEST SCORE
# by checking the score for the toBeMoved piece in every empty tile
# NOTE: this may include the current piece position in case there is no better score than current position
def find_best_move(board, toBeMoved_x, toBeMoved_y):
    toBeMoved = board[toBeMoved_x][toBeMoved_y]
    board[toBeMoved_x][toBeMoved_y] = EMPTY_TILE
    newScores = []
    bestScore = [128,128]
    bestNewPos = None
    scr_collection = []
    for i in range(8):
        for j in range(8):
            if board[i][j] == EMPTY_TILE:
                board[i][j] = toBeMoved
                score = normalize_scoring(ev.boardNumConflicting(board))
                newScores.append({'pos':[i,j], 'scr':score})
                scr_collection.append(score)
                if score < bestScore:
                    bestScore = score
                    bestNewPos = [i,j]
                board[i][j] = EMPTY_TILE
    board[toBeMoved_x][toBeMoved_y] = toBeMoved
    bestMoves = [x for x in newScores if x['scr'] == bestScore]
    return scr_collection, bestMoves

def move_piece(board, origin, dest):
    if origin != dest:
        board[dest[0]][dest[1]] = board[origin[0]][origin[1]]
        board[origin[0]][origin[1]] = EMPTY_TILE

# Receive: 
# - board: the initial state of board
# - wandering_steps: number of steps to wander in plateau until bored
def solve(board, wandering_steps = 20):
    boredom_threshold = wandering_steps
    steps = 0
    while True:
        steps += 1 
        print('\rClimbing the hill', '.'*(steps // 10 % 5 + 1), end='')
        hasmoved = False
        pieceBestMoves = []
        prevScore = normalize_scoring(ev.boardNumConflicting(board))
        pieceScores = find_piece_scores(board)
        for piece in pieceScores:
            scr_collection, bestMoves = find_best_move(board, piece['pos'][0], piece['pos'][1])
            pieceBestMoves.append([piece, bestMoves])
            move = random.choice(bestMoves)
            if prevScore > move['scr']: 
                # Do the move since smaller score is better
                move_piece(board, piece['pos'], move['pos'])
                hasmoved = True
                break

        if not hasmoved:
            boredom_threshold -= 1
            if boredom_threshold < 0:
                break
            else:
                # Find moves that doesn't change the score
                possiblePlateau = [x for x in pieceBestMoves if len(x[1]) > 1] 
                if possiblePlateau:
                    if boredom_threshold == wandering_steps-1:
                        print('\nEncountered a plateau, taking at most {} wandering steps'.format(wandering_steps))
                    piece, bestMoves = random.choice(possiblePlateau)
                    move = random.choice(bestMoves)
                    move_piece(board, piece['pos'], move['pos'])
                else:
                    break
        else:
            boredom_threshold = wandering_steps

    print('\nThis is the top of the hill')