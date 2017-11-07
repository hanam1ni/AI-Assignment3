import time
import math
from random import randint,uniform
from copy import deepcopy

def getInitialBoard(nQueen):
    QUEEN = [{'posX': 0, 'posY': 0}]
    i = 0
    while i < nQueen - 1:
        x = randint(0, nQueen - 1)
        y = i
        flagQ = True
        for q in QUEEN:
            if q['posX'] == x :
                flagQ = False
        if flagQ == True:
            QUEEN.append({'posX': x, 'posY': y})
            i += 1
    return QUEEN

def getEnergy(queens, nQueen):
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
    return nQueen * nQueen - energy

def checkSamePosition(x, y) :
    for q in QUEEN :
        if q['posX'] == x and q['posY'] == y :
            return False
    return True

def moveQueen(QUEEN, nQueen) :
    newQueen = deepcopy(QUEEN)
    movingQueen = randint(0, nQueen - 1)
    newQueen[movingQueen]['posX'] = (QUEEN[movingQueen]['posX'] + randint(1, nQueen - 1)) % nQueen
    newQueen[movingQueen]['posY'] = movingQueen

    return newQueen

def getProb(delta,t) :
    return 1 / math.exp(math.fabs(delta) / t)

def simulatedAnnealing(rate, initTemp, nQueen) :
    if nQueen != 1 :
        startTime = time.time()
        QUEEN = getInitialBoard(nQueen)
        T = initTemp
        progressTime = initTemp * 5 / 100
        while T > 1 :
            currentE = getEnergy(QUEEN, nQueen)
            nextQ = moveQueen(QUEEN, nQueen)
            nextE = getEnergy(nextQ, nQueen)
            delta = nextE - currentE
            if int( initTemp - T ) % progressTime == 0 :
                if delta > 0:
                    print(T, "\tP: ", int((1 - ( T / initTemp  )) * 100), "\tE: ", currentE, "\tP: Not Used")
                else :
                    print(T, "\tP: ", int((1 - ( T / initTemp  )) * 100), "\tE: ", currentE, "\tP: ", getProb(delta,T))
            if delta > 0 :
                QUEEN = nextQ
            else :
                if uniform(0, 1) < getProb(delta, T) :
                    QUEEN = nextQ
            if getEnergy(QUEEN, nQueen) == nQueen * nQueen :
                break
            T *= 1 - rate
        timeElapsed = time.time() - startTime
        return {'solution': QUEEN, 'timeElapsed': timeElapsed}
    return 0

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

if __name__ == "__main__":
    startDate = time.strftime("%d/%m/%Y")
    startTime = time.strftime("%H:%M:%S")
    finishDate = time.strftime("%d/%m/%Y")
    finishTime = time.strftime("%H:%M:%S")