import sys
import copy

# ttt.py
#
# Implementation of MiniMax and Alpha Beta Pruning search for TicTacToe puzzle
#
# Usage: python ttt.py
#
# Author: Siddesh Pillai, RIT, 14 Feb. 2014

# global count
count = 0

#Prints the board
def print_board(board):
	for i in range(len(board)):
		print(board[i], end=" "),
		if ( (i+1)%3 == 0 ):
			print()

# Terminal function which checks whether it is a goal and returns the boolean
# value
def goal_condition(board):
	if( ( board[0] == board[1] == board[2] == 'X') |
		( board[0] == board[1] == board[2] == 'O') |
		( board[0] == board[4] == board[8] == 'X') |
		( board[0] == board[4] == board[8] == 'O') |
		( board[0] == board[3] == board[6] == 'X') |
		( board[0] == board[3] == board[6] == 'O') |
		( board[1] == board[4] == board[7] == 'X') |
		( board[1] == board[4] == board[7] == 'O') |
		( board[2] == board[5] == board[8] == 'X') |
		( board[2] == board[5] == board[8] == 'O') |
		( board[3] == board[4] == board[5] == 'X') |
		( board[3] == board[4] == board[5] == 'O') |
		( board[2] == board[6] == board[4] == 'X') |
		( board[2] == board[6] == board[4] == 'O') |
		( board[6] == board[7] == board[8] == 'X') |
		( board[6] == board[7] == board[8] == 'O')):
		return True
	else:
		return False

# Performs an action to the board marks an X to board the human input
def deploy(board, i):
	board[i] = 'X'

# Checks whether the player can make a valid move to the puzzle
# Checks the non conflicting states and returns the boolean
def isValid_move(board, position):
	valid = False
	if(board[position] == '-'):
		valid = True
		return valid
	else:
		return valid


# Minimax function
def Minimax_decision(board):
	v, con = Max_value(board)
	return v, con

# Calculates the Max Value
# This will take in the state and generate the successor and  return the max value for a particular successor
# This will go on till the leaf node is found and its utility is calculated. If leaf is not reached then
# it call the min function as that will be the move for opponent player.
def Max_value(board):
	if(goal_condition(board) == True):
		return Utility(board), board

	v = -10
	a = Successors(board, 'O')

	newboard = []
	maxVal = -2

	for i in a:
		v1, c1 = Min_value(i)
		if(maxVal < v1):
			maxVal = v1
			newboard = i

	return v, newboard

# Calculates the Min Value
# This will take in the state and generate the successor and  return the min value for a particular successor
# This will go on till the leaf node is found and its utility is calculated. If leaf is not reached then
# it call the max function as that will be the move for opponent player.

def Min_value(board):
	if(goal_condition(board) == True):
		return Utility(board), board

	v = 10
	a = Successors(board, 'X')
	newboard = []
	minVal = 2

	for j in a:
		v1, c1 = Max_value(j)
		if(minVal > v1):
			minVal = v1
			newboard = j

	return v, newboard

# Utility function returns
# -1 if human player wins,
# 1 if PC wins and
# 0 for a draw
def Utility(board):
	if ( ( board[0] == board[1] == board[2] == 'X') |
		 ( board[0] == board[4] == board[8] == 'X') |
		 ( board[0] == board[3] == board[6] == 'X') |
		 ( board[1] == board[4] == board[7] == 'X') |
		 ( board[2] == board[5] == board[8] == 'X') |
		 ( board[3] == board[4] == board[5] == 'X') |
		 ( board[2] == board[6] == board[4] == 'X') |
		 ( board[6] == board[7] == board[8] == 'X') ):
		return -1
	elif (( board[0] == board[1] == board[2] == 'O') |
		  ( board[0] == board[4] == board[8] == 'O') |
		  ( board[0] == board[3] == board[6] == 'O') |
		  ( board[1] == board[4] == board[7] == 'O') |
		  ( board[2] == board[5] == board[8] == 'O') |
		  ( board[3] == board[4] == board[5] == 'O') |
		  ( board[2] == board[6] == board[4] == 'O') |
		  ( board[6] == board[7] == board[8] == 'O') ):
		return 1
	else:
		return 0

# Create the successor nodes from the current configuration
def Successors(board,alpha):
	configs = []
	global count

	for i in range(0,9):
		dummy = []

		if( board[i] == '-' ):
			count = count + 1
			dummy = copy.deepcopy(board)
			dummy[i] = alpha
			configs.append(dummy)
	return configs

# AlphaBetaSearch performs the alpha beta pruning
# on min max algorithm and return the best position
def alpha_beta_search(board):
	#print board
	val, c = alpha_beta_max_value(board, -10, 10)
	return val, c

#The Alpha Beta Max Value
def alpha_beta_max_value(board, alpha, beta):

	if(goal_condition(board) == True):
		return Utility(board), board

	v = -10

	a = Successors(board, 'O')
	newboard = []

	for i in a:
		val, c = alpha_beta_min_value(i, alpha, beta)

		v = max( v, val)

		if( v > beta ):
			return v, board
		alpha = max( alpha, v )
		newboard = i
	return v, newboard

#The Alpha Beta Min Value
def alpha_beta_min_value(board,alpha,beta):
	if(goal_condition(board) == True):
		return Utility(board), board
	v = 10
	a = Successors(board, 'X')
	newboard = []
	for j in a:
		val, c = alpha_beta_max_value(j,alpha,beta)
		v = min( v, val)
		if(v < alpha):
			return v, board
		beta = min( beta, v )
		newboard = j
	return v, newboard

#The main function
def main():
	global count
	print("Tic Tac Toe Game")
	print("Human vs PC")

	board = ['-' for x in range(0, 9)]
	board2 = ['-' for x in range(0, 9)]
	print(" MiniMax")
	print(" Alpha Beta Pruning")

	print_board(board)

	while( goal_condition(board)!= True ):
		print("Human's Turn")
		var = int(input("Please Enter 0-8: "))

		if ( isValid_move(board,var) == True and isValid_move(board2,var) == True):
			i = board
			j = board2

			deploy(board,var)

			deploy(board2,var)
			print("Board 1")
			print_board(i)
			print("Board 2")
			print_board(j)
			a, i = Minimax_decision(i)
			print("MiniMax nodes", count)
			count = 0
			a, j = alpha_beta_search(j)
			print("Alpha Beta nodes", count)
			print("CPU plays")
			print("Board 1")
			print_board(i)
			print("Board 2")
			print_board(j)
			board = copy.deepcopy(i)
			board = copy.deepcopy(j)

main()
