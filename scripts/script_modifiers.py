f = open('modifiers.txt', 'r')
for x in f:
	y = 'modifier_'+x
	y = y.upper()
	z = '\'' + x.rstrip() + '\' : ' + '\'' + y.rstrip() + '\','
	print z