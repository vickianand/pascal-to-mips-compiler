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
		'$s4' : None,
		'$s5' : None, 
		'$s6' : None, 
		'$s7' : None
		}
		self.free_regs = [register  for register in self.register_descriptor]
		self.busy_regs = []


	def add_line(self,line):
		self.code[self.currFunc] += [line]

	def new_func(self,f_n):
		# print f_name + " added"
		self.code[f_n] = []
		self.currFunc = f_n

	def get_reg_array_access(self,temp,arg_num):
		reg = '$t'+str(arg_num)
		self.register_descriptor[reg] = temp
		curr_temp_details = self.symTab.scope_list[self.currFunc].tempList[temp]
		curr_temp_details['reg'] = reg
		self.add_line(['lw',reg, str(curr_temp_details['offset'])+'($sp)' ,''])
		return reg


	def get_reg(self,temp,arg_num):
		reg = '$t'+str(arg_num)
		self.register_descriptor[reg] = temp
		# print temp
		curr_temp_details = self.symTab.scope_list[self.currFunc].tempList[temp]
		curr_temp_details['reg'] = reg
		if curr_temp_details['array_access']:
			self.add_line(['lw','$t9', str(curr_temp_details['offset'])+'($sp)' ,''])
			self.add_line(['lw',reg,'0($t9)',''])
		else:
			self.add_line(['lw',reg, str(curr_temp_details['offset'])+'($sp)' ,''])
		return reg

	def get_f_reg(self,temp,arg_num):
		reg = '$f'+str(arg_num)
		self.register_descriptor[reg] = temp
		curr_temp_details = self.symTab.scope_list[self.currFunc].tempList[temp]
		curr_temp_details['reg'] = reg
		self.add_line(['l.s',reg, str(curr_temp_details['offset'])+'($sp)' ,''])
		return reg

	def get_reg_for_func_temp(self,temp,arg_num,func_name):
		reg = '$t'+str(arg_num)
		self.register_descriptor[reg] = temp
		# print temp
		curr_temp_details = self.symTab.scope_list[func_name].tempList[temp]
		curr_temp_details['reg'] = reg
		if curr_temp_details['array_access']:
			self.add_line(['lw',reg, str(curr_temp_details['offset'])+'($sp)' ,''])
			self.add_line(['lw',reg,'('+reg+')',''])
		else:
			self.add_line(['lw',reg, str(curr_temp_details['offset'])+'($sp)' ,''])
		return reg

	def get_addr_reg(self,temp,arg_num):
		reg = '$t'+str(arg_num)
		self.register_descriptor[reg] = temp
		curr_temp_details = self.symTab.scope_list[self.currFunc].tempList[temp]
		self.add_line(['addi',reg,'$sp',curr_temp_details['offset']])
		return reg

	def get_arg_reg(self,temp,arg_num):
		reg = '$t'+str(arg_num)
		self.register_descriptor[reg] = temp
		curr_temp_details = self.symTab.scope_list[self.currFunc].tempList[temp]
		curr_temp_details['reg'] = reg
		self.add_line(['lw',reg, str(curr_temp_details['offset'])+'($fp)' ,''])
		return reg

	def load_temp_in_reg(self, temp, reg) :
		self.register_descriptor[reg] = temp
		curr_temp_details = self.symTab.scope_list[self.currFunc].tempList[temp]
		curr_temp_details['reg'] = reg
		if curr_temp_details['array_access']:
			self.add_line(['lw',reg, str(curr_temp_details['offset'])+'($sp)' ,''])
			self.add_line(['lw',reg,'0('+reg+')',''])
		else:
			self.add_line(['lw',reg, str(curr_temp_details['offset'])+'($sp)' ,''])

	def load_temp_in_f_reg(self, temp, reg) :
		self.register_descriptor[reg] = temp
		curr_temp_details = self.symTab.scope_list[self.currFunc].tempList[temp]
		curr_temp_details['reg'] = reg
		self.add_line(['l.s',reg, str(curr_temp_details['offset'])+'($sp)' ,''])

	def flush_reg(self,reg):
		if self.register_descriptor[reg] is None:
			return
		curr_temp_details = self.symTab.scope_list[self.currFunc].tempList[self.register_descriptor[reg]]
		if curr_temp_details['array_access']:
			self.add_line(['lw','$t9', str(curr_temp_details['offset'])+'($sp)' ,''])
			self.add_line(['sw',reg,  '0($t9)' ,''])
		else:
			self.add_line(['sw',reg,  str(curr_temp_details['offset'])+'($sp)' ,''])
		self.register_descriptor[reg] = None

	def flush_reg_array_access(self,reg):
		if self.register_descriptor[reg] is None:
			return
		curr_temp_details = self.symTab.scope_list[self.currFunc].tempList[self.register_descriptor[reg]]
		self.add_line(['sw',reg,  str(curr_temp_details['offset'])+'($sp)' ,''])
		self.register_descriptor[reg] = None

	def flush_f_reg(self,reg):
		if self.register_descriptor[reg] is None:
			return
		curr_temp_details = self.symTab.scope_list[self.currFunc].tempList[self.register_descriptor[reg]]
		self.add_line(['s.s',reg,  str(curr_temp_details['offset'])+'($sp)' ,''])
		self.register_descriptor[reg] = None

	def flush_reg_func(self,reg,func_name):
		if self.register_descriptor[reg] is None:
			return
		curr_temp_details = self.symTab.scope_list[func_name].tempList[self.register_descriptor[reg]]
		self.add_line(['sw',reg,  str(curr_temp_details['offset'])+'($sp)' ,''])
		self.register_descriptor[reg] = None


	def allocate_activation(self):
		curr_func_details = self.symTab.scope_list[self.currFunc]
		self.add_line(['move','$fp','$sp',''])
		self.add_line(['sub','$sp',curr_func_details.width+32,''])

	def set_return_val_addr(self,func_name,ret_temp):
		curr_func_details = self.symTab.scope_list[func_name]
		ret_temp_details = curr_func_details.tempList[ret_temp]
		self.flush_reg('$t0')
		self.add_line(['addi','$t0','$fp',ret_temp_details['offset']])
		self.add_line(['sw','$t0','-12($fp)',''])

	def function_return_handler(self,func_name):
		curr_func_details = self.symTab.scope_list[func_name]
		curr_func_entry_list = self.symTab.get_func_entrylist(curr_func_details)
		self.flush_reg('$t1')
		r1 = self.get_reg(curr_func_entry_list['t_name'],1)
		self.flush_reg('$t0')
		self.add_line(['lw','$t0','-12($fp)',''])
		self.add_line(['sw',r1,'0($t0)',''])
		self.add_line(['lw','$ra','-8($fp)',''])
		self.add_line(['move','$sp','$fp',''])
		self.add_line(['lw','$fp','-4($sp)',''])
		self.add_line(['j','$ra','',''])
		


	def function_caller_handler(self,callee_name,counter,tac_params,tac_param_type,width,label,ret_temp):
		curr_func_details = self.symTab.scope_list[callee_name]
		self.add_line(['sw','$fp','-4($sp)',''])
		self.add_line(['move','$fp','$sp',''])
		self.add_line(['sub','$sp','$sp',curr_func_details.width+32])

		curr_func_st_entry = self.symTab.get_func_entrylist(curr_func_details)
		
		self.set_return_val_addr(self.currFunc,ret_temp)

		for i in range(counter):
			r1 = self.get_reg_for_func_temp(curr_func_st_entry['arg_temp_list'][i],1,callee_name)
			r2 = self.get_arg_reg(tac_params[i],2)
			self.add_line(['move',r1,r2,''])
			self.flush_reg_func(r1,callee_name)
		self.add_line(['jal',label,'',''])
			



	def annotate_code(self, str) :
		annotate = True
		if annotate :
			self.add_line(['#', str, '', ''])

	def print_code(self):
		print_str =  '.text'+'\n'
		for func in self.symTab.scope_list:
			if func == 'root':
				print_str += 'main:'+'\n'
			for code in self.code[func]:
				print_str += str(code[0]) + ' ' + str(code[1]) + ' ' + str(code[2]) + ' ' + str(code[3])+'\n'
				# print code
			if func == 'root':
				print_str += 'li $v0, 10'+'\n'
				print_str += 'syscall'+'\n'

		print print_str

		with open('temp.asm', 'w') as f:
			f.write(print_str)
		return	