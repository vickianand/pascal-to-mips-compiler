#!/usr/bin/python

import sys
import ply.lex as lex
# We have to deal with five differen type of tokens which are there in pascal
# These are:	1) reserved words	words which have a fixed meaning in the language.
#				2) identifiers	programmer defined names of symbols. can be changed. subject to scope rules of language.
#				3) operators
# 				4) separators (whitespaces)
# 				5) constants (numerical, character, or string)

# The following characters have a special meaning:
# + - * / = < > [ ] . , ( ) : ^ @ { } $ # & %
# and the following character pairs too:
# << >> ** <> >< <= >= := += -= *= /= (* *) (. .) //


# We are considering only the Turbo Pascal reserved words not the Delphi ones

# Reserved words are part of the Pascal language, and as such, cannot be redefined by the programmer
reserved = {
	'absolute' : 'RESERVED_ABSOLUTE',
	'and' : 'RESERVED_AND',
	'array' : 'RESERVED_ARRAY',
	'asm' : 'RESERVED_ASM',
	'begin' : 'RESERVED_BEGIN',
	'case' : 'RESERVED_CASE',
	'const' : 'RESERVED_CONST',
	'constructor' : 'RESERVED_CONSTRUCTOR',
	'destructor' : 'RESERVED_DESTRUCTOR',
	'div' : 'RESERVED_DIV',
	'do' : 'RESERVED_DO',
	'downto' : 'RESERVED_DOWNTO',
	'else' : 'RESERVED_ELSE',
	'end' : 'RESERVED_END',
	'file' : 'RESERVED_FILE',
	'for' : 'RESERVED_FOR',
	'function' : 'RESERVED_FUNCTION',
	'goto' : 'RESERVED_GOTO',
	'if' : 'RESERVED_IF',
	'implementation' : 'RESERVED_IMPLEMENTATION',
	'in' : 'RESERVED_IN',
	'inherited' : 'RESERVED_INHERITED',
	'inline' : 'RESERVED_INLINE',
	'interface' : 'RESERVED_INTERFACE',
	'label' : 'RESERVED_LABEL',
	'mod' : 'RESERVED_MOD',
	'nil' : 'RESERVED_NIL',
	'not' : 'RESERVED_NOT',
	'object' : 'RESERVED_OBJECT',
	'of' : 'RESERVED_OF',
	'operator' : 'RESERVED_OPERATOR',
	'or' : 'RESERVED_OR',
	'packed' : 'RESERVED_PACKED',
	'procedure' : 'RESERVED_PROCEDURE',
	'program' : 'RESERVED_PROGRAM',
	'record' : 'RESERVED_RECORD',
	'reintroduce' : 'RESERVED_REINTRODUCE',
	'repeat' : 'RESERVED_REPEAT',
	'self' : 'RESERVED_SELF',
	'set' : 'RESERVED_SET',
	'shl' : 'RESERVED_SHL',
	'shr' : 'RESERVED_SHR',
	'string' : 'RESERVED_STRING',
	'then' : 'RESERVED_THEN',
	'to' : 'RESERVED_TO',
	'type' : 'RESERVED_TYPE',
	'unit' : 'RESERVED_UNIT',
	'until' : 'RESERVED_UNTIL',
	'uses' : 'RESERVED_USES',
	'var' : 'RESERVED_VAR',
	'while' : 'RESERVED_WHILE',
	'with' : 'RESERVED_WITH',
	'xor' : 'RESERVED_XOR',
	# following are not part of turbo pascal resrved words but included in free pascal
	'dispose' : 'RESERVED_DISPOSE',
	'exit' : 'RESERVED_EXIT',
	'false' : 'RESERVED_FALSE',
	'new' : 'RESERVED_NEW',
	'true' : 'RESERVED_TRUE'

}

