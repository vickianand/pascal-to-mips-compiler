import ply.yacc as yacc
from lexer import lexer, tokens
import symTab
import threeAddrCode

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
	p[0]['list_id'] = p[1]['list_id'].append(p[3]['name'])

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

def p_constant_2(p):
	'constant :  sign non_string'

def p_constant_3(p):
	'constant :  STRING'



def p_sign_1(p):
	'sign :  PLUS'

def p_sign_2(p):
	'sign :  MINUS'



def p_non_string_1(p):
	'non_string :  DIGITSEQ'

def p_non_string_2(p):
	'non_string :  identifier'


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
	'type_denoter :  identifier'
	p[0] = {}
	st_entry = S_TABLE.currentScope.look_up(name=p[1]['name'])
	if st_entry['type'] != 'typedef':
		throw_error("Type not defined")
	else:
		p[0]['type'] = p[1]['name']

def p_type_denoter_2(p):
	'type_denoter :  new_type'



def p_new_type_1(p):
	'new_type :  new_ordinal_type'

def p_new_type_2(p):
	'new_type :  new_structured_type'

def p_new_type_3(p):
	'new_type :  new_pointer_type'



def p_new_ordinal_type_1(p):
	'new_ordinal_type :  enumerated_type'

def p_new_ordinal_type_2(p):
	'new_ordinal_type :  subrange_type'



def p_enumerated_type_1(p):
	'enumerated_type :  LPAREN identifier_list RPAREN'



def p_subrange_type_1(p):
	'subrange_type :  constant DOTDOT constant'



def p_new_structured_type_1(p):
	'new_structured_type :  structured_type'

def p_new_structured_type_2(p):
	'new_structured_type :  RESERVED_PACKED structured_type'



def p_structured_type_1(p):
	'structured_type :  array_type'

def p_structured_type_2(p):
	'structured_type :  record_type'

def p_structured_type_3(p):
	'structured_type :  set_type'

def p_structured_type_4(p):
	'structured_type :  file_type'



def p_array_type_1(p):
	'array_type :  RESERVED_ARRAY L_SQUARE_BRACKET index_list R_SQUARE_BRACKET RESERVED_OF component_type'

def p_array_type_2(p):
	'array_type :  RESERVED_ARRAY RESERVED_OF component_type'



def p_index_list_1(p):
	'index_list :  index_list comma index_type'

def p_index_list_2(p):
	'index_list :  index_type'



def p_index_type_1(p):
	'index_type :  ordinal_type'



def p_ordinal_type_1(p):
	'ordinal_type :  new_ordinal_type'

def p_ordinal_type_2(p):
	'ordinal_type :  identifier'



def p_component_type_1(p):
	'component_type :  type_denoter'



def p_record_type_1(p):
	'record_type :  RESERVED_RECORD record_section_list RESERVED_END'

def p_record_type_2(p):
	'record_type :  RESERVED_RECORD record_section_list semicolon variant_part RESERVED_END'

def p_record_type_3(p):
	'record_type :  RESERVED_RECORD variant_part RESERVED_END'



def p_record_section_list_1(p):
	'record_section_list :  record_section_list semicolon record_section'

def p_record_section_list_2(p):
	'record_section_list :  record_section'



def p_record_section_1(p):
	'record_section :  identifier_list COLON type_denoter'



def p_variant_part_1(p):
	'variant_part :  RESERVED_CASE variant_selector RESERVED_OF variant_list semicolon'

def p_variant_part_2(p):
	'variant_part :  RESERVED_CASE variant_selector RESERVED_OF variant_list'

def p_variant_part_3(p):
	'variant_part : '



def p_variant_selector_1(p):
	'variant_selector :  tag_field COLON tag_type'

def p_variant_selector_2(p):
	'variant_selector :  tag_type'



def p_variant_list_1(p):
	'variant_list :  variant_list semicolon variant'

def p_variant_list_2(p):
	'variant_list :  variant'



