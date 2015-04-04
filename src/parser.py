import ply.yacc as yacc
from lexer import lexer, tokens
import symTab
import threeAddrCode


def temp_real(a) :
	if a['type'] == 'real':		# no need to type-convert : already a real
		return a['t_name']
	elif a['type'] == 'integer':
		temp_t = S_TABLE.new_temp(typ='integer',width=4)
		# set appropriate offset and width here
		TAC.emit(temp_t, a['t_name'], '', 'INT_TO_REAL')
		return temp_t
	elif a['type'] == 'char':
		temp_t = S_TABLE.new_temp(typ='char',width=1)
		# set appropriate offset and width here
		TAC.emit(temp_t, a['t_name'], '', 'CHAR_TO_REAL')
		return temp_t

	else :
		error_str = "type-conversion from "+a['type']+"-type to real-type not possible"
		throw_error(error_st)
	

def temp_integer(a) :
	if a['type'] == 'integer' :		# if already of integer-type then nothing to do
		return a['t_name']
	elif a['type'] == 'char':
		temp_t = S_TABLE.new_temp(typ='char',width=1)
		# set appropriate offset and width here
		TAC.emit(temp_t, a['t_name'], '', 'CHAR_TO_INT')
		return temp_t
	else :
		error_str = "type-conversion from "+a['type']+"-type to real-type not possible"
		throw_error(error_st)



def match_list(list1,list2):
	if (len(list1) != len(list2)):
		return False
	else:
		for i in range(len(list1)):
			if list1[i] != list2[i]:
				return False
	return True




def p_file_1(p):
	'file :  program'



def p_file_2(p):
	'file :  module'



def p_program_1(p):
	'program :  program_heading semicolon block DOT'



def p_program_heading_1(p):
	'program_heading :  RESERVED_PROGRAM identifier'

def p_program_heading_2(p):
	'program_heading :  RESERVED_PROGRAM identifier LPAREN identifier_list RPAREN'



def p_identifier_list_1(p):
	'identifier_list :  identifier_list comma identifier'
	p[0] = {}
	p[0]['list_id'] = p[1]['list_id'] + [p[3]['name']]

def p_identifier_list_2(p):
	'identifier_list :  identifier'
	p[0] = {}
	p[0]['list_id'] = [p[1]['name']]



def p_block_1(p):
	'block :  declaration_part_list statement_part'
	p[0] = {}
	if p[1]['type'] == 'ERROR' or p[2]['type'] == 'ERROR':
		p[0]['type'] = 'ERROR'
	else:
		p[0]['type'] = 'VOID'

def p_block_2(p):
	'block :  statement_part'
	p[0] = p[1]



def p_declaration_part_list_1(p):
	'declaration_part_list :  declaration_part_list declaration_entity'
	p[0] = {}
	if p[1]['type'] == 'ERROR' or p[2]['type'] == 'ERROR':
		p[0]['type'] = 'ERROR'
	else:
		p[0]['type'] = 'VOID'

def p_declaration_part_list_2(p):
	'declaration_part_list :  declaration_entity'
	p[0] = {}
	p[0]['type'] = p[1]['type']



def p_declaration_entity_1(p):
	'declaration_entity :  label_declaration_part'
	p[0] = {}
	p[0]['type'] = p[1]['type']

def p_declaration_entity_2(p):
	'declaration_entity :  constant_definition_part'
	p[0] = {}
	p[0]['type'] = p[1]['type']

def p_declaration_entity_3(p):
	'declaration_entity :  type_definition_part'
	p[0] = {}
	p[0]['type'] = p[1]['type']

def p_declaration_entity_4(p):
	'declaration_entity :  variable_declaration_part'
	p[0] = {}
	p[0]['type'] = p[1]['type']

def p_declaration_entity_5(p):
	'declaration_entity :  procedure_and_function_declaration_part'
	p[0] = {}
	p[0]['type'] = p[1]['type']



def p_module_1(p):
	'module :  module_declaration_part_list'



def p_module_declaration_part_list_1(p):
	'module_declaration_part_list :  module_declaration_part_list module_declaration_entity'

def p_module_declaration_part_list_2(p):
	'module_declaration_part_list :  module_declaration_entity'



def p_module_declaration_entity_1(p):
	'module_declaration_entity :  constant_definition_part'

def p_module_declaration_entity_2(p):
	'module_declaration_entity :  type_definition_part'

def p_module_declaration_entity_3(p):
	'module_declaration_entity :  variable_declaration_part'

def p_module_declaration_entity_4(p):
	'module_declaration_entity :  procedure_and_function_declaration_part'



def p_label_declaration_part_1(p):
	'label_declaration_part :  RESERVED_LABEL label_list semicolon'



def p_label_list_1(p):
	'label_list :  label_list comma label'

def p_label_list_2(p):
	'label_list :  label'



def p_label_1(p):
	'label :  DIGITSEQ'














def p_constant_definition_part_1(p):
	'constant_definition_part :  RESERVED_CONST constant_list'



def p_constant_list_1(p):
	'constant_list :  constant_list constant_definition'

def p_constant_list_2(p):
	'constant_list :  constant_definition'



def p_constant_definition_1(p):
	'constant_definition :  identifier EQ cexpression semicolon'



def p_cexpression_1(p):
	'cexpression :  csimple_expression'

def p_cexpression_2(p):
	'cexpression :  csimple_expression relop csimple_expression'



def p_csimple_expression_1(p):
	'csimple_expression :  cterm'

def p_csimple_expression_2(p):
	'csimple_expression :  csimple_expression addop cterm'



def p_cterm_1(p):
	'cterm :  cfactor'

def p_cterm_2(p):
	'cterm :  cterm mulop cfactor'



def p_cfactor_1(p):
	'cfactor :  sign cfactor'

def p_cfactor_2(p):
	'cfactor :  cexponentiation'



def p_cexponentiation_1(p):
	'cexponentiation :  cprimary'

def p_cexponentiation_2(p):
	'cexponentiation :  cprimary POWER cexponentiation'



def p_cprimary_1(p):
	'cprimary :  identifier'

def p_cprimary_2(p):
	'cprimary :  LPAREN cexpression RPAREN'

def p_cprimary_3(p):
	'cprimary :  unsigned_constant'

def p_cprimary_4(p):
	'cprimary :  RESERVED_NOT cprimary'



def p_constant_1(p):
	'constant :  non_string'
	p[0] = p[1]

def p_constant_2(p):
	'constant :  sign non_string'
	p[0] = p[1]
	if p[1]['name'] == '-' :
		p[0]['value'] = -1*p[0]['value']

# def p_constant_3(p):
# 	'constant :  STRING'



def p_sign_1(p):
	'sign :  PLUS'
	p[0] = {'name': p[1]}

def p_sign_2(p):
	'sign :  MINUS'
	p[0] = {'name' : p[1]}


def p_non_string_1(p):
	'non_string :  DIGITSEQ'
	p[0] = {'value':p[1],'type':'integer'}

# def p_non_string_2(p):
# 	'non_string :  identifier'































#TYpe definition and declaration part

def p_type_definition_part_1(p):
	'type_definition_part :  RESERVED_TYPE type_definition_list'


def p_type_definition_list_1(p):
	'type_definition_list :  type_definition_list type_definition'

def p_type_definition_list_2(p):
	'type_definition_list :  type_definition'



def p_type_definition_1(p):
	'type_definition :  identifier EQ type_denoter semicolon'




def p_type_denoter_1(p):
	'type_denoter :  identifier'	# integer, char, real, string
	p[0] = {}
	st_entry = S_TABLE.currentScope.look_up(name=p[1]['name'])
	if st_entry['type'] != 'typedef':
		throw_error("Type not defined")
	else:
		p[0]['type'] = p[1]['name']
		p[0]['width'] = st_entry['width']

