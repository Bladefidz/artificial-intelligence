import sys
import itertools

def binomialHash(p, sigma, prime):
	h = 0
	for i in range(len(p)):
		h = p[i] + (sigma * h)
	# return h % prime
	return h

def nativeHash(p):
	en = ""
	for i in range(len(p)):
		en += str(p[i])
	return hash(en)

def testHash(n):
	origin = list(range(0, n))
	limit = 50000
	l = 0
	h = []
	for p in itertools.permutations(origin):
		# h.append(nativeHash(p))
		# print("{} -> {}".format(p, nativeHash(p)))
		h.append(binomialHash(p, len(p), 23))
		l += 1
		if l > limit:
			break
	h.sort()
	duplicate = 0
	for i in range(len(h) - 1):
		print(h[i])
		if h[i] == h[i+1]:
			duplicate += 1
	print("Duplicated = {}".format(duplicate))

if __name__ == '__main__':
	if len(sys.argv) > 1:
		testHash(int(sys.argv[1]))
	else:
		print("Format: python simple_hash.py <size_of_permutations>")