def p_variant_1(p):
	'variant :  case_constant_list COLON LPAREN record_section_list RPAREN'

def p_variant_2(p):
	'variant :  case_constant_list COLON LPAREN record_section_list semicolon  variant_part RPAREN'

def p_variant_3(p):
	'variant :  case_constant_list COLON LPAREN variant_part RPAREN'



def p_case_constant_list_1(p):
	'case_constant_list :  case_constant_list comma case_constant'

def p_case_constant_list_2(p):
	'case_constant_list :  case_constant'



def p_case_constant_1(p):
	'case_constant :  constant'

def p_case_constant_2(p):
	'case_constant :  constant DOTDOT constant'



def p_tag_field_1(p):
	'tag_field :  identifier'



def p_tag_type_1(p):
	'tag_type :  identifier'



def p_set_type_1(p):
	'set_type :  RESERVED_SET RESERVED_OF base_type'



def p_base_type_1(p):
	'base_type :  ordinal_type'



def p_file_type_1(p):
	'file_type :  RESERVED_FILE RESERVED_OF component_type'



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
			S_TABLE.currentScope.update_id(name=iden,id_dict={'type':p[3]['type'],'t_name':S_TABLE.new_temp()})
			p[0]['type'] = 'VOID'


def p_procedure_and_function_declaration_part_1(p):
	'procedure_and_function_declaration_part :  procedure_declaration semicolon'
	p[0] = p[1]

def p_procedure_and_function_declaration_part_2(p):
	'procedure_and_function_declaration_part :  function_declaration semicolon'
	p[0] = p[1]


def p_procedure_declaration_1(p):
	'procedure_declaration :  procedure_heading semicolon directive'
	p[0] = p[1]

def p_procedure_declaration_2(p):
	'procedure_declaration :  procedure_heading semicolon procedure_block'
	p[0] = p[1]



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



def p_directive_1(p):
	'directive :  RESERVED_FORWARD'

def p_directive_2(p):
	'directive :  RESERVED_EXTERNAL'



def p_formal_parameter_list_1(p):
	'formal_parameter_list :  LPAREN formal_parameter_section_list RPAREN'
	p[0] = p[2]



def p_formal_parameter_section_list_1(p):
	'formal_parameter_section_list :  formal_parameter_section_list semicolon formal_parameter_section'
	p[0] = {}
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
	st_entry = S_TABLE.currentScope.look_up(name=p[3]['name'])
	if st_entry['type'] != 'typedef':
		throw_error("Type not defined")
	else:
		p[0]['type'] = 'VOID'
	for iden in p[1]['list_id']:
		st_entry = S_TABLE.currentScope.look_up(name=iden)
		if st_entry is not None:
			throw_error("Variable re-declaration")
			p[0]['type'] = 'ERROR'
		else:
			st_entry = S_TABLE.currentScope.add_id(name=iden)
			S_TABLE.currentScope.update_id(name=iden,id_dict={'type':p[3]['name']})
			p[0]['type'] = 'VOID'



def p_variable_parameter_specification_1(p):
	'variable_parameter_specification :  RESERVED_VAR identifier_list COLON identifier'
	p[0] = {}
	st_entry = S_TABLE.currentScope.look_up(name=p[4]['name'])
	if st_entry['type'] != 'typedef':
		throw_error("Type not defined")
	else:
		p[0]['type'] = 'VOID'
	for iden in p[2]['list_id']:
		st_entry = S_TABLE.currentScope.look_up(name=iden)
		if st_entry is not None:
			throw_error("Variable re-declaration")
			p[0]['type'] = 'ERROR'
		else:
			st_entry = S_TABLE.currentScope.add_id(name=iden)
			S_TABLE.currentScope.update_id(name=iden,id_dict={'type':p[4]['name']})
			p[0]['type'] = 'VOID'


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
		S_TABLE.currentScope.update_id(name=p[2]['name'],id_dict={'type':'procedure'})
		p[0]['type'] = 'VOID'
		S_TABLE.begin_scope(name=p[2]['name'])