def p_type_denoter_2(p):
	'type_denoter :  new_type'
	p[0] = p[1]
	



def p_new_type_1(p):
	'new_type :  new_ordinal_type'

def p_new_type_2(p):
	'new_type :  new_structured_type'
	p[0] = p[1]

def p_new_type_3(p):
	'new_type :  new_pointer_type'



# def p_new_ordinal_type_1(p):
# 	'new_ordinal_type :  enumerated_type'

def p_new_ordinal_type_2(p):
	'new_ordinal_type :  subrange_type'
	p[0] = p[1]



# def p_enumerated_type_1(p):
# 	'enumerated_type :  LPAREN identifier_list RPAREN'



def p_subrange_type_1(p):
	'subrange_type :  constant DOTDOT constant'
	p[0] = {}
	p[0]['range_begin'] = p[1]['value']
	p[0]['range_end'] = p[3]['value']



def p_new_structured_type_1(p):
	'new_structured_type :  structured_type'
	p[0] = p[1]
# def p_new_structured_type_2(p):
# 	'new_structured_type :  RESERVED_PACKED structured_type'



def p_structured_type_1(p):
	'structured_type :  array_type'
	p[0] = p[1]

# def p_structured_type_2(p):
# 	'structured_type :  record_type'

# def p_structured_type_3(p):
# 	'structured_type :  set_type'

# def p_structured_type_4(p):
# 	'structured_type :  file_type'



def p_array_type_1(p):
	'array_type :  RESERVED_ARRAY L_SQUARE_BRACKET index_list R_SQUARE_BRACKET RESERVED_OF component_type'
	p[0] = {}
	p[0]['dim'] = len(p[3]['list'])
	# p[0]['index_list'] = p[3]['list']
	p[0]['lowers']  = [i['range_begin'] for i in p[3]['list']]
	p[0]['lengths']  = [(i['range_end'] - i['range_begin']) for i in p[3]['list']]
	p[0]['base_type'] = p[6]['type']
	p[0]['type'] = 'array'
	p[0]['width'] = p[6]['width']
	for ranges in p[3]['list'] :
		p[0]['width'] *= (ranges['range_end'] - ranges['range_begin'])



def p_array_type_2(p):
	'array_type :  RESERVED_ARRAY RESERVED_OF component_type'
	p[0] = {}



def p_index_list_1(p):
	'index_list :  index_list comma index_type'
	p[0] = {}
	p[0]['list'] = p[1]['list'] + [p[3]]

def p_index_list_2(p):
	'index_list :  index_type'
	p[0] = {}
	p[0]['list'] = [p[1]]


def p_index_type_1(p):
	'index_type :  ordinal_type'
	p[0] = p[1]



def p_ordinal_type_1(p):
	'ordinal_type :  new_ordinal_type'
	p[0] = p[1]

# def p_ordinal_type_2(p):
# 	'ordinal_type :  identifier'



def p_component_type_1(p):
	'component_type :  identifier'
	p[0] = {}
	st_entry = S_TABLE.currentScope.look_up(name=p[1]['name'])
	if st_entry['type'] != 'typedef':
		throw_error("Type not defined")
	else:
		p[0]['type'] = p[1]['name']
		p[0]['width'] = st_entry['width']


# def p_record_type_1(p):
# 	'record_type :  RESERVED_RECORD record_section_list RESERVED_END'

# def p_record_type_2(p):
# 	'record_type :  RESERVED_RECORD record_section_list semicolon variant_part RESERVED_END'

# def p_record_type_3(p):
# 	'record_type :  RESERVED_RECORD variant_part RESERVED_END'



# def p_record_section_list_1(p):
# 	'record_section_list :  record_section_list semicolon record_section'

# def p_record_section_list_2(p):
# 	'record_section_list :  record_section'



# def p_record_section_1(p):
# 	'record_section :  identifier_list COLON type_denoter'



# def p_variant_part_1(p):
# 	'variant_part :  RESERVED_CASE variant_selector RESERVED_OF variant_list semicolon'

# def p_variant_part_2(p):
# 	'variant_part :  RESERVED_CASE variant_selector RESERVED_OF variant_list'

# def p_variant_part_3(p):
# 	'variant_part : '



# def p_variant_selector_1(p):
# 	'variant_selector :  tag_field COLON tag_type'

# def p_variant_selector_2(p):
# 	'variant_selector :  tag_type'



# def p_variant_list_1(p):
# 	'variant_list :  variant_list semicolon variant'

# def p_variant_list_2(p):
# 	'variant_list :  variant'



# def p_variant_1(p):
# 	'variant :  case_constant_list COLON LPAREN record_section_list RPAREN'

# def p_variant_2(p):
# 	'variant :  case_constant_list COLON LPAREN record_section_list semicolon  variant_part RPAREN'

# def p_variant_3(p):
# 	'variant :  case_constant_list COLON LPAREN variant_part RPAREN'



def p_case_constant_list_1(p):
	'case_constant_list :  case_constant_list comma case_constant'

def p_case_constant_list_2(p):
	'case_constant_list :  case_constant'



def p_case_constant_1(p):
	'case_constant :  constant'

def p_case_constant_2(p):
	'case_constant :  constant DOTDOT constant'



# def p_tag_field_1(p):
# 	'tag_field :  identifier'



# def p_tag_type_1(p):
# 	'tag_type :  identifier'



# def p_set_type_1(p):
# 	'set_type :  RESERVED_SET RESERVED_OF base_type'



# def p_base_type_1(p):
# 	'base_type :  ordinal_type'



# def p_file_type_1(p):
# 	'file_type :  RESERVED_FILE RESERVED_OF component_type'



def p_new_pointer_type_1(p):
	'new_pointer_type :  POINTER domain_type'



def p_domain_type_1(p):
	'domain_type :  identifier'


























def p_variable_declaration_part_1(p):
	'variable_declaration_part :  RESERVED_VAR variable_declaration_list semicolon'
	p[0] = {}
	p[0]['type'] = p[2]['type']



def p_variable_declaration_list_1(p):
	'variable_declaration_list :    variable_declaration_list semicolon variable_declaration'
	p[0] = {}
	if p[1]['type'] == 'ERROR' or p[3]['type'] == 'ERROR':
		p[0]['type'] = 'ERROR'
	else:
		p[0]['type'] = 'VOID'

def p_variable_declaration_list_2(p):
	'variable_declaration_list :  variable_declaration'
	p[0] = {}
	p[0]['type'] = p[1]['type']


def p_variable_declaration_1(p):
	'variable_declaration :  identifier_list COLON type_denoter'
	p[0] = {}
	for iden in p[1]['list_id']:
		st_entry = S_TABLE.currentScope.look_up(name=iden)
		if st_entry is not None:
			throw_error("Variable re-declaration")
			p[0]['type'] = 'ERROR'
		else:
			st_entry = S_TABLE.currentScope.add_id(name=iden)
			if(p[3]['type'] == 'array'):
				S_TABLE.currentScope.update_id(name=iden,id_dict={'type':p[3]['type'],'t_name':S_TABLE.new_temp(name=iden,typ='array',width=p[3]['width'],s_entry=st_entry)})
				S_TABLE.currentScope.update_id(name=iden,id_dict=p[3])
			else:
				S_TABLE.currentScope.update_id(name=iden,id_dict={'type':p[3]['type'],'t_name':S_TABLE.new_temp(name=iden,typ=p[3]['type'],width=p[3]['width'],s_entry=st_entry)})
			p[0]['type'] = 'VOID'


def p_procedure_and_function_declaration_part_1(p):
	'procedure_and_function_declaration_part :  procedure_declaration semicolon'
	p[0] = p[1]

