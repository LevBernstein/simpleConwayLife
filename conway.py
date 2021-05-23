# Simple Python implementation of Conway's Game of Life
# Author: Lev Bernstein

from random import randint
from time import sleep
from os import name, system

# Board size
WIDTH = 30
HEIGHT = 30

# Number of generations to simulate
RUNS = 200

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
    sleep(.25)

def alive(board, y, x):
    left = x - 1 if x > 0 else WIDTH-1
    right = x + 1 if x < WIDTH-1 else 0
    up = y - 1 if y > 0 else HEIGHT-1
    down = y + 1 if y < HEIGHT-1 else 0
    neighbors = sum([board[up][left], board[y][left], board[down][left], board[up][x], board[down][x], board[up][right], board[y][right], board[down][right]])
    return 1 if (board[y][x] == 0 and neighbors == 3) or (board[y][x] == 1 and (neighbors == 2 or neighbors == 3)) else 0

def game(board, generations):
    status(board)
    for i in range(generations):
        newBoard = [[0 for i in range(WIDTH)] for j in range(HEIGHT)]
        for i in range(HEIGHT):
            for j in range(WIDTH): newBoard[i][j] = alive(board, i, j)
        if board == newBoard:
            break
        board = newBoard
        status(board)
        if sum(row.count(1) for row in board) == 0:
            break

if __name__ == "__main__":
    game(setup(), RUNS)