def p_procedure_block_1(p):
	'procedure_block :  block'



def p_function_declaration_1(p):
	'function_declaration :  function_heading semicolon directive'
	S_TABLE.end_scope()

def p_function_declaration_2(p):
	'function_declaration :  function_identification semicolon function_block'
	S_TABLE.end_scope()
	if p[1]['type'] == p[1]['type'] == 'VOID' :
		p[0] = {'type' : 'VOID'}
	else :
		p[0] = {'type' : 'ERROR'}

def p_function_declaration_3(p):
	'function_declaration :  function_heading semicolon function_block'
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
		S_TABLE.currentScope.update_id(name=p[2]['name'],id_dict={'type':'function','result_type':p[4]['type']})
		p[0]['type'] = 'VOID'
		S_TABLE.begin_scope(name=p[2]['name'])

def p_function_heading_2(p):
	'function_heading :  RESERVED_FUNCTION identifier marker_fh formal_parameter_list COLON result_type'
	p[0] = {}

	p[3]['f_st_entry']['result_type'] = p[6]['type']
	p[3]['f_st_entry']['type'] = 'function'

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
		S_TABLE.currentScope.update_id(name=p[2]['name'],id_dict={'type':'function','result_type': 'VOID'})
		p[0]['type'] = 'VOID'
		S_TABLE.begin_scope(name=p[2]['name'])


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
	'repeat_statement :  RESERVED_REPEAT statement_sequence RESERVED_UNTIL boolean_expression'



def p_open_while_statement_1(p):
	'open_while_statement :  RESERVED_WHILE boolean_expression RESERVED_DO open_statement'



def p_closed_while_statement_1(p):
	'closed_while_statement :  RESERVED_WHILE boolean_expression RESERVED_DO closed_statement'



def p_open_for_statement_1(p):
	'open_for_statement :  RESERVED_FOR control_variable ASSIGNMENT initial_value direction   final_value RESERVED_DO open_statement'
	p[0] = {}
	if p[2]['type'] == p[4]['type'] == p[6]['type'] :
		if p[2]['type'].lower() == 'integer' or p[2]['type'].lower() == 'longint' or p[2]['type'].lower() == 'shortint' :
			if p[8]['type'] == 'VOID' :
				p[0]['type'] = 'VOID'
				return
		else :
			throw_error('ERROR: control variables in for loop should be integer type')
	else:
		throw_error('type mismatch amongst control variables of for-loop')
	p[0]['type'] = 'ERROR'


def p_closed_for_statement_1(p):
	'closed_for_statement :  RESERVED_FOR control_variable ASSIGNMENT initial_value direction   final_value RESERVED_DO closed_statement'
	p[0] = {}
	if p[2]['type'] == p[4]['type'] == p[6]['type'] :
		if p[2]['type'].lower() == 'integer' or p[2]['type'].lower() == 'longint' or p[2]['type'].lower() == 'shortint' :
			if p[8]['type'] == 'VOID' :
				p[0]['type'] = 'VOID'
				return
		else :
			throw_error('ERROR: control variables in for loop should be integer type')
	else:
		throw_error('type mismatch amongst control variables of for-loop')
	p[0]['type'] = 'ERROR'

def p_open_with_statement_1(p):
	'open_with_statement :  RESERVED_WITH record_variable_list RESERVED_DO open_statement'



def p_closed_with_statement_1(p):
	'closed_with_statement :  RESERVED_WITH record_variable_list RESERVED_DO closed_statement'



def p_open_if_statement_1(p):
	'open_if_statement :  RESERVED_IF boolean_expression RESERVED_THEN marker_for_branching statement'
	p[0] = {}
	if p[2]['type'] == 'ERROR' or p[4]['type'] == 'ERROR':
		p[0]['type'] = 'ERROR'
	else :
		p[0]['type'] = 'VOID'

