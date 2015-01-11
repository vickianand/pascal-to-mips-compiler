import ply.lex as lex

reserved = {
	'and' : 'AND',
	'array' : 'ARRAY',
	'begin' : 'BEGIN',
	'case' : 'CASE',
	'const' : 'CONST',
	'div' : 'DIV',
	'do' : 'DO',
	'downto' : 'DOWNTO',
	'else' : 'ELSE',
	'end' : 'END',
	'file' : 'FILE',
	'for' : 'FOR',
	'function' : 'FUNCTION',
	'goto' : 'GOTO',
	'if' : 'IF',
	'in' : 'IN',
	'label' : 'LABEL',
	'mod' : 'MOD',
	'nil' : 'NIL',
	'not' : 'NOT',
	'of' : 'OF',
	'or' : 'OR',
	'packed' : 'PACKED',
	'procedure' : 'PROCEDURE',
	'program' : 'PROGRAM',
	'record' : 'RECORD',
	'repeat' : 'REPEAT',
	'set' : 'SET',
	'then' : 'THEN',
	'to' : 'TO',
	'type' : 'TYPE',
	'until' : 'UNTIL',
	'var' : 'VAR',
	'while' : 'WHILE',
	'with' : 'WITH'
}



tokens = [
	#special symbols
	'PLUS',
	'MINUS',
	'TIMES',
	'DIVIDE',
	'COLON',
	'ASSIGNMENT',
	'DOT',
	'SEMI_COLON',
	'L_SQUARE_BRACKET',
	'R_SQUARE_BRACKET',
	'L_CURLY_BRACKET',
	'R_CURLY_BRACKET',
	'BACK_TICK',
	'COMMA',
	'LPAREN',
	'RPAREN',
	'LCOMMENT',
	'RCOMMENT',
	'LESS_THAN',
	'GREATER_THAN',
	'LESS_THAN_EQUAL',
	'GREATER_THAN_EQUAL',
	'IDENTIFIER',
	'NUMBER',
	'newline'
] + list(reserved.values())

t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_COLON = r'\:'
t_ASSIGNMENT = r'\='
t_DOT = r'\.'
t_SEMI_COLON = r'\;'
t_L_SQUARE_BRACKET = r'\['
t_R_SQUARE_BRACKET = r'\]'
t_L_CURLY_BRACKET = r'\{'
t_R_CURLY_BRACKET = r'\}'
t_BACK_TICK = r'`'
t_COMMA = r'\,'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LCOMMENT = r'\(\*'
t_RCOMMENT = r'\*\)'
t_LESS_THAN = r'<'
t_GREATER_THAN = r'>'
t_LESS_THAN_EQUAL = r'<='
t_GREATER_THAN_EQUAL = r'>='
t_NUMBER = r'[0-9]+'

def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,"IDENTIFIER")    # Check for reserved words
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    return t
# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Error handling rule
def t_error(t):
    print "Illegal character '%s'" % t.value[0]
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()
f = open('test.pas','r')
lexer.input(f.read())
output = ""
# Tokenize
while True:
    tok = lexer.token()
    if not tok: break      # No more input
    if (tok.type == 'newline'):
    	print output
    	output = ""
    else:
    	output += " " + tok.type
