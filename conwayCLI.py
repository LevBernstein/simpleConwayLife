# Simple Python implementation of Conway's Game of Life
# Author: Lev Bernstein

from random import randint
from time import sleep
from os import name, system

# Board size
WIDTH = 27
HEIGHT = 18

# Number of generations to simulate
TICKS = 5000


def clear():
	system("cls" if name == 'nt' else "clear") # assume everything but Windows is unix-based


def setup():
	clear()
	while True:
		board = [[randint(0,1) for i in range(WIDTH)] for j in range(HEIGHT)]
		status(board)
		answer = input("Is this starting seed acceptable?\n").lower()
		if answer in ("yes", "y"):
			return board


def status(board):
	clear()
	for row in board:
		print("   ".join(("O" if num == 1 else "_" for num in row)) + "\n")
	sleep(.2)


def alive(board, y, x):
	left = (x - 1) % WIDTH
	right = (x + 1) % WIDTH
	up = (y - 1) % HEIGHT
	down = (y + 1) % HEIGHT
	neighbors = sum([
		board[up][left],
		board[y][left],
		board[down][left],
		board[up][x],
		board[down][x],
		board[up][right],
		board[y][right],
		board[down][right]
	])
	return (board[y][x] == 0 and neighbors == 3) or (board[y][x] == 1 and neighbors in (2, 3))


def game(board, generations):
	status(board)
	oldBoard = board
	for n in range(generations):
		newBoard = [[0 for a in range(WIDTH)] for b in range(HEIGHT)]
		for i in range(HEIGHT):
			for j in range(WIDTH):
				newBoard[i][j] = int(alive(board, i, j))
		status(newBoard)
		if newBoard in (board, oldBoard) or sum(row.count(1) for row in board) == 0:
			break
		oldBoard = board
		board = newBoard
	print(f"Ended on generation {n+1}.")


if __name__ == "__main__":
	game(setup(), TICKS)