# The following is a list of all modifiers. They are not exactly reserved words in the sense that they can
# be used as identifiers, but in specific places, they have a special meaning for the compiler, i.e., the
# compiler considers them as part of the Pascal language.
modifiers = {
	'abstract' : 'MODIFIER_ABSTRACT',
	'alias' : 'MODIFIER_ALIAS',
	'assembler' : 'MODIFIER_ASSEMBLER',
	'bitpacked' : 'MODIFIER_BITPACKED',
	'break' : 'MODIFIER_BREAK',
	'cdecl' : 'MODIFIER_CDECL',
	'continue' : 'MODIFIER_CONTINUE',
	'cppdecl' : 'MODIFIER_CPPDECL',
	'cvar' : 'MODIFIER_CVAR',
	'default' : 'MODIFIER_DEFAULT',
	'deprecated' : 'MODIFIER_DEPRECATED',
	'dynamic' : 'MODIFIER_DYNAMIC',
	'enumerator' : 'MODIFIER_ENUMERATOR',
	'experimental' : 'MODIFIER_EXPERIMENTAL',
	'export' : 'MODIFIER_EXPORT',
	'external' : 'MODIFIER_EXTERNAL',
	'far' : 'MODIFIER_FAR',
	'far16' : 'MODIFIER_FAR16',
	'forward' : 'MODIFIER_FORWARD',
	'generic' : 'MODIFIER_GENERIC',
	'helper' : 'MODIFIER_HELPER',
	'implements' : 'MODIFIER_IMPLEMENTS',
	'index' : 'MODIFIER_INDEX',
	'interrupt' : 'MODIFIER_INTERRUPT',
	'iochecks' : 'MODIFIER_IOCHECKS',
	'local' : 'MODIFIER_LOCAL',
	'message' : 'MODIFIER_MESSAGE',
	'name' : 'MODIFIER_NAME',
	'near' : 'MODIFIER_NEAR',
	'nodefault' : 'MODIFIER_NODEFAULT',
	'noreturn' : 'MODIFIER_NORETURN',
	'nostackframe' : 'MODIFIER_NOSTACKFRAME',
	'oldfpccall' : 'MODIFIER_OLDFPCCALL',
	'otherwise' : 'MODIFIER_OTHERWISE',
	'overload' : 'MODIFIER_OVERLOAD',
	'override' : 'MODIFIER_OVERRIDE',
	'pascal' : 'MODIFIER_PASCAL',
	'platform' : 'MODIFIER_PLATFORM',
	'private' : 'MODIFIER_PRIVATE',
	'protected' : 'MODIFIER_PROTECTED',
	'public' : 'MODIFIER_PUBLIC',
	'published' : 'MODIFIER_PUBLISHED',
	'read' : 'MODIFIER_READ',
	'register' : 'MODIFIER_REGISTER',
	'reintroduce' : 'MODIFIER_REINTRODUCE',
	'result' : 'MODIFIER_RESULT',
	'safecall' : 'MODIFIER_SAFECALL',
	'saveregisters' : 'MODIFIER_SAVEREGISTERS',
	'softfloat' : 'MODIFIER_SOFTFLOAT',
	'specialize' : 'MODIFIER_SPECIALIZE',
	'static' : 'MODIFIER_STATIC',
	'stdcall' : 'MODIFIER_STDCALL',
	'stored' : 'MODIFIER_STORED',
	'strict' : 'MODIFIER_STRICT',
	'unaligned' : 'MODIFIER_UNALIGNED',
	'unimplemented' : 'MODIFIER_UNIMPLEMENTED',
	'varargs' : 'MODIFIER_VARARGS',
	'virtual' : 'MODIFIER_VIRTUAL',
	'write' : 'MODIFIER_WRITE'
}


# Remark: Predefined types such as Byte, Boolean and constants such as maxint are not reserved words.
# 		They are identifiers, declared in the system unit. This means that these types can be redefined in
# 		other units. The programmer is however not encouraged to do this, as it will cause a lot of confusion.



tokens = [
	#OPERATORS
	'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'POWER',
	'LSHIFT', 'RSHIFT', #'LOR', 'LAND', 'LNOT',
    'LT', 'LEQ', 'GT', 'GEQ', 'EQ', 'NE', 'GT_NT',
	'POINTER', 'AT', 'DOLLAR', 'HASH', 'AMP', 'PERCENT',
	'PLUS_EQ', 'MINUS_EQ','TIMES_EQ','DIVIDE_EQ',
	'COLON',
	'ASSIGNMENT',
	'DOT',
	'DOTDOT',
	'SEMI_COLON',
	'L_SQUARE_BRACKET',
	'R_SQUARE_BRACKET',
	'L_CURLY_BRACKET',
	'R_CURLY_BRACKET',
	'BACK_TICK',
	'COMMA',
	'LPAREN',
	'RPAREN',
	# 'LCOMMENT',
	# 'RCOMMENT',
	'COMMENT',

	'IDENTIFIER',
	# 'B10_NUMBER',
	'BIN_NUMBER',
	'OCTAL_NUMBER',
	'HEXADECIMAL_NUMBER',
	# inserted later during resolving parser errors
	'DIGITSEQ',
	'REALNUMBER',

	'STRING'
	# 'newline'
] + list(reserved.values()) + list(modifiers.values())

