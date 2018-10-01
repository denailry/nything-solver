import random
from utils import input_helper
from utils import evaluator

listOfPiece = []
population = []

# A piece in the chess, contains it's category and position
class Piece:
    def __init__(self, jenis, posisiX, posisiY):
        self.jenis = jenis # Q,K,B,R,q,k,b,r
        self.posisiX = posisiX
        self.posisiY = posisiY

# Is the numConflicting1 better than numConflicting2
def is_better(numConflicting1, numConflicting2):
    #minimum ally-attacking is prioritized
    if(numConflicting1[0] < numConflicting2[0]):
        return True
    elif(numConflicting1[0] == numConflicting2[0] and numConflicting1[1] > numConflicting2[1]):
        return True
    return False

def convert_matrix_to_list(matrix):
    listOfPiece = []
    for i in range(8):
        for j in range(8):
            if(matrix[i][j]!=''):
                listOfPiece.append(Piece(matrix[i][j],i,j))

    return listOfPiece

def convert_list_to_matrix(listOfPiece):
    board = [[] for i in range(8)]
    for i in range(8):
        board[i] = ['' for i in range(8)]
    for (piece) in listOfPiece:
        board[piece.posisiX][piece.posisiY] = piece.jenis
    return board

# Initialize the population with random pieces
def initialize_population(total_population, pieces):
    population = []
    for j in range(total_population):
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
        population.append(convert_matrix_to_list(board))
    return population

# Get best configuration in population
def get_best_fit(population):
    #initialize the best fit
    bestFitParent = population[0]
    bestFitConflicting = evaluator.boardNumConflicting(convert_list_to_matrix(bestFitParent))

    #searching for the best fit configuration in population
    for pieceList in population:
        numConflicting = evaluator.boardNumConflicting(convert_list_to_matrix(pieceList))
        if(is_better(numConflicting,bestFitConflicting)):
            bestFitParent = pieceList
            bestFitConflicting = numConflicting
    return bestFitParent

# Add child to population that inherits it's parents genes
def crossover(population):
    # Using russian roulette method
    weight = []
    # Get probability for each configuration
    for configuration in population:
        conflictNumber = evaluator.boardNumConflicting(convert_list_to_matrix(configuration))
        #prevent division by zero
        if conflictNumber[0]==0:
            weight.append(2)
        else:
            weight.append(1/conflictNumber[0])

    # Use random with probability to choose parent
    parent1 = random.choices(population, weight)[0]
    parent2 = random.choices(population, weight)[0]
    while parent1 == parent2:
        parent2 = random.choices(population, weight)[0]

    # Choose the crossover point
    # Use two-point crossover
    crossoverBeginPoint = random.randint(0,len(parent1)-1)
    crossoverEndingPoint = random.randint(0,len(parent1)-1)

    #begining point must be more than it's ending point
    if crossoverBeginPoint > crossoverEndingPoint:
        temp = crossoverBeginPoint
        crossoverBeginPoint = crossoverEndingPoint
        crossoverEndingPoint = temp

    # Make child that inherit both parents genes
    child = convert_matrix_to_list(convert_list_to_matrix(parent1))
    child.sort(key=lambda piece:piece.jenis)
    parent2.sort(key=lambda piece:piece.jenis)

    # Mix genes from parent1 and parent2
    childMatrix = convert_list_to_matrix(child)
    for i in range(crossoverBeginPoint, crossoverEndingPoint):
        # Check whether the position has occupied
        if(childMatrix[parent2[i].posisiX][parent2[i].posisiY] == ''):
            child[i] = parent2[i]
        childMatrix = convert_list_to_matrix(child)
    population.append(child)

# Remove the worst performing configuration in population
def remove_worst_config(population):
    worstConfiguration = population[0]
    worstConfigurationConflicting = evaluator.boardNumConflicting(convert_list_to_matrix(worstConfiguration))
    for listOfPiece in population:
        listOfPieceConflicting = evaluator.boardNumConflicting(convert_list_to_matrix(listOfPiece))
        if(is_better(worstConfigurationConflicting, listOfPieceConflicting)):
            worstConfiguration = listOfPiece
            worstConfigurationConflicting = listOfPieceConflicting
    population.remove(worstConfiguration)

# Randomly change one piece place
def mutation(listOfPiece):
    matrix = convert_list_to_matrix(listOfPiece)

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

    # Change the piece
    matrix[destinationPos[0]][destinationPos[1]] = matrix[piecePos[0]][piecePos[1]]
    matrix[piecePos[0]][piecePos[1]] = ''

    listOfPiece = convert_matrix_to_list(matrix)

def solve(chess_pieces, generation_limit):
    total_population = 50
    population = initialize_population(total_population, chess_pieces)
    best_solution_overall = population[0]
    for generation in range(generation_limit):
        print('\rGeneration number {}, record best: {}'.format(generation, evaluator.boardNumConflicting(convert_list_to_matrix(best_solution_overall))), end='')
        crossover(population)
        remove_worst_config(population)
        for x in range (total_population):
            if(random.randint(1,100) % 7 == 0):
                mutation(population[x])
        best_solution = get_best_fit(population)
        if(is_better(evaluator.boardNumConflicting(convert_list_to_matrix(best_solution)), evaluator.boardNumConflicting(convert_list_to_matrix(best_solution_overall)))):
            best_solution_overall = best_solution
            print()
    print()
    return convert_list_to_matrix(best_solution_overall)
