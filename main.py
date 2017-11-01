import time
import math
from random import randint,uniform
from copy import deepcopy

MAX_QUEEN = 10
MAX_T = 100
RATE = 0.01
QUEEN = [{'posX': 0, 'posY': 0}]

def getInitialBoard():
    i = 0
    while i < MAX_QUEEN - 1:
        x = randint(0, MAX_QUEEN - 1)
        y = randint(0, MAX_QUEEN - 1)
        flagQ = True
        for q in QUEEN:
            if q['posX'] == x and q['posY'] == y:
                flagQ = False
        if flagQ == True:
            QUEEN.append({'posX': x, 'posY': y})
            i += 1

def getEnergy(queens):
    queenSize = len(queens)
    energy = 0
    for queenIndex in range(0, queenSize):
        queenX = queens[queenIndex]['posX']
        queenY = queens[queenIndex]['posY']
        for loop in range(0, queenSize):
            if (queenX == queens[loop]['posX'] or queenY == queens[loop]['posY']) and loop != queenIndex:
                energy+=1
        while queenX != 0 and queenY != 0:
            queenX-=1
            queenY-=1
            for loop in range(0, queenSize):
                if (queenX == queens[loop]['posX'] and queenY == queens[loop]['posY']) and loop != queenIndex:
                    energy+=1
        queenX = queens[queenIndex]['posX']
        queenY = queens[queenIndex]['posY']
        while queenY != 0 and queenX != queenSize-1:
            queenX+=1
            queenY-=1
            for loop in range(0, queenSize):
                if (queenX == queens[loop]['posX'] and queenY == queens[loop]['posY']) and loop != queenIndex:
                    energy+=1
        queenX = queens[queenIndex]['posX']
        queenY = queens[queenIndex]['posY']
        while queenX != 0 and queenY != queenSize-1:
            queenX-=1
            queenY+=1
            for loop in range(0, queenSize):
                if (queenX == queens[loop]['posX'] and queenY == queens[loop]['posY']) and loop != queenIndex:
                    energy+=1
        queenX = queens[queenIndex]['posX']
        queenY = queens[queenIndex]['posY']
        while queenX != queenSize-1 and queenY != queenSize-1:
            queenX+=1
            queenY+=1
            for loop in range(0, queenSize):
                if (queenX == queens[loop]['posX'] and queenY == queens[loop]['posY']) and loop != queenIndex:
                    energy+=1
    return MAX_QUEEN * MAX_QUEEN - energy

def checkSamePosition(x, y) :
    for q in QUEEN :
        if q['posX'] == x and q['posY'] == y :
            return False
    return True

def moveQueen() :
    repeat = True
    newQueen = deepcopy(QUEEN)
    while repeat :
        movingQueen = randint(0, MAX_QUEEN - 1)

        newX = (QUEEN[movingQueen]['posX'] + (((randint(0, 1) * (MAX_QUEEN - 1)) + 1))) % MAX_QUEEN
        newY = (QUEEN[movingQueen]['posY'] + (((randint(0, 1) * (MAX_QUEEN - 1)) + 1))) % MAX_QUEEN

        if checkSamePosition(newX, newY) :
            repeat = False
            newQueen[movingQueen]['posX'] = newX
            newQueen[movingQueen]['posY'] = newY
    return newQueen

def getProb(delta,t) :
    return 1 / math.exp(math.fabs(delta) / t)

def simulatedAnnealing() :
    global QUEEN, RATE
    getInitialBoard()
    T = MAX_T
    progressTime = MAX_T * 5 / 100
    while T > 1 :
        currentE = getEnergy(QUEEN)
        nextQ = moveQueen()
        nextE = getEnergy(nextQ)
        delta = nextE - currentE
        if int( MAX_T - T ) % progressTime == 0 :
            print(T, "Progress :", int((1 - ( T / MAX_T  )) * 100), "Current Energy :", currentE, "Probability :", getProb(delta,T))
        if delta > 0 :
            QUEEN = nextQ
        else :
            if uniform(0, 1) < getProb(delta, T) :
                QUEEN = nextQ
        if getEnergy(QUEEN) == MAX_QUEEN * MAX_QUEEN :
            break
        T *= 1 - RATE

def createmap(posQ):
    matrix = [["-"] * MAX_QUEEN for i in range(MAX_QUEEN)]
    for q in posQ:
        xx = q['posX']
        yy = q['posY']
        matrix[xx][yy] = 'Q'
    for j in range(MAX_QUEEN):
        for i in range(MAX_QUEEN):
            print(" |", end='')
            print(matrix[i][j], end='')
            print("| ", end='')
        print('')
        for k in range(MAX_QUEEN):
            print('  -  ', end='')
        print('')

MAX_QUEEN = int(input("Max Queen : "))
MAX_T = float(input("Initial Temp : "))
RATE = float(input("Cooling Rate : "))
print("Start Time :",time.strftime("%d/%m/%Y"), time.strftime("%H:%M:%S"))
simulatedAnnealing()
print("Finish Time Time :",time.strftime("%d/%m/%Y"), time.strftime("%H:%M:%S"))
print("Final Map :")
createmap(QUEEN)
print(getEnergy(QUEEN))