def p_procedure_and_function_declaration_part_2(p):
	'procedure_and_function_declaration_part :  function_declaration semicolon'
	p[0] = p[1]



# def p_procedure_declaration_1(p):
# 	'procedure_declaration :  procedure_heading semicolon directive'
# 	p[0] = p[1]

def p_procedure_declaration_2(p):
	'procedure_declaration :  procedure_heading semicolon procedure_block'
	p[0] = p[1]
	S_TABLE.end_scope()



def p_procedure_heading_1(p):
	'procedure_heading :  procedure_identification'
	p[0] = p[1]

def p_procedure_heading_2(p):
	'procedure_heading :  procedure_identification formal_parameter_list'
	p[0] = {}
	if p[1]['type'] ==  'ERROR' or p[2]['type'] ==  'ERROR':
		p[0]['type'] = 'ERROR'
	else:
		p[0]['type'] = 'VOID'
		p[1]['p_st_entry']['type_list'] = p[2]['type_list']
		p[1]['p_st_entry']['param_width'] = p[2]['width']
		p[1]['p_st_entry']['label'] = S_TABLE.new_label()
		p[1]['p_st_entry']['arg_type_list'] = p[2]['arg_type_list']
		TAC.emit(p[1]['p_st_entry']['label'],'','','label')



# def p_directive_1(p):
# 	'directive :  RESERVED_FORWARD'

# def p_directive_2(p):
# 	'directive :  RESERVED_EXTERNAL'



def p_formal_parameter_list_1(p):
	'formal_parameter_list :  LPAREN formal_parameter_section_list RPAREN'
	p[0] = p[2]



def p_formal_parameter_section_list_1(p):
	'formal_parameter_section_list :  formal_parameter_section_list semicolon formal_parameter_section'
	p[0] = {}
	p[0]['type_list'] = p[1]['type_list'] + p[3]['type_list']
	p[0]['arg_type_list'] = p[1]['arg_type_list'] + p[3]['arg_type_list']
	p[0]['width'] = p[1]['width'] + p[3]['width']
	if p[1]['type'] ==  'ERROR' or p[3]['type'] ==  'ERROR':
		p[0]['type'] = 'ERROR'
	else:
		p[0]['type'] = 'VOID'

def p_formal_parameter_section_list_2(p):
	'formal_parameter_section_list :  formal_parameter_section'
	p[0] = p[1]


def p_formal_parameter_section_1(p):
	'formal_parameter_section :  value_parameter_specification'
	p[0] = p[1]

def p_formal_parameter_section_2(p):
	'formal_parameter_section :  variable_parameter_specification'
	p[0] = p[1]

def p_formal_parameter_section_3(p):
	'formal_parameter_section :  procedural_parameter_specification'
	p[0] = p[1]

def p_formal_parameter_section_4(p):
	'formal_parameter_section :  functional_parameter_specification'
	p[0] = p[1]



def p_value_parameter_specification_1(p):
	'value_parameter_specification :  identifier_list COLON identifier'
	p[0] = {}
	p[0]['type_list'] = []
	p[0]['arg_type_list'] = []
	p[0]['width'] = 0
	st_entry = S_TABLE.currentScope.look_up(name=p[3]['name'])

	if st_entry['type'] != 'typedef':
		throw_error("Type not defined - in value_parameter_specification")
		P[0]['type'] = 'ERROR'
		return
	else:
		p[0]['type'] = 'VOID'
		type_width = st_entry['width']
		for iden in p[1]['list_id']:
			st_entry = S_TABLE.currentScope.look_up(name=iden)
			if st_entry is not None:
				throw_error("Variable re-declaration")
				p[0]['type'] = 'ERROR'
			else:
				st_entry = S_TABLE.currentScope.add_id(name=iden)
				S_TABLE.currentScope.update_id(name=iden,id_dict={'type':p[3]['name'],'t_name':S_TABLE.new_temp(name=iden,typ=p[3]['name'],width=type_width,s_entry=st_entry)})
				p[0]['type_list'] = p[0]['type_list'] + [p[3]['name']]
				p[0]['arg_type_list'] = p[0]['arg_type_list'] + ['val']
				p[0]['type'] = 'VOID'
				p[0]['width'] += type_width



def p_variable_parameter_specification_1(p):
	'variable_parameter_specification :  RESERVED_VAR identifier_list COLON identifier'
	p[0] = {}
	p[0]['type_list'] = []
	p[0]['arg_type_list'] = []
	p[0]['width'] = 0
	st_entry = S_TABLE.currentScope.look_up(name=p[4]['name'])
	if st_entry['type'] != 'typedef':
		throw_error("Type not defined - in variable_parameter_specification")
	else:
		p[0]['type'] = 'VOID'
		type_width = st_entry['width']
		for iden in p[2]['list_id']:
			st_entry = S_TABLE.currentScope.look_up(name=iden)
			if st_entry is not None:
				throw_error("Variable re-declaration")
				p[0]['type'] = 'ERROR'
			else:
				st_entry = S_TABLE.currentScope.add_id(name=iden)
				S_TABLE.currentScope.update_id(name=iden,id_dict={'type':p[4]['name'],'t_name':S_TABLE.new_temp(name=iden,typ=p[4]['name'],width=type_width,s_entry=st_entry)})
				p[0]['type_list'] = p[0]['type_list'] + [p[4]['name']]
				p[0]['arg_type_list'] = p[0]['arg_type_list'] + ['var']
				p[0]['type'] = 'VOID'
				p[0]['width'] += type_width


def p_procedural_parameter_specification_1(p):
	'procedural_parameter_specification :  procedure_heading'



def p_functional_parameter_specification_1(p):
	'functional_parameter_specification :  function_heading'



def p_procedure_identification_1(p):
	'procedure_identification :  RESERVED_PROCEDURE identifier'
	p[0] = {}
	st_entry = S_TABLE.currentScope.look_up(name=p[2]['name'])
	if st_entry is not None:
		throw_error("Variable re-declaration")
		p[0]['type'] = 'ERROR'
	else :
		st_entry = S_TABLE.currentScope.add_id(name=p[2]['name'])
		S_TABLE.currentScope.update_id(name=p[2]['name'],id_dict={'type':'procedure','type_list':[],'arg_type_list':[],'t_name':S_TABLE.new_temp(name=p[2]['name'],width=0,typ='procedure'),'param_width':0})
		p[0]['type'] = 'VOID'
		p[0]['p_st_entry'] = st_entry
		S_TABLE.begin_scope(name=p[2]['name'])
		TAC.add_func(p[2]['name'])




def p_procedure_block_1(p):
	'procedure_block :  block'
	p[0] = p[1]



# def p_function_declaration_1(p):
# 	'function_declaration :  function_heading semicolon directive'
# 	TAC.emit('','','','FUNC_RETURN')
# 	S_TABLE.end_scope()

def p_function_declaration_2(p):
	'function_declaration :  function_identification semicolon function_block'
	TAC.emit('','','','FUNC_RETURN')
	S_TABLE.end_scope()
	if p[1]['type'] == p[1]['type'] == 'VOID' :
		p[0] = {'type' : 'VOID'}
	else :
		p[0] = {'type' : 'ERROR'}

def p_function_declaration_3(p):
	'function_declaration :  function_heading semicolon function_block'
	TAC.emit('','','','FUNC_RETURN')
	S_TABLE.end_scope()
	if p[1]['type'] == p[1]['type'] == 'VOID' :
		p[0] = {'type' : 'VOID'}
	else :
		p[0] = {'type' : 'ERROR'}



