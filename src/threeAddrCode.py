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

	def print_TAC(self):
		print self.code
		
		