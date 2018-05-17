import argparse
import numpy as np


class Board(object):
	def __init__(self, n):
		self.n = n
		self.boardHuman = np.chararray((n, n))
		self.boardComputer = np.chararray((n, n))
		self.boardHuman[:] = b''
		self.boardComputer[:] = b''

	@staticmethod
	def terminalTest(self, board):
		isTerminal = False
		utility = 0
		foundAt = -1
		for i in range(board.shape[0]):
			if board[0][i] == tile:
				foundAt = i
				break
		mid = board.shape[0]/2
		if board.shape[0]%2 == 1:
			mid += 1
			if board[mid][mid] == tile:
				# Check two diagonal
				pass
		else:
			if board[mid][mid] == tile:
				pass
			if board[mid][mid-1] == tile:
				pass
		return False

	def getLegalMoves(self):
		for i in range(len(self.board)):
			pass

	def getTileAt(self, x, y):
		if self.boardHuman[x][y] == self.boardComputer[x][y]:
			return ' '
		if self.boardHuman[x][y] == b'x':
			return 'x'
		else:
			return 'o'

	def show(self):
		for i in range(self.n):
			for j in range(self.n-1):
				print(self.getTileAt(i, j), end='|')
			print(self.getTileAt(i, self.n-1))

class Minimax:
	"""docstring for minimax"""
	def dls():
		"""Depth Limited Search"""
		pass

	def ids():
		""" Iterative Deepening Search """
		pass

	def minimize(self, state):
		if state.isTerminal():
			return None

	def maximize(self, state):
		if state.isTerminal():
			return None
		for childs in state.children():
			pass

	def decision(self, board, depth):
		maxvalue = float("-inf")
		bestMove = (-1, -1)
		legalMoves = board.getLegalMoves(self)
		if len(legalMoves) >= 1:
			bestMove = legalMoves.pop()
		else:
			return bestMove


def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("n", help="Size of n*n board", type=int)
	args = parser.parse_args()
	game = Board(args.n)
	# minimax = Minimax(game)

	game.show()
	print("To make move, input row and column separated by space.")

	# while True:
	# 	# if board.isTerminal():
	# 	# 	break
	# 	move = int(input("Your move: "))
	# 	move = move.split(" ")


if __name__ == '__main__':
	main()