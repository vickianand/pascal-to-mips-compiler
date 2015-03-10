import sys

#function to find whether a symbol is terminal or non-terminal or something else(kachra)
def symbol_type(s) :
	flag = 1
	for c in s:
		if c >= 'a' and c <= 'z' :
			flag = 0
		else:
			if not((c >= 'A' and c<= 'Z') or c == '_'):
				flag = 2
				break

	if flag == 1:
		return "terminal"
	elif flag == 0:
		return "non_terminal"
	else:
		# print "some kachra given to symbol_type() function!"
		return "kachra"	



node_names = {}

prod_file = open("productions.out", "w")
tree_file = open("parse_tree.dot", "w")

tree_file.write("digraph \"Parse Tree\" {\n")

with open("debug_parse.out", "r") as f:
	for line in reversed(f.readlines()):
		if line.find("Stack  : ") != -1 :
			stack_line = line

		if line.find("Action : ") != -1 :
			action_line = line

			# if action_line.find("Action : Shift and goto state ") != -1 :


			if action_line.find("Action : Reduce rule [") != -1 :
				production_rule = action_line.split("Action : Reduce rule [")[1].split("]")[0]
				prod_file.write( production_rule + "\n" )
				prod_lhs = production_rule.split(" -> ")[0]
				prod_rhs = production_rule.split(" -> ")[1]
				rhs_tokens = prod_rhs.split()
				# print prod_lhs
				# print prod_rhs
				# print rhs_tokens
				lhs_suffix = node_names.get(prod_lhs, 0)
				for rhs_token in rhs_tokens :
					if rhs_token == "<empty>" :
						rhs_token = "empty"
					rhs_suffix = node_names.get(rhs_token, 0) + 1
					node_names[rhs_token] = rhs_suffix
					tree_file.write( "\n\t"+prod_lhs+str(lhs_suffix)+" -> "+rhs_token+str(rhs_suffix) )

tree_file.write("\n\n}")

tree_file.close()
prod_file.close()