import ply.yacc as yacc
from lexer import lexer, tokens



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

def p_identifier_list_2(p):
	'identifier_list :  identifier'



def p_block_1(p):
	'block :  label_declaration_part constant_definition_part type_definition_part variable_declaration_part procedure_and_function_declaration_part statement_part'



def p_module_1(p):
	'module :  constant_definition_part type_definition_part variable_declaration_part procedure_and_function_declaration_part'



def p_label_declaration_part_1(p):
	'label_declaration_part :  RESERVED_LABEL label_list semicolon'

def p_label_declaration_part_2(p):
	'label_declaration_part : '



def p_label_list_1(p):
	'label_list :  label_list comma label'

def p_label_list_2(p):
	'label_list :  label'



def p_label_1(p):
	'label :  DIGITSEQ'



def p_constant_definition_part_1(p):
	'constant_definition_part :  RESERVED_CONST constant_list'

def p_constant_definition_part_2(p):
	'constant_definition_part : '



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



def p_type_definition_part_1(p):
	'type_definition_part :  RESERVED_TYPE type_definition_list'

def p_type_definition_part_2(p):
	'type_definition_part : '



def p_type_definition_list_1(p):
	'type_definition_list :  type_definition_list type_definition'

def p_type_definition_list_2(p):
	'type_definition_list :  type_definition'



def p_type_definition_1(p):
	'type_definition :  identifier EQ type_denoter semicolon'



def p_type_denoter_1(p):
	'type_denoter :  identifier'

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

def p_variable_declaration_part_2(p):
	'variable_declaration_part : '



def p_variable_declaration_list_1(p):
	'variable_declaration_list :    variable_declaration_list semicolon variable_declaration'

def p_variable_declaration_list_2(p):
	'variable_declaration_list :  variable_declaration'



def p_variable_declaration_1(p):
	'variable_declaration :  identifier_list COLON type_denoter'



def p_procedure_and_function_declaration_part_1(p):
	'procedure_and_function_declaration_part :   proc_or_func_declaration_list semicolon'

def p_procedure_and_function_declaration_part_2(p):
	'procedure_and_function_declaration_part : '



def p_proc_or_func_declaration_list_1(p):
	'proc_or_func_declaration_list :    proc_or_func_declaration_list semicolon proc_or_func_declaration'

def p_proc_or_func_declaration_list_2(p):
	'proc_or_func_declaration_list :  proc_or_func_declaration'



def p_proc_or_func_declaration_1(p):
	'proc_or_func_declaration :  procedure_declaration'

def p_proc_or_func_declaration_2(p):
	'proc_or_func_declaration :  function_declaration'



def p_procedure_declaration_1(p):
	'procedure_declaration :  procedure_heading semicolon directive'

def p_procedure_declaration_2(p):
	'procedure_declaration :  procedure_heading semicolon procedure_block'



def p_procedure_heading_1(p):
	'procedure_heading :  procedure_identification'

def p_procedure_heading_2(p):
	'procedure_heading :  procedure_identification formal_parameter_list'



def p_directive_1(p):
	'directive :  RESERVED_FORWARD'

def p_directive_2(p):
	'directive :  RESERVED_EXTERNAL'



def p_formal_parameter_list_1(p):
	'formal_parameter_list :  LPAREN formal_parameter_section_list RPAREN'



def p_formal_parameter_section_list_1(p):
	'formal_parameter_section_list :  formal_parameter_section_list semicolon formal_parameter_section'

def p_formal_parameter_section_list_2(p):
	'formal_parameter_section_list :  formal_parameter_section'



def p_formal_parameter_section_1(p):
	'formal_parameter_section :  value_parameter_specification'

def p_formal_parameter_section_2(p):
	'formal_parameter_section :  variable_parameter_specification'

def p_formal_parameter_section_3(p):
	'formal_parameter_section :  procedural_parameter_specification'

def p_formal_parameter_section_4(p):
	'formal_parameter_section :  functional_parameter_specification'



def p_value_parameter_specification_1(p):
	'value_parameter_specification :  identifier_list COLON identifier'



def p_variable_parameter_specification_1(p):
	'variable_parameter_specification :  RESERVED_VAR identifier_list COLON identifier'



def p_procedural_parameter_specification_1(p):
	'procedural_parameter_specification :  procedure_heading'



def p_functional_parameter_specification_1(p):
	'functional_parameter_specification :  function_heading'



def p_procedure_identification_1(p):
	'procedure_identification :  RESERVED_PROCEDURE identifier'



def p_procedure_block_1(p):
	'procedure_block :  block'