def p_open_if_statement_2(p):
	'open_if_statement :  RESERVED_IF boolean_expression RESERVED_THEN marker_for_branching closed_statement RESERVED_ELSE open_statement'
	p[0] = {}
	if p[2]['type'] == 'ERROR' or p[4]['type'] == 'ERROR' or p[6]['type'] == 'ERROR':
		p[0]['type'] = 'ERROR'
	else :
		p[0]['type'] = 'VOID'


def p_closed_if_statement_1(p):
	'closed_if_statement :  RESERVED_IF boolean_expression RESERVED_THEN marker_for_branching closed_statement RESERVED_ELSE marker_if_false_closed closed_statement'
	p[0] = {}
	if p[2]['type'] == 'ERROR' or p[5]['type'] == 'ERROR' or p[5]['type'] == 'ERROR':
		p[0]['type'] = 'ERROR'
	else :
		p[0]['type'] = 'VOID'
		TAC.emit(p[7]['if_end'],'','','label')


def p_marker_if_false_closed_1(p):
	'marker_if_false_closed :'
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
		p[0]['type'] = 'ERROR'
		throw_error("type error during assignment")
	else:
		p[0]['type'] = 'VOID'
		TAC.emit(p[1]['t_name'],p[3]['t_name'],'',p[2])



def p_variable_access_1(p):
	'variable_access :  identifier'
	p[0] = p[1]
	st_entry = S_TABLE.currentScope.look_up(name=p[1]['name'])
	if st_entry is None:
		p[0]['type'] = 'ERROR'
		throw_error("Variable not declared")
	elif st_entry['type'] == 'function':
		p[0]['result_type'] = st_entry['result_type']
		p[0]['type'] = st_entry['type']
		# throw_error("Variable not declared")
	else:
		p[0]['type'] = st_entry['type']
		p[0]['t_name'] = st_entry['t_name']


def p_variable_access_2(p):
	'variable_access :  indexed_variable'

def p_variable_access_3(p):
	'variable_access :  field_designator'

def p_variable_access_4(p):
	'variable_access :  variable_access POINTER'



def p_indexed_variable_1(p):
	'indexed_variable :  variable_access L_SQUARE_BRACKET index_expression_list R_SQUARE_BRACKET'



def p_index_expression_list_1(p):
	'index_expression_list :  index_expression_list comma index_expression'

def p_index_expression_list_2(p):
	'index_expression_list :  index_expression'



def p_index_expression_1(p):
	'index_expression :  expression'



def p_field_designator_1(p):
	'field_designator :  variable_access DOT identifier'



def p_procedure_statement_1(p):
	'procedure_statement :  identifier params'
	p[0] = {}
	st_entry = S_TABLE.currentScope.look_up(name=p[1]['name'])
	if st_entry == None:
		throw_error('undeclared function/procedure used')
		p[0]['type'] = 'ERROR'
		return
	elif st_entry['type'] != 'procedure':
		throw_error('this identifier cannot be used as a function or procedure')
		p[0]['type'] = 'ERROR'
		return
	else:
		p[1]['type'] = 'VOID'

	if p[1]['type'] == 'ERROR' or p[2]['type'] == 'ERROR':
		p[0]['type'] = 'ERROR'
	else :
		p[0]['type'] = 'VOID'

def p_procedure_statement_2(p):
	'procedure_statement :  identifier'



def p_params_1(p):
	'params :  LPAREN actual_parameter_list RPAREN'
	p[0] = p[2]




def p_actual_parameter_list_1(p):
	'actual_parameter_list :  actual_parameter_list comma actual_parameter'
	p[0] = {}
	p[0]['list'] = p[1]['list'].append(p[3])
	if p[1]['type'] == 'ERROR' or p[3]['type'] == 'ERROR' :
		p[0]['type'] = 'ERROR'
	else :
		p[0]['type'] = 'VOID'


