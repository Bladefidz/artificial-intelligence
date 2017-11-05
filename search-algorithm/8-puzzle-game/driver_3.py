import sys
import math
import time
import resource
from collections import deque
from queue import PriorityQueue


'''
	Solve 8 puzzle game.
	Order of movements is UDLR (Up, Down Left and Right).

	Execution	: python driver.py <method> <board>
	Example 	: python driver.py bfs 0,8,7,6,5,4,3,2,1
	Goal		: 0, 1, 2, 3, 4, 5, 6, 7, 8
	Output 		: output.txt
'''

class Board(object):
	"""
		Board representation
	"""
	def __init__(self, board, predecessor, move, depth):
		self.board = board
		self.dimension = int(math.sqrt(len(board)))
		self.predecessor = predecessor
		self.move = move
		self.depth = depth
		self.manhattan = 0

		self.id = 0
		if self.board[0] != 0:
			for i in range(len(self.board) - 1, -1, -1):
				self.id += self.board[len(self.board) - i - 1] * 10 ** i

	def hasDuplicate(self):
		'''
			Evaluate board if has duplicated tile
		'''
		tmp = self.board.copy()
		tmp.sort()
		for i in range(len(tmp) - 1):
			if (tmp[i] == tmp[i + 1]):
				return true
		return false

	def hammingDistance(self, q):
		'''
			Calculate difference between current board and board q.
			Return 0 if both are equal.
			Return 1 to N indicate how many differences between two board.
		'''
		d = 0
		for i in q:
			if self.board[i] != q[i]:
				d += 1
		return d

	def manhattanDistance(self, q):
		'''
			Manhattan distance each point in current board to q
		'''
		if self.manhattan == 0:
			self.manhattan = 0
			n = len(q)
			m = math.sqrt(n)

			# Build dictionary for easier and faster lookup
			r = {}
			for i in range(n):
				r[q[i]] = i

			# Find only wrong placed tiles and calculate its distance to right place.
			for i in range(n):
				if self.board[i] != q[i]:
					# (x1, y1) is wrong position
					x1 = i % m
					y1 = math.ceil(((n - i) / m) - 1)

					# Index of right position
					j = r[self.board[i]]

					# (x2, y2) is right position
					x2 = j % m
					y2 = math.ceil(((n - j) / m) - 1)

					self.manhattan += abs(x2 - x1) + abs(y2 - y1)
			self.manhattan = int(self.manhattan)
		return self.manhattan

	def cloneSwap(self, i, j):
		'''
			Clone current board and exchange value of i into j and otherwise.
		'''
		clone = self.board.copy()
		clone[i] = self.board[j]
		clone[j] = self.board[i]
		return clone

	def getNeighborsMoves(self):
		'''
			Move zero tile by UDLR (Up, Down, Left, Right) movement rule.
		'''
		# Find zero position
		iZero = 0
		for i in range(len(self.board)):
			if self.board[i] == 0:
				iZero = i

		# Parse movements
		neighbors = []
		moves = []

		if (iZero >= self.dimension):
			# Move Up
			neighbors.append(
				Board(
					self.cloneSwap(iZero, iZero - self.dimension),
					self,
					'Up',
					self.depth + 1
				)
			)

		if (iZero < len(self.board) - self.dimension):
			# Move Down
			neighbors.append(
				Board(
					self.cloneSwap(iZero, iZero + self.dimension),
					self,
					'Down',
					self.depth + 1
				)
			)

		if (iZero % self.dimension != 0):
			# Move left
			neighbors.append(
				Board(
					self.cloneSwap(iZero, iZero - 1),
					self,
					'Left',
					self.depth + 1
				)
			)

		if ((iZero + 1) % self.dimension != 0):
			# Move right
			neighbors.append(
				Board(
					self.cloneSwap(iZero, iZero + 1),
					self,
					'Right',
					self.depth + 1
				)
			)

		return neighbors

	def getNeighborsMovesRevs(self):
		'''
			Move zero tile by RLDU (Right, Left, Down, Up) movement rule.
		'''
		# Find zero position
		iZero = 0
		for i in range(len(self.board)):
			if self.board[i] == 0:
				iZero = i

		# Parse movements
		neighbors = []
		moves = []

		if ((iZero + 1) % self.dimension != 0):
			# Move right
			neighbors.append(
				Board(
					self.cloneSwap(iZero, iZero + 1),
					self,
					'Right',
					self.depth + 1
				)
			)

		if (iZero % self.dimension != 0):
			# Move left
			neighbors.append(
				Board(
					self.cloneSwap(iZero, iZero - 1),
					self,
					'Left',
					self.depth + 1
				)
			)

		if (iZero < len(self.board) - self.dimension):
			# Move Down
			neighbors.append(
				Board(
					self.cloneSwap(iZero, iZero + self.dimension),
					self,
					'Down',
					self.depth + 1
				)
			)

		if (iZero >= self.dimension):
			# Move Up
			neighbors.append(
				Board(
					self.cloneSwap(iZero, iZero - self.dimension),
					self,
					'Up',
					self.depth + 1
				)
			)

		return neighbors

	def __str__(self):
		s = ""
		for i in range(len(self.board)):
			s += str(self.board[i])
			if (i + 1) % 3 == 0:
				s += '\n'
			else:
				s += ' '
		return s

	def __lt__(self, other):
		return (self.manhattan + self.depth) < (other.manhattan + other.depth)

	def __eq__(self, other):
		return (self.manhattan + self.depth) == (other.manhattan + other.depth)

	def __gt__(self, other):
		return (self.manhattan + self.depth) > (other.manhattan + other.depth)


