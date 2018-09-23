import random
import input_helper

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
                pos = input_helper.randomPos()
                print('bisa')
                if (board[pos[1]][pos[0]] == ''):
                    board[pos[1]][pos[0]] = elm
                    valid = True
    return population

def crossover(population):
    #find 2 best fit parent
    child = bestFitParent


def mutation(listOfPiece):
    matrix = convertListOfPieceToMatrix(listOfPiece)

    #find a piece to move its position
    foundPiece = False
    piecePos = (0,0)
    while(not(foundPiece)):
        piecePos = input_helper.randomPos()
        if(matrix[piecePos[0]][piecePos[1]])!='':
            foundPiece = True

    #find a piece as a destination
    foundDestination = False
    destinationPos = (0,0)
    while(not(foundDestination)):
        destinationPos = input_helper.randomPos()
        if(matrix[destinationPos[0]][destinationPos[1]])=='':
            foundDestination = False

    matrix[destinationPos[0]][destinationPos[1]] = matrix[piecePos[0]][piecePos[1]]
    matrix[piecePos[0]][piecePos[1]] = ''

    listOfPiece = convertMatrixToListOfPiece(matrix)




initPopulation(5, ['K','B'])

