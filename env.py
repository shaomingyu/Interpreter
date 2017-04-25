class GlobalEnv:
	
	def __init__(self, prevenv):
		self.variables = []
		self.values = []
		self.prev = prevenv

	@staticmethod
	def empty_env():
		return GlobalEnv(None)

	def lookup(self, symbol):
		if symbol in self.variables:
			a = self.variables.index(symbol)
			return self.values[a]
		if (self.prev != None):
			return self.prev.lookup(symbol)
		return None
		

	def extend(self, variables, values):
		self.variables = variables
		self.values = values
		return GlobalEnv(self)

class LocalEnv:

	def __init__(self, prevenv, globalenvironment):
		self.variables = []
		self.values = []
		self.prev = prevenv
		self.globalenv = globalenvironment

	def lookup(self, symbol):
		if symbol in self.variables:
			a = self.variables.index(symbol)
			return self.values[a]
		if (self.prev != None):
			return self.prev.lookup(symbol)
		return self.globalenv.lookup(symbol)

	def extend(self, variables, values):
		self.variables = variables
		self.values = values
		return LocalEnv(self, self.globalenv)

if __name__ == '__main__':
    g = GlobalEnv.empty_env()
    g = g.extend(['a', 'b'], [1, 2])
    print(g.lookup('a'))
    l = g.extend(['x', 'y'], [3, 4])
    print(l.lookup('a'))
    print(l.lookup('b'))
    print(l.lookup('x'))
    print(l.lookup('y'))