def p_actual_parameter_list_2(p):
	'actual_parameter_list :  actual_parameter'
	p[0] = {}
	p[0]['list'] = [p[1]]
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

def p_direction_2(p):
	'direction :  RESERVED_DOWNTO'



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
	if p[1]['type'] != 'boolean' and p[1]['type'] != 'ERROR':
		throw_error("condition in 'if' is not boolean")
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
	# if(debugger):
	# 	print "DEBUGGING: p_expression_2"
	# 	print "p_1_type, p_3_type : "+p[1]['type']+"  "+p[3]['type']
	p[0] = {}
	if p[1]['type'] == 'integer' or p[1]['type'] == 'longint' or p[1]['type'] == 'boolean' or p[1]['type'] == 'real':
		if p[3]['type'] == 'integer' or p[3]['type'] == 'longint' or p[3]['type'] == 'boolean' or p[3]['type'] == 'real':
			p[0]['type'] = 'boolean'
			p[0]['t_name'] = S_TABLE.new_temp()
			TAC.emit(p[0]['t_name'],p[1]['t_name'],p[3]['t_name'],p[2]['name'])
			return
	p[0]['type'] = 'ERROR'
	throw_error('Invalid types comparison with relational operator')
	# if(debugger):
	# 	print "DEBUGGING: at the end of p_expression_2"
	# 	print "p_0_type : "+p[0]['type']




def p_simple_expression_1(p):
	'simple_expression :  term'
	p[0] = p[1]

def p_simple_expression_2(p):
	'simple_expression :  simple_expression addop term' 
	p[0] = {}
	if p[1]['type'] == 'integer' :
		if p[3]['type'] == 'real' or p[3]['type'] == 'integer':
			p[0]['type'] = p[3]['type']
			p[0]['t_name'] = S_TABLE.new_temp()
			TAC.emit(p[0]['t_name'],p[1]['t_name'],p[3]['t_name'],p[2]['name'])
		else:
			throw_error("type mismatch")
			p[0]['type'] = 'ERROR'
	elif p[1]['type'] == 'real':
		if p[3]['type'] == 'real' or p[3]['type'] == 'integer':
			p[0]['type'] = 'real'
			p[0]['t_name'] = S_TABLE.new_temp()
			TAC.emit(p[0]['t_name'],p[1]['t_name'],p[3]['t_name'],p[2]['name'])
		else:
			throw_error("type mismatch")
			p[0]['type'] = 'ERROR'
	else:
		throw_error("type mismatch")
		return







def p_term_1(p):
	'term :  factor'
	p[0] = p[1]

def p_term_2(p):
	'term :  term mulop factor'
	p[0] = {}
	if p[1]['type'] == 'integer' or p[1]['type'] == 'longint':
		if p[3]['type'] == 'real' or p[3]['type'] == 'integer' or p[3]['type'] == 'longint':
			p[0]['type'] = p[3]['type']
			p[0]['t_name'] = S_TABLE.new_temp()
			TAC.emit(p[0]['t_name'],p[1]['t_name'],p[3]['t_name'],p[2]['name'])
		else:
			throw_error("type mismatch between two operands of mulop")
			p[0]['type'] = 'ERROR'
	elif p[1]['type'] == 'real':
		if p[3]['type'] == 'real' or p[3]['type'] == 'integer' or p[3]['type'] == 'longint':
			p[0]['type'] = 'real'
			p[0]['t_name'] = S_TABLE.new_temp()
			TAC.emit(p[0]['t_name'],p[1]['t_name'],p[3]['t_name'],p[2]['name'])
		else:
			throw_error("type mismatch between two operands of mulop")
			p[0]['type'] = 'ERROR'
	else:
		throw_error("type mismatch between two operands of mulop")
		return




def p_factor_1(p):
	'factor :  sign factor'
	p[0] = p[2]
	p[0]['t_name'] = S_TABLE.new_temp()
	TAC.emit(p[0]['t_name'],p[2]['t_name'],'',p[1])

