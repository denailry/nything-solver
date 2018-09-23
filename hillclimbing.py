import evaluator as ev #nama placeholder buat modul bersama
import random

empty_tile = ''

def findPieceScores(board): # the board is a matrix
    # find the scores of each individual piece, sorted from the worst scoring
    pieceScores = []
    for i in range(8):
        for j in range(8):
            if board[i][j] != empty_tile:
                score = ev.numConflicting(board, j, i)
                score[1] = 64 - score[1]
                pieceScores.append({'pos':[i,j], 'scr':score})
    pieceScores.sort(key=lambda piece: piece['scr'], reverse=True)
    return pieceScores

def findBestMove(board, toBeMoved_x, toBeMoved_y):
    toBeMoved = board[toBeMoved_x][toBeMoved_y]
    #print(board)
    board[toBeMoved_x][toBeMoved_y] = empty_tile
    newScores = []
    bestScore = [64,64]
    bestNewPos = None
    for i in range(8):
        for j in range(8):
            if board[i][j] == empty_tile:
                board[i][j] = toBeMoved
                score = ev.numConflicting(board, j, i)
                score[1] = 64 - score[1]
                newScores.append({'pos':[i,j], 'scr':score})
                if score < bestScore:
                    bestScore = score
                    bestNewPos = [i,j]
                board[i][j] = empty_tile
    board[toBeMoved_x][toBeMoved_y] = toBeMoved
    
    bestMoves = [x for x in newScores if x['scr'] == bestScore]
    return bestMoves

def movePiece(board, origin, dest):
    board[dest[0]][dest[1]] = board[origin[0]][origin[1]]
    board[origin[0]][origin[1]] = empty_tile

def hillclimb(board):
    boredom_threshold = 100
    while True:
        hasmoved = False
        prevScore = ev.boardNumConflicting(board)
        pieceScores = findPieceScores(board)
        for piece in pieceScores:
            bestMoves = findBestMove(board, piece['pos'][0], piece['pos'][1])
            move = random.choice(bestMoves)
            if piece['scr'] > move['scr']:
                movePiece(board, piece['pos'], move['pos'])
                hasmoved = True
                break

        if not hasmoved:
            break
        if ev.boardNumConflicting(board) == prevScore:
            boredom_threshold -= 1
            if boredom_threshold == 0:
                break
        else:
            boredom_threshold = 100