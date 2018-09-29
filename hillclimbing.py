import evaluator as ev
import random

empty_tile = ''

# for this module, the piece score will be [number_of_same_color_conflict, 64 - number_of_diff_color_conflict]
# the second value is made as such to make sorting easier
# generally, the lesser the value of the scores, the better (best possible score is [0,0])

def normalizeScoring(score):
    score[1] = 64 - score[1]
    return score

def findPieceScores(board): # the board is a matrix
    # find the scores of each individual piece, sorted from the worst scoring
    pieceScores = []
    for i in range(8):
        for j in range(8):
            if board[i][j] != empty_tile:
                score = normalizeScoring(ev.numConflicting(board, j, i))
                pieceScores.append({'pos':[i,j], 'scr':score})
    pieceScores.sort(key=lambda piece: piece['scr'], reverse=True) # worst scoring piece first
    return pieceScores

def findBestMove(board, toBeMoved_x, toBeMoved_y):
    # check the score for the toBeMoved piece in every empty tile and return the best scoring tiles 
    # note that this may include the current piece position if there is no better scoring tile
    
    toBeMoved = board[toBeMoved_x][toBeMoved_y]
    board[toBeMoved_x][toBeMoved_y] = empty_tile
    newScores = []
    bestScore = [64,64]
    bestNewPos = None
    for i in range(8):
        for j in range(8):
            if board[i][j] == empty_tile:
                board[i][j] = toBeMoved
                score = normalizeScoring(ev.boardNumConflicting(board))
                newScores.append({'pos':[i,j], 'scr':score})
                if score < bestScore:
                    bestScore = score
                    bestNewPos = [i,j]
                board[i][j] = empty_tile
    board[toBeMoved_x][toBeMoved_y] = toBeMoved
    
    #return every position with the same score as best score
    bestMoves = [x for x in newScores if x['scr'] == bestScore]
    
    return bestMoves

def movePiece(board, origin, dest):
    #print('move ', board[origin[0]][origin[1]], 'from', origin, 'to', dest)
    if origin != dest:
        board[dest[0]][dest[1]] = board[origin[0]][origin[1]]
        board[origin[0]][origin[1]] = empty_tile
        

def hillclimb(board, wandering_steps = 20):
    # hillclimbing algorithm with wandering steps to avoid getting stuck on a plateau
    boredom_threshold = wandering_steps
    while True:
        hasmoved = False
        pieceBestMoves = []
        prevScore = normalizeScoring(ev.boardNumConflicting(board))
        pieceScores = findPieceScores(board)
        for piece in pieceScores:
            bestMoves = findBestMove(board, piece['pos'][0], piece['pos'][1])
            pieceBestMoves.append([piece, bestMoves])
            move = random.choice(bestMoves)
            if prevScore > move['scr']: 
                #do the move since smaller score is better
                movePiece(board, piece['pos'], move['pos'])
                hasmoved = True
                break

        if not hasmoved:
            boredom_threshold -= 1
            #print(boredom_threshold)
            if boredom_threshold < 0:
                break
            else:
                # find moves that doesn't change the score
                possiblePlateau = [x for x in pieceBestMoves if len(x[1]) > 1] 
                if possiblePlateau:
                    piece, bestMoves = random.choice(possiblePlateau)
                    move = random.choice(bestMoves)
                    movePiece(board, piece['pos'], move['pos'])
                else:
                    break
        else:
            boredom_threshold = wandering_steps