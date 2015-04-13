class MIPS_Code(object):
	"""docstring for CodeGen"""
	def __init__(self, TAC, symTab):
		self.TAC = TAC
		self.symTab = symTab
		self.code = {}
		self.currFunc = ''
		self.register_descriptor = {
		'$t0' : None, 
		'$t1' : None, 
		'$t2' : None, 
		'$t3' : None, 
		'$t4' : None, 
		'$t5' : None, 
		'$t6' : None, 
		'$t7' : None, 
		'$t8' : None, 
		'$t9' : None, 
		'$s0' : None, 
		'$s1' : None, 
		'$s2' : None, 
		'$s3' : None, 
		'$s4' : None
		}
		self.free_regs = [register  for register in self.register_descriptor]
		self.busy_regs = []


	def add_line(self,line):
		self.code[self.currFunc] += [line]

	def new_func(self,f_name):
		self.code[f_name] = []
		self.currFunc = f_name

	def get_reg(self,temp,arg_num):
		reg = '$t'+str(arg_num)
		self.register_descriptor[reg] = temp
		curr_temp_details = self.symTab.scope_list[self.currFunc].tempList[temp]
		curr_temp_details['reg'] = reg
		self.add_line(['lw',reg, str(curr_temp_details['offset'])+'($sp)' ,''])
		return reg

	def flush_reg(self,reg):
		curr_temp_details = self.symTab.scope_list[self.currFunc].tempList[self.register_descriptor[reg]]
		self.add_line(['sw',reg,  str(curr_temp_details['offset'])+'($sp)' ,''])
		self.register_descriptor[reg] = None

	def print_code(self):
		print '.text'
		for func in self.symTab.scope_list:
			if func == 'root':
				print 'main:'
			for code in self.code[func]:
				print str(code[0]) + ' ' + str(code[1]) + ' ' + str(code[2]) + ' ' + str(code[3])
				# print code
			if func == 'root':
				print 'li $v0, 10'
				print 'syscall'






		