def p_function_heading_1(p):
	'function_heading :  RESERVED_FUNCTION identifier COLON result_type'
	p[0] = {}

	st_entry = S_TABLE.currentScope.look_up(name=p[2]['name'])
	if st_entry is not None:
		throw_error("Variable re-declaration")
		p[0]['type'] = 'ERROR'
	else:
		st_entry = S_TABLE.currentScope.add_id(name=p[2]['name'])
		p[0]['label'] = S_TABLE.new_label()
		S_TABLE.currentScope.update_id(name=p[2]['name'],id_dict={'type':'function','result_type':p[4]['type'],'label':p[0]['label'],'type_list':[],'arg_type_list':[],'t_name':S_TABLE.new_temp(name=p[2]['name'],width=0,s_entry=st_entry),'param_width':0})
		p[0]['type'] = 'VOID'
		S_TABLE.begin_scope(name=p[2]['name'])
		TAC.add_func(p[2]['name'])
		TAC.emit(p[0]['label'],'','','label')

def p_function_heading_2(p):
	'function_heading :  RESERVED_FUNCTION identifier marker_fh formal_parameter_list COLON result_type'
	p[0] = {}

	p[3]['f_st_entry']['result_type'] = p[6]['type']
	p[3]['f_st_entry']['type'] = 'function'
	p[0]['label'] = S_TABLE.new_label()
	p[3]['f_st_entry']['label'] = p[0]['label']
	p[3]['f_st_entry']['type_list'] = p[4]['type_list']
	p[3]['f_st_entry']['arg_type_list'] = p[4]['arg_type_list']
	p[3]['f_st_entry']['t_name'] = S_TABLE.new_temp(name=p[2]['name'],typ='function',s_entry=p[3]['f_st_entry'],width=0)
	p[3]['f_st_entry']['param_width'] = p[4]['width']
	TAC.emit(p[0]['label'],'','','label')
	if p[6]['type'] == 'ERROR' :
		p[0]['type'] = 'ERROR'
		return
	if p[3]['type'] == p[4]['type'] == 'VOID' :
		p[0]['type'] = 'VOID'
	else:
		p[0]['type'] = 'ERROR'


def p_marker_fh_1(p):
	'marker_fh :'
	p[0] = {}
	st_entry = S_TABLE.currentScope.look_up(name=p[-1]['name'])
	if st_entry is not None:
		throw_error("Variable re-declaration")
		p[0]['type'] = 'ERROR'
	else:
		st_entry = S_TABLE.currentScope.add_id(name=p[-1]['name'])
		p[0]['type'] = 'VOID'
		p[0]['f_st_entry'] = st_entry
		S_TABLE.begin_scope(name=p[-1]['name'])
		TAC.add_func(p[-1]['name'])


def p_result_type_1(p):
	'result_type :  identifier'
	p[0] = {}
	st_entry = S_TABLE.currentScope.look_up(name=p[1]['name'])
	if st_entry['type'] != 'typedef':
		throw_error("Type not defined")
		p[0]['type'] = 'ERROR'
	else:
		p[0]['type'] = p[1]['name']




def p_function_identification_1(p):
	'function_identification :  RESERVED_FUNCTION identifier'
	p[0] = {}

	st_entry = S_TABLE.currentScope.look_up(name=p[2]['name'])
	if st_entry is not None:
		throw_error("Variable re-declaration")
		p[0]['type'] = 'ERROR'
	else:
		st_entry = S_TABLE.currentScope.add_id(name=p[2]['name'])
		S_TABLE.currentScope.update_id(name=p[2]['name'],id_dict={'type':'function','result_type': 'VOID','type_list':[],'t_name':S_TABLE.new_temp(name=p[2]['name'],typ='function',s_entry=st_entry,width=0),'param_width':0})
		p[0]['type'] = 'VOID'
		S_TABLE.begin_scope(name=p[2]['name'])
		TAC.add_func(p[2]['name'])


def p_function_block_1(p):
	'function_block :  block'
	p[0] = p[1]



































def p_statement_part_1(p):
	'statement_part :  compound_statement'
	p[0] = {}
	p[0]['type'] = p[1]['type']


def p_compound_statement_1(p):
	'compound_statement :  RESERVED_BEGIN statement_sequence RESERVED_END'
	p[0] = {}
	p[0]['type'] = p[2]['type']


def p_statement_sequence_1(p):
	'statement_sequence :  statement_sequence semicolon statement'
	p[0] = {}
	if p[1]['type'] == 'ERROR' or p[3]['type'] == 'ERROR':
		p[0]['type'] = 'ERROR'
	else:
		p[0]['type'] = 'VOID'

def p_statement_sequence_2(p):
	'statement_sequence :  statement'
	p[0] = {}
	p[0]['type'] = p[1]['type']



def p_statement_1(p):
	'statement :  open_statement'
	p[0] = {}
	p[0]['type'] = p[1]['type']

def p_statement_2(p):
	'statement :  closed_statement'
	p[0] = {}
	p[0]['type'] = p[1]['type']



def p_open_statement_1(p):
	'open_statement :  label COLON non_labeled_open_statement'
	p[0] = {}
	p[0]['type'] = p[1]['type']

def p_open_statement_2(p):
	'open_statement :  non_labeled_open_statement'
	p[0] = {}
	p[0]['type'] = p[1]['type']



def p_closed_statement_1(p):
	'closed_statement :  label COLON non_labeled_closed_statement'
	p[0] = {}
	p[0]['type'] = p[1]['type']

def p_closed_statement_2(p):
	'closed_statement :  non_labeled_closed_statement'
	p[0] = {}
	p[0]['type'] = p[1]['type']



def p_non_labeled_closed_statement_1(p):
	'non_labeled_closed_statement :  assignment_statement'
	p[0] = {}
	p[0]['type'] = p[1]['type']

def p_non_labeled_closed_statement_2(p):
	'non_labeled_closed_statement :  procedure_statement'
	p[0] = {}
	p[0]['type'] = p[1]['type']

def p_non_labeled_closed_statement_3(p):
	'non_labeled_closed_statement :  goto_statement'
	p[0] = {}
	p[0]['type'] = p[1]['type']

def p_non_labeled_closed_statement_4(p):
	'non_labeled_closed_statement :  compound_statement'
	p[0] = {}
	p[0]['type'] = p[1]['type']

def p_non_labeled_closed_statement_5(p):
	'non_labeled_closed_statement :  case_statement'
	p[0] = {}
	p[0]['type'] = p[1]['type']

def p_non_labeled_closed_statement_6(p):
	'non_labeled_closed_statement :  repeat_statement'
	p[0] = {}
	p[0]['type'] = p[1]['type']

def p_non_labeled_closed_statement_7(p):
	'non_labeled_closed_statement :  closed_with_statement'
	p[0] = {}
	p[0]['type'] = p[1]['type']

def p_non_labeled_closed_statement_8(p):
	'non_labeled_closed_statement :  closed_if_statement'
	p[0] = {}
	p[0]['type'] = p[1]['type']

def p_non_labeled_closed_statement_9(p):
	'non_labeled_closed_statement :  closed_while_statement'
	p[0] = {}
	p[0]['type'] = p[1]['type']

def p_non_labeled_closed_statement_10(p):
	'non_labeled_closed_statement :  closed_for_statement'
	p[0] = {}
	p[0]['type'] = p[1]['type']

def p_non_labeled_closed_statement_11(p):
	'non_labeled_closed_statement : '
	p[0] = {}
	p[0]['type'] = 'VOID'


def p_non_labeled_open_statement_1(p):
	'non_labeled_open_statement :  open_with_statement'
	p[0] = {}
	p[0]['type'] = p[1]['type']

def p_non_labeled_open_statement_2(p):
	'non_labeled_open_statement :  open_if_statement'
	p[0] = {}
	p[0]['type'] = p[1]['type']

def p_non_labeled_open_statement_3(p):
	'non_labeled_open_statement :  open_while_statement'
	p[0] = {}
	p[0]['type'] = p[1]['type']