t_PLUS = r'\+'
t_MINUS = r'\-'
t_TIMES = r'\*'
t_DIVIDE = r'\/'
t_POWER = r'\*\*'
t_LSHIFT = r'\<\<'
t_RSHIFT = r'\>\>'
t_LT = r'\<'
t_GT = r'\>'
t_LEQ = r'\<\='
t_GEQ = r'\>\='
t_EQ = r'\='
t_NE = r'\<\>'
t_GT_NT = r'\>\<'
t_POINTER = r'\^'
t_AT = r'\@'
t_DOLLAR = r'\$'
t_HASH = r'\#'
t_AMP = r'\&'
t_PERCENT =r'\%'
t_PLUS_EQ = r'\+\='
t_MINUS_EQ = r'\-\='
t_TIMES_EQ = r'\*\='
t_DIVIDE_EQ = r'\/\='
t_COLON = r'\:'
t_ASSIGNMENT = r'\:\='
t_DOT = r'\.'
t_DOTDOT = r'\.\.'
t_SEMI_COLON = r'\;'
t_L_SQUARE_BRACKET = r'\['
t_R_SQUARE_BRACKET = r'\]'
t_L_CURLY_BRACKET = r'\{'
t_R_CURLY_BRACKET = r'\}'
t_BACK_TICK = r'\`'
t_COMMA = r'\,'
t_LPAREN = r'\('
t_RPAREN = r'\)'
# t_LCOMMENT = r'(\(\*)'
# t_RCOMMENT = r'(\*\))'
# inserted later during resolving parser errors
t_DIGITSEQ = r'([0-9]+)'
# t_REALNUMBER = r'([0-9]+)(\.[0-9]+)([eE]([+-]|)[0-9]+|)'
# t_B10_NUMBER = r'([0-9]+)(\.[0-9]+|)([eE]([+-]|)[0-9]+|)'

def t_BIN_NUMBER(t):
	r'\%[01]*'
	t.value = int(t.value[1:],2)
	t.type = 'DIGITSEQ'
	return t

def t_OCTAL_NUMBER(t):
	r'\%[01]*'
	t.value = int(t.value[1:],8)
	t.type = 'DIGITSEQ'
	return t

def t_HEXADECIMAL_NUMBER(t):
	r'\%[01]*'
	t.value = int(t.value[1:],16)
	t.type = 'DIGITSEQ'
	return t

def t_REALNUMBER(t):
	r'([0-9]+)(\.[0-9]+|)([eE]([+-]|)[0-9]+|)'
	if '.' in t.value:
		t.value = float(t.value)
	else:
		t.type = 'DIGITSEQ'
		t.value = int(t.value)
	return t

# t_STRING = r'(\'.*?\')|\#(' + t_B10_NUMBER + '|' + t_BIN_NUMBER + '|' + t_OCTAL_NUMBER + '|' + t_HEXADECIMAL_NUMBER+')'
t_STRING = r'(\'.*?\')'#|\#(' + t_B10_NUMBER + '|' + t_BIN_NUMBER + '|' + t_OCTAL_NUMBER + '|' + t_HEXADECIMAL_NUMBER+')'
def t_COMMENT(t):
    r'(//.*)|(/\*)(.|\n)*\*/|\(\*(.|\n)*\*\)|{(.|\n)*}'
    # pass
    # No return value. Token discarded	

# Like Pascal reserved words, identifiers are case insensitive
def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value.lower(),"IDENTIFIER")    # Check for reserved words
    if t.type == 'IDENTIFIER':
    	t.type = modifiers.get(t.value,"IDENTIFIER")
    return t

output = ""
curr_line = ""

def t_newline(t):
	r'\n+'
	t.lexer.lineno += len(t.value)
	global output
	global curr_line
	# print  curr_line + '\t (* ' + output +' *)'
	output = ""
	curr_line = ""
    # return t
# A string containing ignored characters (spaces and tabs)

# t_ignore  = ' \t'
def t_indent(t):
	r'\ |\t'
	global output
	global curr_line
	curr_line += t.value


# Error handling rule
def t_error(t):
    print "Illegal character '%s'" % t.value[0]
    t.lexer.skip(1)

# Build the lexer
# lexer = lex.lex(debug = 1)
lexer = lex.lex()