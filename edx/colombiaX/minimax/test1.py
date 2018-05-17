class A(object):
	"""docstring for A"""
	@staticmethod
	def doThis(a):
		a = 3
		A.doThat(a)

	@staticmethod
	def doThat(a):
		print(a)

a = 2
A.doThis(a)
print(a)