def p_non_labeled_open_statement_4(p):
	'non_labeled_open_statement :  open_for_statement'
	p[0] = {}
	p[0]['type'] = p[1]['type']



def p_repeat_statement_1(p):
	'repeat_statement :  RESERVED_REPEAT repeat_begin_marker statement_sequence RESERVED_UNTIL boolean_expression'
	TAC.emit(p[2]['repeat_begin'],p[5]['t_name'], '','IF_TRUE_GOTO')
	p[0] = {}
	if p[3]['type'] == 'ERROR' or p[5]['type'] == 'ERROR':
		p[0]['type'] = 'ERROR'
	else :
		p[0]['type'] = 'VOID'

def p_repeat_begin_marker_1(p):
	'repeat_begin_marker : '
	p[0] = {}
	p[0]['repeat_begin'] = S_TABLE.new_label()
	TAC.emit(p[0]['repeat_begin'],'','','label')

def p_open_while_statement_1(p):
	'open_while_statement :  RESERVED_WHILE boolean_expression marker_while RESERVED_DO open_statement'
	p[0] = {}
	if p[2]['type'] == 'ERROR' or p[5]['type'] == 'ERROR':
		p[0]['type'] = 'ERROR'
	else :
		p[0]['type'] = 'VOID'
	TAC.emit(p[2]['false'],'','','label')


def p_closed_while_statement_1(p):
	'closed_while_statement :  RESERVED_WHILE boolean_expression marker_while RESERVED_DO closed_statement'
	p[0] = {}
	if p[2]['type'] == 'ERROR' or p[5]['type'] == 'ERROR':
		p[0]['type'] = 'ERROR'
	else :
		p[0]['type'] = 'VOID'
	TAC.emit(p[2]['false'],'','','label')


def p_marker_while_1(p):
	'marker_while :'
	p[0] = {}
	TAC.emit(p[-1]['false'],p[-1]['t_name'],'','IF_FALSE_GOTO')

def p_open_for_statement_1(p):
	'open_for_statement :  RESERVED_FOR control_variable ASSIGNMENT initial_value direction final_value marker_for_for_branching RESERVED_DO open_statement'
	p[0] = {}
	if p[2]['type'] == p[4]['type'] == p[6]['type'] :
		if p[2]['type'].lower() == 'integer' :
			if p[8]['type'] == 'VOID' :
				p[0]['type'] = 'VOID'
				TAC.emit(p[2]['t_name'], p[2]['t_name'], 1,'int'+p[5]['control_op'])
				TAC.emit(p[7]['cond_chek_label'],'','','GOTO')
				TAC.emit(p[7]['for_end'],'','','label')
				return
		else :
			throw_error('control variables in for loop should be integer type')
	else:
		throw_error('type mismatch amongst control variables of for-loop')
	p[0]['type'] = 'ERROR'


def p_closed_for_statement_1(p):
	'closed_for_statement :  RESERVED_FOR control_variable ASSIGNMENT initial_value direction final_value marker_for_for_branching RESERVED_DO closed_statement'
	p[0] = {}
	if p[2]['type'] == p[4]['type'] == p[6]['type'] :
		if p[2]['type'].lower() == 'integer' :
			if p[9]['type'] == 'VOID' :
				p[0]['type'] = 'VOID'
				TAC.emit(p[2]['t_name'], p[2]['t_name'], 1,'int'+p[5]['control_op'])
				TAC.emit(p[7]['cond_chek_label'],'','','GOTO')
				TAC.emit(p[7]['for_end'],'','','label')
				return
		else :
			throw_error('control variables in for loop should be integer type')
	else:
		throw_error('type mismatch amongst control variables of for-loop')
	p[0]['type'] = 'ERROR'


def p_marker_for_for_branching_1(p):
	'marker_for_for_branching : '
	p[0] = {}
	TAC.emit(p[-5]['t_name'],p[-3]['t_name'],'',p[-4])
	p[0]['cond_chek_label'] = S_TABLE.new_label()
	TAC.emit(p[0]['cond_chek_label'],'','','label')
	p[0]['bool_temp'] = S_TABLE.new_temp(typ='integer')
	TAC.emit(p[0]['bool_temp'],p[-5]['t_name'],p[-1]['t_name'],p[-2]['relop'])
	p[0]['for_end'] = S_TABLE.new_label()
	TAC.emit(p[0]['for_end'],p[0]['bool_temp'],'','IF_FALSE_GOTO')


def p_open_with_statement_1(p):
	'open_with_statement :  RESERVED_WITH record_variable_list RESERVED_DO open_statement'



def p_closed_with_statement_1(p):
	'closed_with_statement :  RESERVED_WITH record_variable_list RESERVED_DO closed_statement'



def p_open_if_statement_1(p):
	'open_if_statement :  RESERVED_IF boolean_expression RESERVED_THEN marker_for_branching statement'
	p[0] = {}
	if p[2]['type'] == 'ERROR' or p[5]['type'] == 'ERROR':
		p[0]['type'] = 'ERROR'
	else :
		p[0]['type'] = 'VOID'
		TAC.emit(p[2]['false'],'','','label')

def p_open_if_statement_2(p):
	'open_if_statement :  RESERVED_IF boolean_expression RESERVED_THEN marker_for_branching closed_statement RESERVED_ELSE marker_if_false open_statement'
	p[0] = {}
	if p[2]['type'] == 'ERROR' or p[5]['type'] == 'ERROR' or p[8]['type'] == 'ERROR':
		p[0]['type'] = 'ERROR'
	else :
		p[0]['type'] = 'VOID'
		TAC.emit(p[7]['if_end'],'','','label')


def p_closed_if_statement_1(p):
	'closed_if_statement :  RESERVED_IF boolean_expression RESERVED_THEN marker_for_branching closed_statement RESERVED_ELSE marker_if_false closed_statement'
	p[0] = {}
	if p[2]['type'] == 'ERROR' or p[5]['type'] == 'ERROR' or p[8]['type'] == 'ERROR':
		p[0]['type'] = 'ERROR'
	else :
		p[0]['type'] = 'VOID'
		TAC.emit(p[7]['if_end'],'','','label')


def p_marker_if_false_1(p):
	'marker_if_false :'
	p[0] = {}
	p[0]['t_name'] = p[-5]['false']
	p[0]['if_end'] = S_TABLE.new_label()
	TAC.emit(p[0]['if_end'],'','','GOTO')
	TAC.emit(p[0]['t_name'],'','','label')

def p_marker_for_branching_1(p):
	'marker_for_branching :'
	p[0] = {}
	TAC.emit(p[-2]['false'],p[-2]['t_name'],'','IF_FALSE_GOTO')


def p_assignment_statement_1(p):
	'assignment_statement :  variable_access ASSIGNMENT expression'
	p[0] = {}
	# if(debugger):
	# 	print "DEBUGGING: at top of p_assignment_statement_1"
	# 	print "p_1_type: "+p[1]['type']
	# 	print "p_1_type: "+p[3]['type']
	if p[1]['type'] == 'function':
		p[1]['type'] = p[1]['result_type'] 
	if p[1]['type'] == 'ERROR' or p[3]['type'] == 'ERROR':
		p[0]['type'] = 'ERROR'
		return

	if (p[1]['type'] != p[3]['type']) :
		if p[1]['type'] == 'real' and p[3]['type'] == 'integer' :
			p[0]['type'] = 'VOID'
			TAC.emit(p[1]['t_name'],temp_real(p[3]),'',p[2])
		elif p[1]['type'] == 'integer' and p[3]['type'] == 'char' :
			p[0]['type'] = 'VOID'
			TAC.emit(p[1]['t_name'],temp_integer(p[3]),'',p[2])
		else :
			p[0]['type'] = 'ERROR'
			throw_error("type mis-match during assignment : conversion not possible")
	else:
		p[0]['type'] = 'VOID'
		TAC.emit(p[1]['t_name'],p[3]['t_name'],'',p[2])



