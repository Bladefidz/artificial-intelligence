import sys
import time
import resource
from collections import deque


'''
	Solve 8 puzzle game.
	Execution	: python driver.py <method> <board>
	Example 	: python driver.py bfs 0,8,7,6,5,4,3,2,1
	Output 		: output.txt
'''

board = None  # Our working board, Will became list if successfully initialized
path = deque()  # The sequence of moves taken to reach the goal
nodesExpanded = 0  # The number of nodes that have been expanded
searchDepth = 0  # The depth within the search tree when the goal node is found
maxSearchDepth = 0  # The maximum depth of the search tree in the lifetime of the algorithm
timeStart = 0.0

def move(xy1, xy2):
	return 1

def parseMove():
	'''
		Parse moves stored in path contains integers 1, 2, 3 or 4.
		Parse 1 as Up, 2, as Right, 3 as Down and 4 as Left.
	'''
	moves = []
	for i in len(path):
		m = path.popleft()
		if m == 1:
			moves.append("Up")
		elif m == 2:
			moves.append("Right")
		elif m == 3:
			moves.append("Down")
		elif m == 4:
			moves.append("Left")
	return moves

def output():
	'''
		Parse search statistics and save it into output.txt
	'''
	f = open('output.txt', 'w')
	f.write("path_to_goal: {}\n".format(parseMove()))
	f.write("cost_of_path: {}\n".format(len(pathToGoal)))
	f.write("nodes_expanded: {}\n".format(nodesExpanded))
	f.write("search_depth: {}\n".format(searchDepth))
	f.write("max_search_depth: {}\n".format(maxSearchDepth))
	f.write("running_time: {}\n".format(time.time() - timeStart))
	f.write("max_ram_usage: {}\n".format(
		resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024)
	)
	f.close()

def updateMaxSearchDepth(depth):
	if depth > maxSearchDepth:
		maxSearchDepth = depth

def hammingDistance(b):
	d = 0
	for i in range(9):
		if b[i] != i:
			d += 1
	return d

def manhattanDistance(b):
	d = 0;
	for i in range(9):
		if (b[i] - i) > 0:
			d += 1
		elif (b[i] - i) < 0:
			d += 1
	return d

def bfs():
	'''
		Breadth-First Search
	'''
	return 1

def dfs():
	'''
		Depth-First Search
	'''
	return 1

def ast():
	'''
		A-Star Search
	'''
	return 1

def solve(method):
	'''
		Solve given board using given algorithm
	'''
	if (board is not None):
		timeStart = time.time()

		if (method == "bfs"):
			bfs()
		elif (method == "dfs"):
			dfs()
		elif (method == "ast"):
			ast()

def initBoard(tmpBoard):
	'''
		Evaluate and build board from string
	'''
	if (len(tmpBoard) == 9):
		board = tmpBoard

		# Checking for duplicate
		tmpBoard.sort()
		for i in range(len(tmpBoard) - 1):
			if (tmpBoard[i] == tmpBoard[i + 1]):
				board = None
				print("A board contains duplicated tile!")
				break
	else:
		print("A board must be consisted 9 tiles!")


if __name__ == '__main__':
	if (len(sys.argv) >= 2):
		# Initialize 8 puzzle board
		initBoard([int(i) for i in sys.argv[2].split(',')])

		# Run search algorithm
		solve(sys.argv[1])