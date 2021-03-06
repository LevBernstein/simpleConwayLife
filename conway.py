# Simple Python implementation of Conway's Game of Life
# Author: Lev Bernstein

from random import randint
from time import sleep
from os import name, system

# Board size
WIDTH = 60
HEIGHT = 30

# Number of generations to simulate
TICKS = 500

def setup():
    system("cls" if name == 'nt' else "clear") # assume everything but Windows is unix-based
    valid = False
    while not valid:
        board = [[randint(0,1) for i in range(WIDTH)] for j in range(HEIGHT)]
        status(board)
        answer = input("Is this starting seed acceptable?\n").lower()
        if answer == "yes" or answer == "y": valid = True
    return board

def status(board):
    system("cls" if name == 'nt' else "clear") # assume everything but Windows is unix-based
    for row in board:
        answer = ""
        for num in row: answer += "O   " if num == 1 else "_   "
        print(answer[:-3] + "\n")
    sleep(.2)

def alive(board, y, x):
    left = (x - 1) % WIDTH
    right = (x + 1) % WIDTH
    up = (y - 1) % HEIGHT
    down = (y + 1) % HEIGHT
    neighbors = sum([board[up][left], board[y][left], board[down][left], board[up][x], board[down][x], board[up][right], board[y][right], board[down][right]])
    return 1 if (board[y][x] == 0 and neighbors == 3) or (board[y][x] == 1 and (neighbors == 2 or neighbors == 3)) else 0

def game(board, generations):
    status(board)
    oldBoard = board
    for n in range(generations):
        newBoard = [[0 for a in range(WIDTH)] for b in range(HEIGHT)]
        for i in range(HEIGHT):
            for j in range(WIDTH): newBoard[i][j] = alive(board, i, j)
        status(newBoard)
        if board == newBoard or oldBoard == newBoard or sum(row.count(1) for row in board) == 0: break
        oldBoard = board
        board = newBoard
    print("Ended on generation " + str(n+1))

if __name__ == "__main__":
    game(setup(), TICKS)