def p_variable_access_1(p):
	'variable_access :  identifier'
	p[0] = {}
	st_entry = S_TABLE.currentScope.look_up(name=p[1]['name'])
	if st_entry is None:
		p[0]['type'] = 'ERROR'
		throw_error("Variable not declared")
	elif st_entry['type'] == 'function':
		p[0]['result_type'] = st_entry['result_type']
		p[0]['type'] = st_entry['type']
		p[0]['t_name'] = st_entry['t_name']
		# throw_error("Variable not declared")
	else:
		p[0]['type'] = st_entry['type']
		p[0]['t_name'] = st_entry['t_name']


def p_variable_access_2(p):
	'variable_access :  indexed_variable'
	p[0] = p[1]
# def p_variable_access_3(p):
# 	'variable_access :  field_designator'

def p_variable_access_4(p):
	'variable_access :  variable_access POINTER'



def p_indexed_variable_1(p):
	# 'indexed_variable :  variable_access L_SQUARE_BRACKET index_expression_list R_SQUARE_BRACKET'
	'indexed_variable :  identifier L_SQUARE_BRACKET index_expression_list R_SQUARE_BRACKET'
	p[0] = {}
	p[0]['type'] = 'VOID'
	st_entry = S_TABLE.currentScope.look_up(name=p[1]['name'])
	if st_entry is None:
		p[0]['type'] = 'ERROR'
		throw_error("Variable not declared")
	elif st_entry['type'] == 'array':
		if(len(p[3]['list']) != st_entry['dim']):
			p[0]['type'] = 'ERROR'
			throw_error("Illegal dimension of array accessed")
		else:
			for ind in p[3]['list']:
				if ind['type'] != 'integer':
					p[0]['type'] = 'ERROR'
					throw_error("Array index must be integer")
					break
			if p[0]['type'] != 'ERROR':
				offset_in_arr = S_TABLE.new_temp(typ='integer')
				z = S_TABLE.new_temp(typ='integer')
				TAC.emit(z,1,'',':=')
				TAC.emit(offset_in_arr,0,'',':=')
				y = S_TABLE.new_temp(typ='integer')
				for lower, length, index_val, in reversed(zip(st_entry['lowers'], st_entry['lengths'], p[3]['list']) ) :
					# offset_in_arr += z*(index_val - ranges['range_begin'])
					TAC.emit(y, index_val['t_name'],lower,'int-')
					TAC.emit(y,y,z,'int*')
					TAC.emit(offset_in_arr,offset_in_arr,y,'int+')
					TAC.emit(z,z,length,'int*')
			p[0]['t_name'] = S_TABLE.new_temp(typ='integer')
			TAC.emit(p[0]['t_name'],st_entry['t_name'],offset_in_arr,'ARRAY_MEM_ACCESS')
			p[0]['type'] = st_entry['base_type']
	else:
		p[0]['type'] = 'ERROR'
		throw_error("Variable not declared")



def p_index_expression_list_1(p):
	'index_expression_list :  index_expression_list comma index_expression'
	p[0] = {}
	p[0]['list'] = p[1]['list'] + [p[3]]

def p_index_expression_list_2(p):
	'index_expression_list :  index_expression'
	p[0] = {}
	p[0]['list'] = [p[1]]



def p_index_expression_1(p):
	'index_expression :  expression'
	p[0] = p[1]



# def p_field_designator_1(p):
# 	'field_designator :  variable_access DOT identifier'



def p_procedure_statement_1(p):
	'procedure_statement :  identifier params'
	st_entry = S_TABLE.currentScope.look_up(name = p[1]['name'])
	if(st_entry == None) :
		throw_error("procedure yet not defined")
		p[0] = {'type' : 'ERROR'}
	elif st_entry['type'] != 'procedure' :
		throw_error('this identifier cannot be used as a procedure ')
		p[0] = {'type' : 'ERROR'}
	else :
		p[0] = {'type' : 'VOID','t_name':S_TABLE.new_temp(name = p[1]['name'],width=0)}
		if match_list(p[2]['type_list'],st_entry['type_list']) :
			TAC.emit('',st_entry['param_width'],'','SET_PARAM_OFFSET_WIDTH')
			for i,params in enumerate(p[2]['list']):
				if(st_entry['arg_type_list'][i] == 'var'):
					TAC.emit(params['t_name'],'','','PUSH_VAR_PARAMS')
				else:
					TAC.emit(params['t_name'],'','','PUSH_VAL_PARAMS')
			TAC.emit(st_entry['label'],'','','CALL_PROCEDURE')

def p_procedure_statement_2(p):
	'procedure_statement :  identifier'
	p[0] = {}
	st_entry = S_TABLE.currentScope.look_up(name=p[1]['name'])
	st_entry = S_TABLE.currentScope.look_up(name = p[1]['name'])
	if(st_entry == None) :
		throw_error("procedure yet not defined")
		p[0] = {'type' : 'ERROR'}
	elif st_entry['type'] != 'procedure' :
		throw_error('this identifier cannot be used as a procedure ')
		p[0] = {'type' : 'ERROR'}
	else :
		p[0] = {'type' : 'VOID','t_name':S_TABLE.new_temp(name = p[1]['name'],width=0)}
		# if st_entry['type_list'] == []
		TAC.emit(st_entry['label'],'','','CALL_PROCEDURE')
		# else :
		# 	throw_error('parameter numbers of procedure not matching with definition of procedure')



def p_params_1(p):
	'params :  LPAREN actual_parameter_list RPAREN'
	p[0] = p[2]




def p_actual_parameter_list_1(p):
	'actual_parameter_list :  actual_parameter_list comma actual_parameter'
	p[0] = {}
	p[0]['list'] = p[1]['list'] + [p[3]]
	p[0]['type_list'] = p[1]['type_list'] + [p[3]['type']]
	if p[1]['type'] == 'ERROR' or p[3]['type'] == 'ERROR' :
		p[0]['type'] = 'ERROR'
	else :
		p[0]['type'] = 'VOID'


def p_actual_parameter_list_2(p):
	'actual_parameter_list :  actual_parameter'
	p[0] = {}
	p[0]['list'] = [p[1]]
	p[0]['type_list'] = [p[1]['type']]
	p[0]['type'] = p[1]['type']



def p_actual_parameter_1(p):
	'actual_parameter :  expression'
	p[0] = p[1]

def p_actual_parameter_2(p):
	'actual_parameter :  expression COLON expression'

def p_actual_parameter_3(p):
	'actual_parameter :  expression COLON expression COLON expression'



def p_goto_statement_1(p):
	'goto_statement :  RESERVED_GOTO label'



def p_case_statement_1(p):
	'case_statement :  RESERVED_CASE case_index RESERVED_OF case_list_element_list RESERVED_END'

def p_case_statement_2(p):
	'case_statement :  RESERVED_CASE case_index RESERVED_OF case_list_element_list SEMI_COLON RESERVED_END'

def p_case_statement_3(p):
	'case_statement :  RESERVED_CASE case_index RESERVED_OF case_list_element_list semicolon   otherwisepart statement RESERVED_END'

def p_case_statement_4(p):
	'case_statement :  RESERVED_CASE case_index RESERVED_OF case_list_element_list semicolon   otherwisepart statement SEMI_COLON RESERVED_END'



def p_case_index_1(p):
	'case_index :  expression'



def p_case_list_element_list_1(p):
	'case_list_element_list :  case_list_element_list semicolon case_list_element'

def p_case_list_element_list_2(p):
	'case_list_element_list :  case_list_element'