def p_function_declaration_1(p):
	'function_declaration :  function_heading semicolon directive'

def p_function_declaration_2(p):
	'function_declaration :  function_identification semicolon function_block'

def p_function_declaration_3(p):
	'function_declaration :  function_heading semicolon function_block'



def p_function_heading_1(p):
	'function_heading :  RESERVED_FUNCTION identifier COLON result_type'

def p_function_heading_2(p):
	'function_heading :  RESERVED_FUNCTION identifier formal_parameter_list COLON result_type'



def p_result_type_1(p):
	'result_type :  identifier'



def p_function_identification_1(p):
	'function_identification :  RESERVED_FUNCTION identifier'



def p_function_block_1(p):
	'function_block :  block'



def p_statement_part_1(p):
	'statement_part :  compound_statement'



def p_compound_statement_1(p):
	'compound_statement :  RESERVED_BEGIN statement_sequence RESERVED_END'



def p_statement_sequence_1(p):
	'statement_sequence :  statement_sequence semicolon statement'

def p_statement_sequence_2(p):
	'statement_sequence :  statement'



def p_statement_1(p):
	'statement :  open_statement'

def p_statement_2(p):
	'statement :  closed_statement'



def p_open_statement_1(p):
	'open_statement :  label COLON non_labeled_open_statement'

def p_open_statement_2(p):
	'open_statement :  non_labeled_open_statement'



def p_closed_statement_1(p):
	'closed_statement :  label COLON non_labeled_closed_statement'

def p_closed_statement_2(p):
	'closed_statement :  non_labeled_closed_statement'



def p_non_labeled_closed_statement_1(p):
	'non_labeled_closed_statement :  assignment_statement'

def p_non_labeled_closed_statement_2(p):
	'non_labeled_closed_statement :  procedure_statement'

def p_non_labeled_closed_statement_3(p):
	'non_labeled_closed_statement :  goto_statement'

def p_non_labeled_closed_statement_4(p):
	'non_labeled_closed_statement :  compound_statement'

def p_non_labeled_closed_statement_5(p):
	'non_labeled_closed_statement :  case_statement'

def p_non_labeled_closed_statement_6(p):
	'non_labeled_closed_statement :  repeat_statement'

def p_non_labeled_closed_statement_7(p):
	'non_labeled_closed_statement :  closed_with_statement'

def p_non_labeled_closed_statement_8(p):
	'non_labeled_closed_statement :  closed_if_statement'

def p_non_labeled_closed_statement_9(p):
	'non_labeled_closed_statement :  closed_while_statement'

def p_non_labeled_closed_statement_10(p):
	'non_labeled_closed_statement :  closed_for_statement'

def p_non_labeled_closed_statement_11(p):
	'non_labeled_closed_statement :  exit_statement'

def p_non_labeled_closed_statement_12(p):
	'non_labeled_closed_statement : '



def p_non_labeled_open_statement_1(p):
	'non_labeled_open_statement :  open_with_statement'

def p_non_labeled_open_statement_2(p):
	'non_labeled_open_statement :  open_if_statement'

def p_non_labeled_open_statement_3(p):
	'non_labeled_open_statement :  open_while_statement'

def p_non_labeled_open_statement_4(p):
	'non_labeled_open_statement :  open_for_statement'



def p_repeat_statement_1(p):
	'repeat_statement :  RESERVED_REPEAT statement_sequence RESERVED_UNTIL boolean_expression'



def p_open_while_statement_1(p):
	'open_while_statement :  RESERVED_WHILE boolean_expression RESERVED_DO open_statement'



def p_closed_while_statement_1(p):
	'closed_while_statement :  RESERVED_WHILE boolean_expression RESERVED_DO closed_statement'



def p_open_for_statement_1(p):
	'open_for_statement :  RESERVED_FOR control_variable ASSIGNMENT initial_value direction   final_value RESERVED_DO open_statement'



def p_closed_for_statement_1(p):
	'closed_for_statement :  RESERVED_FOR control_variable ASSIGNMENT initial_value direction   final_value RESERVED_DO closed_statement'



def p_open_with_statement_1(p):
	'open_with_statement :  RESERVED_WITH record_variable_list RESERVED_DO open_statement'



def p_closed_with_statement_1(p):
	'closed_with_statement :  RESERVED_WITH record_variable_list RESERVED_DO closed_statement'



def p_open_if_statement_1(p):
	'open_if_statement :  RESERVED_IF boolean_expression RESERVED_THEN statement'

