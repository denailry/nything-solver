import random
import input_helper
import evaluator


listOfPiece = []
population = []

#a piece in the chess, contains it's category and position
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
    elif(numConflicting1[1] > numConflicting2[1]):
        return True
    return False

#convert matrix to list of piece
def convertMatrixToListOfPiece(matrix):
    listOfPiece = []
    for i in range(8):
        for j in range(8):
            if(matrix[i][j]!=''):
                listOfPiece.append(Piece(matrix[i][j],i,j))

    return listOfPiece

#convert list of piece to matrix
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

#add child to population that inherits it's parents genes
def crossover(population):

    #using russian roulette method
    weight = []
    #get probability for each configuration
    for configuration in population:
        conflictNumber = evaluator.boardNumConflicting(convertListOfPieceToMatrix(configuration))
        #prevent division by zero
        if conflictNumber[0]==0:
            weight.append(2)
        else:
            weight.append(1/conflictNumber[0])

    #use random with probability to choose parent
    parent1 = random.choices(population, weight)[0]
    parent2 = random.choices(population, weight)[0]
    while parent1 == parent2:
        parent2 = random.choices(population, weight)[0]

    #choose the crossover point
    #use two-point crossover
    crossoverBeginPoint = random.randint(0,len(parent1)-1)
    crossoverEndingPoint = random.randint(0,len(parent1)-1)

    #begining point must be more than it's ending point
    if crossoverBeginPoint > crossoverEndingPoint:
        temp = crossoverBeginPoint
        crossoverBeginPoint = crossoverEndingPoint
        crossoverEndingPoint = temp

    #make child that inherit both parents genes
    child = convertMatrixToListOfPiece(convertListOfPieceToMatrix(parent1))
    child.sort(key=getJenis)
    parent2.sort(key=getJenis)

    #mix genes from parent1 and parent2
    childMatrix = convertListOfPieceToMatrix(child)
    for i in range(crossoverBeginPoint, crossoverEndingPoint):
        #check whether the position has occupied
        if(childMatrix[parent2[i].posisiX][parent2[i].posisiY] == ''):
            child[i] = parent2[i]
        childMatrix = convertListOfPieceToMatrix(child)
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
        if((matrix[piecePos[0]][piecePos[1]])!=''):
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


def geneticAlgorithm(chessPieces):
    #Program Test
    totalPopulation = 50

    #tolong cek di bawah ini kenapa kalo boardnya dari input dari input_helper.board kenapa gabisa
    #population = initPopulation(totalPopulation, board)
    population = initPopulation(totalPopulation, chessPieces)
    bestSolutionOverall = population[0]
    for x in range(0,1000):
        crossover(population)
        removeWorstConfiguration(population)
        for x in range (0, totalPopulation):
            if(random.randint(1,100) % 7 == 0):
                mutation(population[x])
        bestSolution = getBestFit(population)
        if(isBetter(evaluator.boardNumConflicting(convertListOfPieceToMatrix(bestSolution)), evaluator.boardNumConflicting(convertListOfPieceToMatrix(bestSolutionOverall)))):
            bestSolutionOverall = bestSolution
        """
        for y in range(totalPopulation):
            input_helper.display_board(convertListOfPieceToMatrix(population[y]))
            print()
        """
    return convertListOfPieceToMatrix(bestSolutionOverall)
    """
    input_helper.display_board()
    bestSolutionConflicts = evaluator.boardNumConflicting(convertListOfPieceToMatrix(bestSolutionOverall))
    print(bestSolutionConflicts[0],bestSolutionConflicts[1])
"""