def p_case_list_element_1(p):
	'case_list_element :  case_constant_list COLON statement'



def p_otherwisepart_1(p):
	'otherwisepart :  RESERVED_OTHERWISE'

def p_otherwisepart_2(p):
	'otherwisepart :  RESERVED_OTHERWISE COLON'



def p_control_variable_1(p):
	'control_variable :  identifier'
	p[0] = {}
	st_entry = S_TABLE.currentScope.look_up(name = p[1]['name'])
	if st_entry == None:
		throw_error('control variable not declared')
		p[0]['type'] = 'ERROR'
		return
	else :
		p[0]['type'] = st_entry['type']
		p[0]['t_name'] = st_entry['t_name']

def p_initial_value_1(p):
	'initial_value :  expression'
	p[0] = p[1]


def p_direction_1(p):
	'direction :  RESERVED_TO'
	p[0] = {}
	p[0]['relop'] = '<='
	p[0]['control_op'] = '+'

def p_direction_2(p):
	'direction :  RESERVED_DOWNTO'
	p[0] = {}
	p[0]['relop'] = '>='
	p[0]['control_op'] = '-'



def p_final_value_1(p):
	'final_value :  expression'
	p[0] = p[1]



def p_record_variable_list_1(p):
	'record_variable_list :  record_variable_list comma variable_access'

def p_record_variable_list_2(p):
	'record_variable_list :  variable_access'



def p_boolean_expression_1(p):
	'boolean_expression :  expression'
	# if(debugger):
	# 	print "DEBUGGING: p_boolean_expression_1"
	# 	print "p_1_type : "+ p[1]['type']
	p[0] = {}
	if p[1]['type'] == 'ERROR':
		# throw_error("condition in 'if' is not boolean")
		p[0]['type'] == 'ERROR'
	else : 
		p[0] = p[1]
		p[0]['true'] = S_TABLE.new_label()
		p[0]['false'] = S_TABLE.new_label()


def p_expression_1(p):
	'expression :  simple_expression'
	p[0] = p[1]

def p_expression_2(p):
	'expression :  simple_expression relop simple_expression'
	p[0] = {}
	p[0]['t_name'] = S_TABLE.new_temp()
	# issue: I am not sure what all types are compatible with different types of operands
	if p[1]['type'] == 'string' or p[3]['type'] == 'string' :
		error_st = "string type cannot be used with "+p[3]['name']+" relational-operator"
		throw_error(error_st)
	elif p[1]['type'] == 'real' or p[3]['type'] == 'real' :
		TAC.emit(p[0]['t_name'],p[1]['t_name'],p[3]['t_name'],'real'+p[2]['name'])
	else :
		TAC.emit(p[0]['t_name'],p[1]['t_name'],p[3]['t_name'],'int'+p[2]['name'])
	p[0]['type'] = 'integer' 	# for us integer is boolean



def p_simple_expression_1(p):
	'simple_expression :  term'
	p[0] = p[1]

def p_simple_expression_2(p):
	'simple_expression :  simple_expression addop term' 
	p[0] = {}
	p[0]['t_name'] = S_TABLE.new_temp()
	if p[1]['type'] == 'string' or p[3]['type'] == 'string' :
		error_st = "string type cannot be used with "+p[3]['name']+" addop-operator"
		throw_error(error_st)
		return
	elif p[2]['name'] == 'or' or p[2]['name'] == 'xor' :	# if its safe to proceed and operator is 'OR' or 'XOR'
		p[0]['type'] = 'integer'	# then output type must be integer(boolean)
		TAC.emit(p[0]['t_name'],p[1]['t_name'],p[3]['t_name'],p[2]['name'])
	# for other operators we are going to type-cast it into the largest-sized data-type .
	elif p[1]['type'] == 'real' or p[3]['type'] == 'real' :
		p[0]['type'] = 'real'					# real is a larger data-type
		# TAC.emit(p[0]['t_name'], p[1]['t_name'], p[3]['t_name'], 'real'+p[2]['name'])
		TAC.emit(p[0]['t_name'], temp_real(p[1]), temp_real(p[3]), 'real'+p[2]['name'])	# temp_real function is used for handling type-conversion during assignment
	elif p[1]['type'] == 'integer' or p[3]['type'] == 'integer' :
		p[0]['type'] = 'integer'					# integer is a larger data-type
		# TAC.emit(p[0]['t_name'], p[1]['t_name'], p[3]['t_name'], 'int'+p[2]['name'])
		TAC.emit(p[0]['t_name'], temp_integer(p[1]), temp_integer(p[3]), 'int'+p[2]['name'])	# temp_integer function is used for handling type-conversion during assignment
	else :
		p[0]['type'] = 'char'					# char is only left data-type	
		TAC.emit(p[0]['t_name'],p[1]['t_name'],p[3]['t_name'],'char'+p[2]['name'])





def p_term_1(p):
	'term :  factor'
	p[0] = p[1]

def p_term_2(p):
	'term :  term mulop factor'
	p[0] = {}
	p[0]['t_name'] = S_TABLE.new_temp()
	if p[1]['type'] == 'string' or p[3]['type'] == 'string' :
		error_st = "string type cannot be used with "+p[3]['name']+" mulop-operator"
		throw_error(error_st)
		return
	elif p[2]['name'] == 'and' :	# if its safe to proceed and operator is 'AND'
		p[0]['type'] = 'integer'	# then output type must be integer(boolean)
		TAC.emit(p[0]['t_name'],p[1]['t_name'],p[3]['t_name'],p[2]['name'])
	# for other operators we are going to type-cast it into the largest-sized data-type .
	elif p[1]['type'] == 'real' or p[3]['type'] == 'real' :
		p[0]['type'] = 'real'					# real is a larger data-type
		# TAC.emit(p[0]['t_name'],p[1]['t_name'],p[3]['t_name'],'real'+p[2]['name'])
		TAC.emit(p[0]['t_name'], temp_real(p[1]), temp_real(p[3]), 'real'+p[2]['name'])	# temp_real function is used for handling type-conversion during assignment
	elif p[1]['type'] == 'integer' or p[3]['type'] == 'integer' :
		p[0]['type'] = 'integer'					# integer is a larger data-type
		# TAC.emit(p[0]['t_name'],p[1]['t_name'],p[3]['t_name'],'int'+p[2]['name'])
		TAC.emit(p[0]['t_name'], temp_integer(p[1]), temp_integer(p[3]), 'int'+p[2]['name'])	# temp_integer function is used for handling type-conversion during assignment
	else :
		p[0]['type'] = 'char'					# char is only left data-type	
		TAC.emit(p[0]['t_name'],p[1]['t_name'],p[3]['t_name'],'char'+p[2]['name'])





def p_factor_1(p):
	'factor :  sign factor'
	p[0] = {}
	p[0]['t_name'] = S_TABLE.new_temp()
	# p[0]['t_name'] = S_TABLE.new_temp()
	if p[2]['type'] == 'string' :
		throw_error('string type can\'t be used with unary operators')
		p[0]['type'] = 'ERROR'
	elif p[2]['type'] == 'char' :
		p[0]['type'] = 'integer'	# automatic type casting done
									# issue: how to change the width while type-casting
		TAC.emit(p[0]['t_name'],0,p[2]['t_name'],p[1]['name'])		# implementing unary operators by substracting it from 0
	else:
		p[0]['type'] = p[2]['type']
		TAC.emit(p[0]['t_name'],0,p[2]['t_name'],p[1]['name'])		# implementing unary operators by substracting it from 0
		

def p_factor_2(p):
	'factor :  exponentiation'
	p[0] = p[1]


def p_exponentiation_1(p):
	'exponentiation :  primary'
	p[0] = p[1]

