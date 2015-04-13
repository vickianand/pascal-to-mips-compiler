from MIPS_Code import *

def code_gen(TAC,symTab):
	M_Code = MIPS_Code(TAC,symTab)
	for f_name in TAC.code:
		M_Code.new_func(f_name)
		
		if f_name == 'root':
			#Add space to store the register's mapping
			M_Code.add_line(['sub', '$sp','$sp',120])
		else:
			M_Code.add_line(['sub', '$sp','$sp',4])
		
		for tac in TAC.code[f_name]:
			if tac[3] == ':=':
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

			elif tac[3] == '<':
				r1 = M_Code.get_reg(tac[0],1)
				r2 = M_Code.get_reg(tac[1],2)
				r3 = M_Code.get_reg(tac[2],3)
				M_Code.add_line(['slt',r1,r2,r3])
				M_Code.flush_reg(r1)

			elif tac[3] == '>':
				r1 = M_Code.get_reg(tac[0],1)
				r2 = M_Code.get_reg(tac[1],2)
				r3 = M_Code.get_reg(tac[2],3)
				M_Code.add_line(['slt',r1,r3,r2])
				M_Code.flush_reg(r1)

			elif tac[3] == '<=':
				r1 = M_Code.get_reg(tac[0],1)
				r2 = M_Code.get_reg(tac[1],2)
				r3 = M_Code.get_reg(tac[2],3)
				M_Code.add_line(['slt',r1,r3,r2])
				M_Code.add_line(['xori',r1,r1,1])
				M_Code.flush_reg(r1)

			elif tac[3] == '>=':
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

		M_Code.print_code()

		