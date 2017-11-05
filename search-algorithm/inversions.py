import sys
import math
import itertools


def inversion(l):
	n = len(l)
	inv = 0
	for i in range(0, n):
		for j in range(i, n):
			if (l[i] > l[j]):
				inv += 1
	return inv

def invPermt(n):
	'''
		Print inversions of all possible permutations.
	'''
	for p in itertools.permutations(list(range(1, n + 1))):
		print("{} -> {}".format(p, inversion(p)))


if __name__ == '__main__':
	if len(sys.argv) == 2:
		invPermt(int(sys.argv[1]))
	elif (len(sys.argv) == 3 and sys.argv[1] == "-l"):
		print(inversion([int(k) for k in sys.argv[2].split(',')]))
	else:
		print("Format 1: python inversions.py <size_of_permutations>")
		print("Format 2: python inversions.py -l 1,2,3")