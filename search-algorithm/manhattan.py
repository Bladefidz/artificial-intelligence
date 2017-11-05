import sys
import itertools
import math

def getPoint(i, n):
	m = math.sqrt(n);
	return i % m, math.ceil(((n - i) / m) - 1)

def distance(p, q):
	'''
		Manhattan distance each point in p to q
	'''
	dist = 0
	n = len(q)
	m = math.sqrt(n)

	# Build dictionary for easier and faster lookup
	r = {}
	for i in range(n):
		r[q[i]] = i

	# Find only wrong placed tiles and calculate its distance to right place.
	for i in range(n):
		if p[i] != q[i]:
			# (x1, y1) is wrong position
			x1 = i % m
			y1 = math.ceil(((n - i) / m) - 1)

			# Index of right position
			j = r[p[i]]

			# (x2, y2) is right position
			x2 = j % m
			y2 = math.ceil(((n - j) / m) - 1)

			dist += abs(x2 - x1) + abs(y2 - y1)
	return dist

def inversionDistance(p, q):
	'''
		Manhattan distance each tile in p to tile point in q, except tile "zero"
	'''
	dist = 0
	n = len(q)
	m = math.sqrt(n)

	# Build dictionary for easier and faster lookup
	r = {}
	for i in range(n):
		r[q[i]] = i

	# Find only wrong placed tiles and calculate its distance to right place.
	for i in range(n):
		if p[i] != 0 and p[i] != q[i]:
			# (x1, y1) is wrong position
			x1 = i % m
			y1 = math.ceil(((n - i) / m) - 1)

			# Index of right position
			j = r[p[i]]

			# (x2, y2) is right position
			x2 = j % m
			y2 = math.ceil(((n - j) / m) - 1)

			dist += abs(x2 - x1) + abs(y2 - y1)
	return dist

def distPermutation(n):
	'''
		Print distance of all possible permutations.
	'''
	if n % math.sqrt(n) == 0.0:
		origin = list(range(0, n))
		for p in itertools.permutations(origin):
			print("{} -> {}".format(p, inversionDistance(p, origin)))
	else:
		print("Please insert board of N square.")

if __name__ == '__main__':
	if len(sys.argv) > 1:
		distPermutation(int(sys.argv[1]))
	else:
		print("Format: python manhattan.py <size_of_permutations>")