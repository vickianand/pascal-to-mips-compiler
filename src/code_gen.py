from MIPS_Code import *

def code_gen(TAC,symTab):
	M_Code = MIPS_Code(TAC,symTab)
	# for key in TAC.code:
	# 	print key +" found."
	for f_name in TAC.code:
		# print f_name
		M_Code.new_func(f_name)
		# print f_name
		if f_name == 'root':
			#Add space to store the register's mapping
			M_Code.add_line(['sub', '$sp','$sp',120])
			M_Code.allocate_activation()
		# else:
		# 	M_Code.allocate_activation(f_name)
		
		for tac in TAC.code[f_name]:

			M_Code.annotate_code('generating code for : '+tac[3])
			# ******************** addops *************************
			if tac[3] == 'int:=' or tac[3] == 'integer:=':
				r1 = M_Code.get_reg(tac[0],1)
				if type(tac[1]) is str:
					r2 = M_Code.get_reg(tac[1],2)
					M_Code.add_line(['move',r1,r2,''])
				else:
					M_Code.add_line(['li',r1,tac[1],''])
				M_Code.flush_reg(r1)

			elif tac[3] == 'label':
				M_Code.add_line([tac[0], ':','',''])
			
			elif tac[3] == 'int+':
				r1 = M_Code.get_reg(tac[0],1)
				r2 = M_Code.get_reg(tac[1],2)
				if type(tac[2]) is int:
					M_Code.add_line(['addi',r1,r2,tac[2]])
				else:
					r3 = M_Code.get_reg(tac[2],3)
					M_Code.add_line(['add',r1,r2,r3])
				M_Code.flush_reg(r1)

			elif tac[3] == 'int-':
				r1 = M_Code.get_reg(tac[0],1)
				r2 = M_Code.get_reg(tac[1],2)
				if type(tac[2]) is int:
					M_Code.add_line(['sub',r1,r2,tac[2]])
				else:
					r3 = M_Code.get_reg(tac[2],3)
					M_Code.add_line(['sub',r1,r2,r3])
				M_Code.flush_reg(r1)


			elif tac[3] == 'real+':
				r1 = M_Code.get_f_reg(tac[0],1)
				r2 = M_Code.get_f_reg(tac[1],2)
				if type(tac[2]) is float:
					M_Code.add_line(['li.s', '$f30', tac[2]])	# don't use $f30 anywhere
					M_Code.add_line(['add.s',r1,r2,'$f30'])		# don't use $f30 anywhere
				else:
					r3 = M_Code.get_reg(tac[2],3)
					M_Code.add_line(['add.s',r1,r2,r3])
				M_Code.flush_reg(r1)

			elif tac[3] == 'real-':
				r1 = M_Code.get_f_reg(tac[0],1)
				r2 = M_Code.get_f_reg(tac[1],2)
				if type(tac[2]) is float:
					M_Code.add_line(['li.s', '$f30', tac[2]])	# don't use $f30 anywhere
					M_Code.add_line(['sub.s',r1,r2,'$f30'])		# don't use $f30 anywhere
				else:
					r3 = M_Code.get_f_reg(tac[2],3)
					M_Code.add_line(['sub.s',r1,r2,r3])
				M_Code.flush_f_reg(r1)


			# ******************** mulops *************************

			elif tac[3] == 'int*':
				r1 = M_Code.get_reg(tac[0],1)
				r2 = M_Code.get_reg(tac[1],2)
				if type(tac[2]) is int :
					M_Code.flush_reg('$s7')						# be careful!! using $7 forcibly.
					M_Code.add_line(['li', '$s7', tac[2], ''])	# be careful!! using $7 forcibly.
					r3 = '$s7'
				else :
					r3 = M_Code.get_reg(tac[2],3)
				M_Code.add_line(['mult', r2, r3, ''])
				M_Code.add_line(['mflo', r1, '', ''])
				M_Code.flush_reg(r1)



			# ******************** relops *************************

			elif tac[3] == 'int<':
				r1 = M_Code.get_reg(tac[0],1)
				r2 = M_Code.get_reg(tac[1],2)
				r3 = M_Code.get_reg(tac[2],3)
				M_Code.add_line(['slt',r1,r2,r3])
				M_Code.flush_reg(r1)

			elif tac[3] == 'int>':
				r1 = M_Code.get_reg(tac[0],1)
				r2 = M_Code.get_reg(tac[1],2)
				r3 = M_Code.get_reg(tac[2],3)
				M_Code.add_line(['slt',r1,r3,r2])
				M_Code.flush_reg(r1)

			elif tac[3] == 'int<=':
				r1 = M_Code.get_reg(tac[0],1)
				r2 = M_Code.get_reg(tac[1],2)
				r3 = M_Code.get_reg(tac[2],3)
				M_Code.add_line(['slt',r1,r3,r2])
				M_Code.add_line(['xori',r1,r1,1])
				M_Code.flush_reg(r1)

			elif tac[3] == 'real:=' :
				r1 = M_Code.get_f_reg(tac[0],1)
				if type(tac[1]) is str:
					r2 = M_Code.get_f_reg(tac[1],2)
					M_Code.add_line(['mov.s',r1,r2,''])
				else:
					M_Code.add_line(['li.s',r1,tac[1],''])
				M_Code.flush_f_reg(r1)

			elif tac[3] == 'int>=':
				r1 = M_Code.get_reg(tac[0],1)
				r2 = M_Code.get_reg(tac[1],2)
				r3 = M_Code.get_reg(tac[2],3)
				M_Code.add_line(['slt',r1,r2,r3])
				M_Code.add_line(['xori',r1,r1,1])
				M_Code.flush_reg(r1)

			elif tac[3] == 'IF_FALSE_GOTO':
				r1 = M_Code.get_reg(tac[1],1)
				M_Code.add_line(['beqz',r1,tac[0],''])

			elif tac[3] == 'GOTO':
				M_Code.add_line(['j', tac[0],'',''])



			elif tac[3] == 'WRITE_INT' :
				M_Code.add_line(['li', '$v0', '1', ''])
				M_Code.load_temp_in_reg(tac[1], '$a0')
				M_Code.add_line(['syscall', '', '', ''])

			elif tac[3] == 'READ_INT' :
				M_Code.add_line(['li', '$v0', '5', ''])
				M_Code.add_line(['syscall', '', '', ''])
				r1 = M_Code.get_reg(tac[1],1)
				r2 = '$v0'
				M_Code.add_line(['move',r1,r2,''])
				M_Code.flush_reg(r1)

			elif tac[3] == 'WRITE_REAL' :
				M_Code.add_line(['li', '$v0', '2', ''])
				M_Code.load_temp_in_f_reg(tac[1], '$f12')
				M_Code.add_line(['syscall', '', '', ''])

			elif tac[3] == 'READ_REAL' :
				M_Code.add_line(['li', '$v0', '6', ''])
				M_Code.add_line(['syscall', '', '', ''])
				r1 = M_Code.get_f_reg(tac[1],1)
				r2 = '$f0'
				M_Code.add_line(['mov.s',r1,r2,''])
				M_Code.flush_f_reg(r1)



			elif tac[3] == 'SET_PARAM_OFFSET_WIDTH':
				calee_name = tac[0]
				counter = 0
				tac_params = []
				tac_param_type = []
				width = tac[1]
				ret_temp = tac[2]

			elif tac[3] ==  'PUSH_VAR_PARAMS':
				counter += 1
				tac_param_type += ['var'] 
				tac_params += [tac[0]]

			elif tac[3] ==  'PUSH_VAL_PARAMS':
				tac_param_type += ['val'] 
				tac_params += [tac[0]]
				counter += 1

			elif tac[3] == 'CALL_FUNCTION':
				M_Code.function_caller_handler(calee_name,counter,tac_params,tac_param_type,width,tac[0],ret_temp)

			elif tac[3] == 'FUNC_RETURN':
				M_Code.function_return_handler(f_name)

			elif tac[3] == 'FUNC_BEGIN':
				M_Code.add_line(['sw','$ra','-8($fp)',''])

			else:
				print tac[3] + " not implemented"

			M_Code.annotate_code('===========================================')


	M_Code.print_code()

		