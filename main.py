import time
import os
import random

def disperseLittleDots(rows, cols):
    grid = [ [0 for _ in range(cols)] for _ in range(rows)]
    for col in range(cols - 1):
        for row in range(rows - 1):
            r = random.randint(0, 7)
            if r == 0:   grid[row][col] = 2
            elif r == 1: grid[row][col] = 1
            else:        grid[row][col] = 0
    return grid

def computeNextGeneration(grid):
    nextGrid = [ [0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
    changing = False
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            live_neighbors = getNeighbours(row, col, grid)
            if live_neighbors not in [2,3]:
                nextGrid[row][col] = 0
                changing = True
            elif live_neighbors in [3] and grid[row][col] == 2:
                nextGrid[row][col] = 1
                changing = True
            elif live_neighbors in [3]:
                nextGrid[row][col] = 2
                changing = True
            else:
                nextGrid[row][col] = grid[row][col]
    return nextGrid, changing

def getNeighbours(row, col, grid):
    alives = 0
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            if not (i == 0 and j == 0):
                if grid[((row + i) % len(grid))][((col + j) % len(grid[0]))] >= 1:
                    alives += 1
    return alives

def prettyPrint(grid, step):
    map = {
        0:'  ',#'\033[39m⋅ ',
        1:'\033[38;5;165m⬤ \033[49m',  # '💖️'
        2:'\033[38;5;105m⬤ \033[49m',  # '💜️'
    }

    os.system('clear')
    strToPrint = ''
    strToPrint += '\n┌'+'─'*len(grid[0]) * 2+'┐\n'
    for row in grid:
        strToPrint += '│'
        for col in row:
            strToPrint += map[col]
        strToPrint += '│\n'
    strToPrint += '└'+'─'*len(grid[0]) * 2+'┘\n'
    strToPrint += 'GENERATION '+'% 3d' % step
    print(strToPrint)


def play(rows, cols):
    game = disperseLittleDots(rows, cols)
    gen = 1
    changing = True
    while changing:
        prettyPrint(game, gen)
        game, changing = computeNextGeneration(game)
        gen += 1
        time.sleep(.1)

play(50, 100)