def p_open_if_statement_2(p):
	'open_if_statement :  RESERVED_IF boolean_expression RESERVED_THEN closed_statement RESERVED_ELSE open_statement'



def p_closed_if_statement_1(p):
	'closed_if_statement :  RESERVED_IF boolean_expression RESERVED_THEN closed_statement   RESERVED_ELSE closed_statement'



def p_assignment_statement_1(p):
	'assignment_statement :  variable_access ASSIGNMENT expression'


def p_exit_statement_1(p):
	'exit_statement : RESERVED_EXIT'

def p_variable_access_1(p):
	'variable_access :  identifier'

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

def p_procedure_statement_2(p):
	'procedure_statement :  identifier'



def p_params_1(p):
	'params :  LPAREN actual_parameter_list RPAREN'



def p_actual_parameter_list_1(p):
	'actual_parameter_list :  actual_parameter_list comma actual_parameter'

def p_actual_parameter_list_2(p):
	'actual_parameter_list :  actual_parameter'



def p_actual_parameter_1(p):
	'actual_parameter :  expression'

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



def p_initial_value_1(p):
	'initial_value :  expression'



def p_direction_1(p):
	'direction :  RESERVED_TO'

def p_direction_2(p):
	'direction :  RESERVED_DOWNTO'



def p_final_value_1(p):
	'final_value :  expression'



def p_record_variable_list_1(p):
	'record_variable_list :  record_variable_list comma variable_access'

def p_record_variable_list_2(p):
	'record_variable_list :  variable_access'



def p_boolean_expression_1(p):
	'boolean_expression :  expression'



def p_expression_1(p):
	'expression :  simple_expression'

def p_expression_2(p):
	'expression :  simple_expression relop simple_expression'



def p_simple_expression_1(p):
	'simple_expression :  term'

def p_simple_expression_2(p):
	'simple_expression :  simple_expression addop term'



def p_term_1(p):
	'term :  factor'

def p_term_2(p):
	'term :  term mulop factor'



def p_factor_1(p):
	'factor :  sign factor'

def p_factor_2(p):
	'factor :  exponentiation'



def p_exponentiation_1(p):
	'exponentiation :  primary'

def p_exponentiation_2(p):
	'exponentiation :  primary POWER exponentiation'



def p_primary_1(p):
	'primary :  variable_access'

def p_primary_2(p):
	'primary :  unsigned_constant'

def p_primary_3(p):
	'primary :  function_designator'

def p_primary_4(p):
	'primary :  set_constructor'

def p_primary_5(p):
	'primary :  LPAREN expression RPAREN'

def p_primary_6(p):
	'primary :  RESERVED_NOT primary'



def p_unsigned_constant_1(p):
	'unsigned_constant :  unsigned_number'

def p_unsigned_constant_2(p):
	'unsigned_constant :  STRING'

def p_unsigned_constant_3(p):
	'unsigned_constant :  RESERVED_NIL'



def p_unsigned_number_1(p):
	'unsigned_number :  unsigned_integer'

def p_unsigned_number_2(p):
	'unsigned_number :  unsigned_real'



def p_unsigned_integer_1(p):
	'unsigned_integer :  DIGITSEQ'



def p_unsigned_real_1(p):
	'unsigned_real :  REALNUMBER'



def p_function_designator_1(p):
	'function_designator :  identifier params'



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
	'addop : PLUS'

def p_addop_2(p):
	'addop : MINUS'

def p_addop_3(p):
	'addop : RESERVED_OR'

def p_addop_4(p):
	'addop : RESERVED_XOR'


def p_mulop_1(p):
	'mulop :  TIMES'

def p_mulop_2(p):
	'mulop :  DIVIDE'

def p_mulop_3(p):
	'mulop :  RESERVED_DIV'

def p_mulop_4(p):
	'mulop :  RESERVED_MOD'

def p_mulop_5(p):
	'mulop :  RESERVED_AND'



def p_relop_1(p):
	'relop :  EQ'

def p_relop_2(p):
	'relop :  NE'

def p_relop_3(p):
	'relop :  LT'

def p_relop_4(p):
	'relop :  GT'

def p_relop_5(p):
	'relop :  LEQ'

def p_relop_6(p):
	'relop :  GEQ'

def p_relop_7(p):
	'relop :  RESERVED_IN'



def p_identifier_1(p):
	'identifier :  IDENTIFIER'



def p_semicolon_1(p):
	'semicolon :  SEMI_COLON'



def p_comma_1(p):
	'comma :  COMMA'


def p_error(p):
	print "Unexpected token " + str(p.value) + " found."


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

    testYacc(inputFile)