class Solver(object):
	"""
		Board solver using three different algorithms:
	"""
	def __init__(self, board, goal):
		self.board = Board(board, None, None, 0)
		self.goal = goal
		self.bestBoard = None
		self.cost = 0
		self.expandedNode = 0
		self.searchDepth = 0
		self.maxSearchDepth = 0
		self.timeStart = 0.0
		self.timeEnd = 0.0
		self.solved = False

	def bfs(self):
		'''
			Breadth-First Search
		'''
		self.timeStart = time.time()

		frontiers = deque()
		explored = set()

		frontiers.append(self.board)

		while len(frontiers) > 0:
			self.bestBoard = frontiers.popleft()
			explored.add(self.bestBoard.id)

			if (self.bestBoard.hammingDistance(self.goal) == 0):
				self.searchDepth = self.bestBoard.depth
				self.cost = self.bestBoard.depth
				self.solved = True
				break
			else:
				for n in self.bestBoard.getNeighborsMoves():
					if n.id not in explored:
						frontiers.append(n)

						self.expandedNode += 1
						if n.depth > self.maxSearchDepth:
							self.maxSearchDepth = n.depth
						# print(self.expandedNode)
						# print(n)

		self.timeEnd = time.time()

	def dfs(self):
		'''
			Depth-First Search
		'''
		self.timeStart = time.time()

		frontiers = []
		explored = set()

		frontiers.append(self.board)

		while len(frontiers) > 0:
			self.bestBoard = frontiers.pop()
			explored.add(self.bestBoard.id)

			if (self.bestBoard.hammingDistance(self.goal) == 0):
				self.searchDepth = self.bestBoard.depth
				self.cost = self.bestBoard.depth
				self.solved = True
				break
			else:
				for n in self.bestBoard.getNeighborsMovesRevs():
					if n.id not in explored:
						frontiers.append(n)

						self.expandedNode += 1
						if n.depth > self.maxSearchDepth:
							self.maxSearchDepth = n.depth

		self.timeEnd = time.time()

	def ast(self):
		'''
			A-Star Search
		'''
		self.timeStart = time.time()

		pq = PriorityQueue()
		explored = set()

		self.board.manhattanDistance(self.goal)
		pq.put(self.board)

		while pq.qsize() > 0:
			self.bestBoard = pq.get()
			explored.add(self.bestBoard.id)

			if (self.bestBoard.hammingDistance(self.goal) == 0):
				self.searchDepth = self.bestBoard.depth
				self.cost = self.bestBoard.manhattan + self.bestBoard.depth
				self.solved = True
				break
			else:
				for n in self.bestBoard.getNeighborsMoves():
					if n.id not in explored:
						pq.put(n)

						self.expandedNode += 1
						if n.depth > self.maxSearchDepth:
							self.maxSearchDepth = n.depth

		self.timeEnd = time.time()

	def isSolved(self):
		return self.solved

	def getPath(self):
		if self.bestBoard is not None:
			path = deque()
			b = self.bestBoard
			while b.predecessor is not None:
				path.appendleft(b.move)
				b = b.predecessor
			return list(path)
		return None

	def solveTime(self):
		return self.timeEnd - self.timeStart


def solve(method, board):
	'''
		Solve given board using given algorithm
	'''
	if (board is not None):
		solver = Solver(board, [0, 1, 2, 3, 4, 5, 6, 7, 8])
		if (method == "bfs"):
			solver.bfs()
		elif (method == "dfs"):
			solver.dfs()
		elif (method == "ast"):
			solver.ast()
		else:
			return False

		f = open('output.txt', 'w')
		f.write("path_to_goal: {}\n".format(list(solver.getPath())))
		f.write("cost_of_path: {}\n".format(solver.cost))
		f.write("nodes_expanded: {}\n".format(solver.expandedNode))
		f.write("search_depth: {}\n".format(solver.searchDepth))
		f.write("max_search_depth: {}\n".format(solver.maxSearchDepth))
		f.write("running_time: {}\n".format(solver.solveTime()))
		f.write("max_ram_usage: {}\n".format(
			resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024)
		)
		f.close()


if __name__ == '__main__':
	if (len(sys.argv) > 2):
		# Run search algorithm
		solve(sys.argv[1], [int(i) for i in sys.argv[2].split(',')])