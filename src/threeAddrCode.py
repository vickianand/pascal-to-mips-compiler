class ThreeAddrCode:
	def __init__(self,symbol_table):
		self.code = {'root' : []}
		self.quad = {'root' : -1}
		self.n_quad = {'root' : 0}
		self.ST = symbol_table

	def emit(self,dest,src1,src2,op):
		curr_func = self.ST.currentScope.name
		self.quad[curr_func] = self.n_quad[curr_func]
		self.n_quad[curr_func] += 1
		self.code[curr_func].append([dest,src1,src2,op])

	def add_func(self,func_name):
		self.code[func_name] = []
		self.quad[func_name] = -1
		self.n_quad[func_name] = 0

	def print_TAC(self):
		for t in self.code:
			print t
			for c in self.code[t]:
				print c
		
		