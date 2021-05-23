# Simple Python implementation of Conway's Game of Life
# Author: Lev Bernstein

from random import randint
from time import sleep
from os import name, system

# MUSTFIX: sometimes random lines show up that should not exist

# Board size
WIDTH = 30
HEIGHT = 30

# Number of generations to simulate
RUNS = 100

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
    #system("cls" if name == 'nt' else "clear") # assume everything but Windows is unix-based
    print("AAAAAAAAAAAAAAAAA") # temporary while I try to figure out what's going wrong
    for row in board:
        answer = ""
        for num in row: answer += "O   " if num == 1 else "_   "
        print(answer[:-3] + "\n")
    sleep(.25)

def alive(board, y, x):
    neighbors = 0
    left = x - 1 if x > 0 else 9
    right = x + 1 if x < 9 else 0
    up = y - 1 if y > 0 else 9
    down = y + 1 if y < 9 else 0
    #print(left, right, up, down)
    neighbors += board[up][left] + board[y][left] + board[down][left] + board[up][x] + board[down][x] + board[up][right] + board[y][right] + board[down][right]
    #print(neighbors)
    return 1 if (board[y][x] == 0 and neighbors == 3) or (board[y][x] == 1 and (neighbors == 2 or neighbors == 3)) else 0

def game(board, generations):
    status(board)
    for i in range(generations):
        newBoard = [[0 for i in range(WIDTH)] for j in range(HEIGHT)]
        for i in range(HEIGHT):
            for j in range(WIDTH): newBoard[i][j] = alive(board, i, j)
        board = newBoard
        status(board)

if __name__ == "__main__":
    game(setup(), RUNS)