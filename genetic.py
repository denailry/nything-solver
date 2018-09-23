import random
import annealing

pieces = ['K','B','R','Q','k','b','r','q']
listOfPiece = []
population = []

class Piece:
    def __init__(self, jenis, posisiX, posisiY):
        self.jenis = jenis #Q,K,B,R,q,k,b,r
        self.posisiX = posisiX
        self.posisiY = posisiY

def convertMatrixToListOfPiece(matrix):
    listOfPiece = []
    for i in range(8):
        for j in range(8):
            listOfPiece.append(Piece(matrix[i][j],i,j))
    return listOfPiece

def convertListOfPieceToMatrix(listOfBidak):
    board = [[] for i in range(8)]
    for i in range(8):
        board[i] = ['' for i in range(8)]
    for (Piece) in listOfPiece:
        board[Piece.posisiX][Piece.posisiY] = Piece.jenis
    return board

def initPopulation(totalPopulation, pieces):
    population = []
    for i in range(totalPopulation):
        board = [[] for i in range(8)]
        for i in range(8):
            board[i] = ['' for i in range(8)]
        for elm in pieces:
            valid = False
            while not valid:
                pos = annealing.randomPos()
                print('bisa')
                if (board[pos[1]][pos[0]] == ''):
                    board[pos[1]][pos[0]] = elm
                    valid = True

    return population



initPopulation(5, ['K','B'])