def p_exponentiation_2(p):
	'exponentiation :  primary POWER exponentiation'
	p[0] = {}
	p[0]['t_name'] = S_TABLE.new_temp()
	if p[1]['type'] == 'string' or p[3]['type'] != 'integer' :
		throw_error('incompatible operand-types used with POWER(\'**\') operator')
		p[0]['type'] = 'ERROR'
	else :
		p[0]['type'] = p[1]['type']
		TAC.emit(p[0]['t_name'], p[1]['t_name'], p[3]['t_name'], 'POWER')



def p_primary_1(p):
	'primary :  variable_access'
	p[0] = p[1]

def p_primary_2(p):
	'primary :  unsigned_constant'
	p[0] = p[1]

def p_primary_3(p):
	'primary :  function_designator'
	p[0] = p[1]

# def p_primary_4(p):
# 	'primary :  set_constructor'
# 	p[0] = p[1]

def p_primary_5(p):
	'primary :  LPAREN expression RPAREN'	# if its bracketd, it surpasses all the precedence of operators
	p[0] = p[2]

def p_primary_6(p):
	'primary :  RESERVED_NOT primary'		# not has a very high precedence
	p[0] = {}
	p[0]['t_name'] = S_TABLE.new_temp(typ='integer')
	p[0]['type'] = 'integer'				# we are not keeping boolean type specifically. Integer type will do the job of boolean type
	TAC.emit(p[0]['t_name'], p[2]['t_name'], '', 'NOT')




def p_unsigned_constant_1(p):
	'unsigned_constant :  unsigned_number'
	p[0] = p[1]
	p[0]['t_name'] = S_TABLE.new_temp()
	TAC.emit(p[0]['t_name'],p[1]['value'],'',':=')

def p_unsigned_constant_2(p):
	'unsigned_constant :  STRING'
	p[0] = {'value':p[1],'type':'string'}
	p[0]['t_name'] = S_TABLE.new_temp()
	TAC.emit(p[0]['t_name'],p[1],'',':=')	# issue: how to get the exact string value ??

def p_unsigned_constant_3(p):
	'unsigned_constant :  RESERVED_NIL'
	p[0] = {'value':None,'type':'NIL'}
	p[0]['t_name'] = S_TABLE.new_temp()
	TAC.emit(p[0]['t_name'],p[1],'',':=')	# issue: how to handle the NIL type ??


def p_unsigned_number_1(p):
	'unsigned_number :  unsigned_integer'
	p[0] = p[1]

def p_unsigned_number_2(p):
	'unsigned_number :  unsigned_real'
	p[0] = p[1]


def p_unsigned_integer_1(p):
	'unsigned_integer :  DIGITSEQ'
	p[0] = {'value':p[1],'type':'integer'}


def p_unsigned_real_1(p):
	'unsigned_real :  REALNUMBER'
	p[0] = {'value':p[1],'type':'real'}



def p_function_designator_1(p):
	'function_designator :  identifier params'
	st_entry = S_TABLE.currentScope.look_up(name = p[1]['name'])
	if(st_entry == None) :
		throw_error("function yet not defined")
		p[0] = {'type' : 'ERROR'}
	elif st_entry['type'] != 'function' :
		throw_error('this identifier cannot be used as a function ')
		p[0] = {'type' : 'ERROR'}
	else :
		p[0] = {'type' : st_entry['result_type'],'t_name':S_TABLE.new_temp(name = p[1]['name'],width=0,typ='function',s_entry=st_entry)}
		if match_list(p[2]['type_list'],st_entry['type_list']):
			TAC.emit('',st_entry['param_width'],'','SET_PARAM_OFFSET_WIDTH')
			for params in p[2]['list']:
				TAC.emit(params['t_name'],'','','PARAMS')
			TAC.emit(st_entry['label'],'','','CALL_FUNCTION')



# def p_set_constructor_1(p):
# 	'set_constructor :  L_SQUARE_BRACKET member_designator_list R_SQUARE_BRACKET'

# def p_set_constructor_2(p):
# 	'set_constructor :  L_SQUARE_BRACKET R_SQUARE_BRACKET'



# def p_member_designator_list_1(p):
# 	'member_designator_list :  member_designator_list comma member_designator'

# def p_member_designator_list_2(p):
# 	'member_designator_list :  member_designator'



# def p_member_designator_1(p):
# 	'member_designator :  member_designator DOTDOT expression'

# def p_member_designator_2(p):
# 	'member_designator :  expression'



def p_addop_1(p):
	'addop :  PLUS'
	p[0] = {'name':p[1].lower()}

def p_addop_2(p):
	'addop :  MINUS'
	p[0] = {'name':p[1].lower()}

def p_addop_3(p):
	'addop :  RESERVED_OR'
	p[0] = {'name':p[1].lower()}

def p_addop_4(p):
	'addop :  RESERVED_XOR'
	p[0] = {'name':p[1].lower()}



def p_mulop_1(p):
	'mulop :  TIMES'
	p[0] = {'name':p[1].lower()}

def p_mulop_2(p):
	'mulop :  DIVIDE'
	p[0] = {'name':p[1].lower()}

def p_mulop_3(p):
	'mulop :  RESERVED_DIV'
	p[0] = {'name':p[1].lower()}

def p_mulop_4(p):
	'mulop :  RESERVED_MOD'
	p[0] = {'name':p[1].lower()}

def p_mulop_5(p):
	'mulop :  RESERVED_AND'
	p[0] = {'name':p[1].lower()}



def p_relop_1(p):
	'relop :  EQ'
	p[0] = {'name':p[1]}

def p_relop_2(p):
	'relop :  NE'
	p[0] = {'name':p[1]}

def p_relop_3(p):
	'relop :  LT'
	p[0] = {'name':p[1]}

def p_relop_4(p):
	'relop :  GT'
	p[0] = {'name':p[1]}

def p_relop_5(p):
	'relop :  LEQ'
	p[0] = {'name':p[1]}

def p_relop_6(p):
	'relop :  GEQ'
	p[0] = {'name':p[1]}

def p_relop_7(p):
	'relop :  RESERVED_IN'
	p[0] = {'name':p[1].lower()}


def p_identifier_1(p):
	'identifier :  IDENTIFIER'
	p[0] = {}
	p[0]['name'] = p[1].lower()

def p_identifier_2(p):
	'identifier :  RESERVED_EXIT'
	p[0] = {}
	p[0]['name'] = p[1].lower()
	# TAC.emit('','','','exit')

def p_identifier_3(p):
	'identifier :  RESERVED_STRING'
	p[0] = {}
	p[0]['name'] = p[1].lower()


def p_semicolon_1(p):
	'semicolon :  SEMI_COLON'



def p_comma_1(p):
	'comma :  COMMA'
	



def p_error(p):
	if p == None:
		print "ERROR: Token missing at the end of input"
		return
	else:
		print "ERROR: Unexpected token \""+str(p.value)+"\" at line no. " + str(p.lineno)
	while True:
		tok = yacc.token()
		if not tok or tok.type == 'SEMI_COLON': break
	yacc.errok()
	return tok

def throw_error(err):
	print "ERROR: "+err

parser = yacc.yacc()

def parseProgram(program):
    parser.parse(program, lexer=lexer)
    # return ST, TAC, debug

# a function to test the parser
def testYacc(inputFile):
    program = open(inputFile).read()
    parser.parse(program, lexer=lexer, debug=1)
    # parser.parse(program, lexer=lexer, debug=1)

if __name__ == "__main__":
    from sys import argv
    filename, inputFile = argv
    debugger = True
    S_TABLE = symTab.SymTable()
    TAC = threeAddrCode.ThreeAddrCode(S_TABLE)
    testYacc(inputFile)
    TAC.print_TAC()
    # S_TABLE.print_temp()
