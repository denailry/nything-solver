import random
import input_helper
import evaluator

pieces = ['K','B','R','Q','k','b','r','q']
listOfPiece = []
population = []

class Piece:
    def __init__(self, jenis, posisiX, posisiY):
        self.jenis = jenis #Q,K,B,R,q,k,b,r
        self.posisiX = posisiX
        self.posisiY = posisiY

#is the numConflicting1 better than numConflicting2
def isBetter(numConflicting1, numConflicting2):
    #minimum ally-attacking is prioritized
    if(numConflicting1[0] < numConflicting2[0]):
        return True
    elif(numConflicting1[1] > numConflicting2[0]):
        return True
    return False

def convertMatrixToListOfPiece(matrix):
    listOfPiece = []
    for i in range(8):
        for j in range(8):
            listOfPiece.append(Piece(matrix[i][j],i,j))
    return listOfPiece

def convertListOfPieceToMatrix(listOfPiece):
    board = [[] for i in range(8)]
    for i in range(8):
        board[i] = ['' for i in range(8)]
    for (piece) in listOfPiece:
        board[piece.posisiX][piece.posisiY] = piece.jenis
    return board

#initialize the population with random pieces
def initPopulation(totalPopulation, pieces):
    population = []
    for j in range(totalPopulation):
        board = [[] for i in range(8)]
        for i in range(8):
            board[i] = ['' for i in range(8)]
        for elm in pieces:
            valid = False
            while not valid:
                pos = input_helper.randomPos()
                if (board[pos[1]][pos[0]] == ''):
                    board[pos[1]][pos[0]] = elm
                    valid = True
        population.append(convertMatrixToListOfPiece(board))
    return population

#get jenis of piece for sorting
def getJenis(piece):
    return piece.jenis

#get best configuration in population
def getBestFit(population):
    #initialize the best fit
    bestFitParent = population[0]
    bestFitConflicting = evaluator.boardNumConflicting(convertListOfPieceToMatrix(bestFitParent))
    
    #searching for the best fit configuration in population
    for pieceList in population:
        numConflicting = evaluator.boardNumConflicting(convertListOfPieceToMatrix(pieceList))
        if(isBetter(numConflicting,bestFitConflicting)):
            bestFitParent = pieceList
            bestFitConflicting = numConflicting
    return bestFitParent

def crossover(population):
    #find 2 best fit parent
    #population can't be less than 2

    #initialize the best and second best fit parent
    bestFitParent = population[0]
    bestFitConflicting = evaluator.boardNumConflicting(convertListOfPieceToMatrix(bestFitParent)) 
    secondBestFitParent = population[1]
    secondBestFitConflicting = evaluator.boardNumConflicting(convertListOfPieceToMatrix(secondBestFitParent))

    #find the best fit and second best fit parent
    for pieceList in population:
        numConflicting = evaluator.boardNumConflicting(convertListOfPieceToMatrix(pieceList))
        if(isBetter(numConflicting,bestFitConflicting)):
            bestFitParent = pieceList
            bestFitConflicting = numConflicting
        elif(isBetter(numConflicting, secondBestFitConflicting)):
            secondBestFitParent = pieceList
            secondBestFitConflicting = numConflicting

    #choose the crossover point
    crossoverBeginPoint = random.randint(0,len(listOfPiece))
    crossoverEndingPoint = random.randint(crossoverBeginPoint,len(listOfPiece))
    
    #make child that inherit both parents genes
    child = convertMatrixToListOfPiece(convertListOfPieceToMatrix(bestFitParent))
    child.sort(key=getJenis)
    secondBestFitParent.sort(key=getJenis)
    for i in range(crossoverBeginPoint, crossoverEndingPoint):
        child[i] = secondBestFitParent[i]
    population.append(child)

#remove the worst performing configuration in population
def removeWorstConfiguration(population):
    worstConfiguration = population[0]
    worstConfigurationConflicting = evaluator.boardNumConflicting(convertListOfPieceToMatrix(worstConfiguration))
    for listOfPiece in population:
        listOfPieceConflicting = evaluator.boardNumConflicting(convertListOfPieceToMatrix(listOfPiece))
        if(isBetter(worstConfigurationConflicting, listOfPieceConflicting)):
            worstConfiguration = listOfPiece
            worstConfigurationConflicting = listOfPieceConflicting
    population.remove(worstConfiguration)

#randomly change one piece place
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
            foundDestination = True

    #change the piece
    matrix[destinationPos[0]][destinationPos[1]] = matrix[piecePos[0]][piecePos[1]]
    matrix[piecePos[0]][piecePos[1]] = ''

    listOfPiece = convertMatrixToListOfPiece(matrix)



#Program Test
population = initPopulation(50, ['K','B','R','Q','k','b','r','q'])
for x in range(0,200):
    print(x)
    crossover(population)
    removeWorstConfiguration(population)
    if(random.randint(1,100) %7 == 0):
        mutation(population[random.randint(0,24)])
bestSolution = getBestFit(population)
input_helper.display_board(convertListOfPieceToMatrix(bestSolution))
bestSolutionConflicts = evaluator.boardNumConflicting(convertListOfPieceToMatrix(bestSolution))
print(bestSolutionConflicts[0],bestSolutionConflicts[1])


