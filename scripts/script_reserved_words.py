f = open('reserved_words.txt', 'r')
for x in f:
	y = 'reserved_'+x
	y = y.upper()
	z = '\'' + x.rstrip() + '\' : ' + '\'' + y.rstrip() + '\','
	print z