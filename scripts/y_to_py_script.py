print "import ply.yacc as yacc\nfrom lexer import lexer, tokens\n"

with open('pascal_latest.y', 'r') as f:
	data = f.read()

data = data.replace('\n', '')
data = data.replace('\r', '')
# print data
data = data.split(';')
#print 'length after split = ' + str(len(data))
# print data

for item in data:
	if len(item):
		#print item
		item = item.split(':')
		base_name = item[0];
		productions = item[1].split('|')
		for i, rhs in enumerate(productions):
			new_func = 'def p_' + base_name.rstrip() + '_' + str(i+1) + '(p):\n\t' + '\''+base_name+ ': ' + rhs.rstrip() + '\''
			print new_func + '\n'
		print '\n'