def p_factor_2(p):
	'factor :  exponentiation'
	p[0] = p[1]


def p_exponentiation_1(p):
	'exponentiation :  primary'
	p[0] = p[1]

def p_exponentiation_2(p):
	'exponentiation :  primary POWER exponentiation'




def p_primary_1(p):
	'primary :  variable_access'
	p[0] = p[1]

def p_primary_2(p):
	'primary :  unsigned_constant'
	p[0] = p[1]

def p_primary_3(p):
	'primary :  function_designator'
	p[0] = p[1]


def p_primary_4(p):
	'primary :  set_constructor'
	p[0] = p[1]

def p_primary_5(p):
	'primary :  LPAREN expression RPAREN'
	p[0] = p[2]

def p_primary_6(p):
	'primary :  RESERVED_NOT primary'



def p_unsigned_constant_1(p):
	'unsigned_constant :  unsigned_number'
	p[0] = p[1]
	p[0]['t_name'] = S_TABLE.new_temp()
	TAC.emit(p[0]['t_name'],p[1]['value'],'',':=')

def p_unsigned_constant_2(p):
	'unsigned_constant :  STRING'
	p[0] = {'value':p[1],'type':'STRING'}
	p[0]['t_name'] = S_TABLE.new_temp()
	TAC.emit(p[0]['t_name'],p[1]['value'],'',':=')

def p_unsigned_constant_3(p):
	'unsigned_constant :  RESERVED_NIL'
	p[0] = {'value':None,'type':'NIL'}
	p[0]['t_name'] = S_TABLE.new_temp()
	TAC.emit(p[0]['t_name'],p[1]['value'],'',':=')


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
		p[0] = {'type' : st_entry['result_type']}



def p_set_constructor_1(p):
	'set_constructor :  L_SQUARE_BRACKET member_designator_list R_SQUARE_BRACKET'

def p_set_constructor_2(p):
	'set_constructor :  L_SQUARE_BRACKET R_SQUARE_BRACKET'



def p_member_designator_list_1(p):
	'member_designator_list :  member_designator_list comma member_designator'

def p_member_designator_list_2(p):
	'member_designator_list :  member_designator'



def p_member_designator_1(p):
	'member_designator :  member_designator DOTDOT expression'

def p_member_designator_2(p):
	'member_designator :  expression'



def p_addop_1(p):
	'addop :  PLUS'
	p[0] = {'name':p[1]}

def p_addop_2(p):
	'addop :  MINUS'
	p[0] = {'name':p[1]}

def p_addop_3(p):
	'addop :  RESERVED_OR'
	p[0] = {'name':p[1]}

def p_addop_4(p):
	'addop :  RESERVED_XOR'
	p[0] = {'name':p[1]}



def p_mulop_1(p):
	'mulop :  TIMES'
	p[0] = {'name':p[1]}

def p_mulop_2(p):
	'mulop :  DIVIDE'
	p[0] = {'name':p[1]}

def p_mulop_3(p):
	'mulop :  RESERVED_DIV'
	p[0] = {'name':p[1]}

def p_mulop_4(p):
	'mulop :  RESERVED_MOD'
	p[0] = {'name':p[1]}

def p_mulop_5(p):
	'mulop :  RESERVED_AND'
	p[0] = {'name':p[1]}



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
	p[0] = {'name':p[1]}


def p_identifier_1(p):
	'identifier :  IDENTIFIER'
	p[0] = {}
	p[0]['name'] = p[1].lower()

def p_identifier_2(p):
	'identifier :  RESERVED_EXIT'
	p[0] = {}
	p[0]['name'] = p[1]
	# TAC.emit('','','','exit')

def p_identifier_3(p):
	'identifier :  RESERVED_STRING'
	p[0] = {}
	p[0]['name'] = p[1]


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
	print err

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
