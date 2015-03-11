
file : program
 | module
 ;

program : program_heading semicolon block DOT
 ;

program_heading : RESERVED_PROGRAM identifier
 | RESERVED_PROGRAM identifier LPAREN identifier_list RPAREN
 ;

identifier_list : identifier_list comma identifier
 | identifier
 ;

block : label_declaration_part
 constant_definition_part
 type_definition_part
 variable_declaration_part
 procedure_and_function_declaration_part
 statement_part
 ;

module : constant_definition_part
 type_definition_part
 variable_declaration_part
 procedure_and_function_declaration_part
 ;

label_declaration_part : RESERVED_LABEL label_list semicolon
 |
 ;

label_list : label_list comma label
 | label
 ;

label : DIGITSEQ
 ;

constant_definition_part : RESERVED_CONST constant_list
 |
 ;

constant_list : constant_list constant_definition
 | constant_definition
 ;

constant_definition : identifier EQ cexpression semicolon
 ;


cexpression : csimple_expression
 | csimple_expression relop csimple_expression
 ;

csimple_expression : cterm
 | csimple_expression addop cterm
 ;

cterm : cfactor
 | cterm mulop cfactor
 ;

cfactor : sign cfactor
 | cexponentiation
 ;

cexponentiation : cprimary
 | cprimary POWER cexponentiation
 ;

cprimary : identifier
 | LPAREN cexpression RPAREN
 | unsigned_constant
 | RESERVED_NOT cprimary
 ;

constant : non_string
 | sign non_string
 | STRING
 ;

sign : PLUS
 | MINUS
 ;

non_string : DIGITSEQ
 | identifier
 ;

type_definition_part : RESERVED_TYPE type_definition_list
 |
 ;

type_definition_list : type_definition_list type_definition
 | type_definition
 ;

type_definition : identifier EQ type_denoter semicolon
 ;

type_denoter : identifier
 | new_type
 ;

new_type : new_ordinal_type
 | new_structured_type
 | new_pointer_type
 ;

new_ordinal_type : enumerated_type
 | subrange_type
 ;

enumerated_type : LPAREN identifier_list RPAREN
 ;

subrange_type : constant DOTDOT constant
 ;

new_structured_type : structured_type
 | RESERVED_PACKED structured_type
 ;

structured_type : array_type
 | record_type
 | set_type
 | file_type
 ;

array_type : RESERVED_ARRAY L_SQUARE_BRACKET index_list R_SQUARE_BRACKET RESERVED_OF component_type
 ;

index_list : index_list comma index_type
 | index_type
 ;

index_type : ordinal_type ;

ordinal_type : new_ordinal_type
 | identifier
 ;

component_type : type_denoter ;

record_type : RESERVED_RECORD record_section_list RESERVED_END
 | RESERVED_RECORD record_section_list semicolon variant_part RESERVED_END
 | RESERVED_RECORD variant_part RESERVED_END
 ;

record_section_list : record_section_list semicolon record_section
 | record_section
 ;

record_section : identifier_list COLON type_denoter
 ;

variant_part : RESERVED_CASE variant_selector RESERVED_OF variant_list semicolon
 | RESERVED_CASE variant_selector RESERVED_OF variant_list
 |
 ;

variant_selector : tag_field COLON tag_type
 | tag_type
 ;

variant_list : variant_list semicolon variant
 | variant
 ;

variant : case_constant_list COLON LPAREN record_section_list RPAREN
 | case_constant_list COLON LPAREN record_section_list semicolon
  variant_part RPAREN
 | case_constant_list COLON LPAREN variant_part RPAREN
 ;

case_constant_list : case_constant_list comma case_constant
 | case_constant
 ;

case_constant : constant
 | constant DOTDOT constant
 ;

tag_field : identifier ;

tag_type : identifier ;

set_type : RESERVED_SET RESERVED_OF base_type
 ;

base_type : ordinal_type ;

file_type : RESERVED_FILE RESERVED_OF component_type
 ;

new_pointer_type : POINTER domain_type
 ;

domain_type : identifier ;

variable_declaration_part : RESERVED_VAR variable_declaration_list semicolon
 |
 ;

variable_declaration_list :
   variable_declaration_list semicolon variable_declaration
 | variable_declaration
 ;

variable_declaration : identifier_list COLON type_denoter
 ;

procedure_and_function_declaration_part :
  proc_or_func_declaration_list semicolon
 |
 ;

proc_or_func_declaration_list :
   proc_or_func_declaration_list semicolon proc_or_func_declaration
 | proc_or_func_declaration
 ;

proc_or_func_declaration : procedure_declaration
 | function_declaration
 ;

procedure_declaration : procedure_heading semicolon directive
 | procedure_heading semicolon procedure_block
 ;

procedure_heading : procedure_identification
 | procedure_identification formal_parameter_list
 ;

directive : RESERVED_FORWARD
 | RESERVED_EXTERNAL
 ;

formal_parameter_list : LPAREN formal_parameter_section_list RPAREN ;

formal_parameter_section_list : formal_parameter_section_list semicolon formal_parameter_section
 | formal_parameter_section
 ;

formal_parameter_section : value_parameter_specification
 | variable_parameter_specification
 | procedural_parameter_specification
 | functional_parameter_specification
 ;

value_parameter_specification : identifier_list COLON identifier
 ;

variable_parameter_specification : RESERVED_VAR identifier_list COLON identifier
 ;

procedural_parameter_specification : procedure_heading ;

functional_parameter_specification : function_heading ;

procedure_identification : RESERVED_PROCEDURE identifier ;

procedure_block : block ;

function_declaration : function_heading semicolon directive
 | function_identification semicolon function_block
 | function_heading semicolon function_block
 ;

function_heading : RESERVED_FUNCTION identifier COLON result_type
 | RESERVED_FUNCTION identifier formal_parameter_list COLON result_type
 ;

result_type : identifier ;

function_identification : RESERVED_FUNCTION identifier ;

function_block : block ;

statement_part : compound_statement ;

compound_statement : RESERVED_BEGIN statement_sequence RESERVED_END ;

statement_sequence : statement_sequence semicolon statement
 | statement
 ;

statement : open_statement
 | closed_statement
 ;

open_statement : label COLON non_labeled_open_statement
 | non_labeled_open_statement
 ;

closed_statement : label COLON non_labeled_closed_statement
 | non_labeled_closed_statement
 ;

non_labeled_closed_statement : assignment_statement
 | procedure_statement
 | goto_statement
 | compound_statement
 | case_statement
 | repeat_statement
 | closed_with_statement
 | closed_if_statement
 | closed_while_statement
 | closed_for_statement
 | exit_statement
 |
 ;

non_labeled_open_statement : open_with_statement
 | open_if_statement
 | open_while_statement
 | open_for_statement
 ;

repeat_statement : RESERVED_REPEAT statement_sequence RESERVED_UNTIL boolean_expression
 ;

open_while_statement : RESERVED_WHILE boolean_expression RESERVED_DO open_statement
 ;

closed_while_statement : RESERVED_WHILE boolean_expression RESERVED_DO closed_statement
 ;

open_for_statement : RESERVED_FOR control_variable ASSIGNMENT initial_value direction
   final_value RESERVED_DO open_statement
 ;

closed_for_statement : RESERVED_FOR control_variable ASSIGNMENT initial_value direction
   final_value RESERVED_DO closed_statement
 ;

open_with_statement : RESERVED_WITH record_variable_list RESERVED_DO open_statement
 ;

closed_with_statement : RESERVED_WITH record_variable_list RESERVED_DO closed_statement
 ;

open_if_statement : RESERVED_IF boolean_expression RESERVED_THEN statement
 | RESERVED_IF boolean_expression RESERVED_THEN closed_statement RESERVED_ELSE open_statement
 ;

closed_if_statement : RESERVED_IF boolean_expression RESERVED_THEN closed_statement
   RESERVED_ELSE closed_statement
 ;

assignment_statement : variable_access ASSIGNMENT expression
 ;

exit_statement : RESERVED_EXIT
;


variable_access : identifier
 | indexed_variable
 | field_designator
 | variable_access POINTER
 ;

indexed_variable : variable_access L_SQUARE_BRACKET index_expression_list R_SQUARE_BRACKET
 ;

index_expression_list : index_expression_list comma index_expression
 | index_expression
 ;

index_expression : expression ;

field_designator : variable_access DOT identifier
 ;

procedure_statement : identifier params
 | identifier
 ;

params : LPAREN actual_parameter_list RPAREN ;

actual_parameter_list : actual_parameter_list comma actual_parameter
 | actual_parameter
 ;


actual_parameter : expression
 | expression COLON expression
 | expression COLON expression COLON expression
 ;

goto_statement : RESERVED_GOTO label
 ;

case_statement : RESERVED_CASE case_index RESERVED_OF case_list_element_list RESERVED_END
 | RESERVED_CASE case_index RESERVED_OF case_list_element_list SEMI_COLON RESERVED_END
 | RESERVED_CASE case_index RESERVED_OF case_list_element_list semicolon
   otherwisepart statement RESERVED_END
 | RESERVED_CASE case_index RESERVED_OF case_list_element_list semicolon
   otherwisepart statement SEMI_COLON RESERVED_END
 ;

case_index : expression ;

case_list_element_list : case_list_element_list semicolon case_list_element
 | case_list_element
 ;

case_list_element : case_constant_list COLON statement
 ;

otherwisepart : RESERVED_OTHERWISE
 | RESERVED_OTHERWISE COLON
 ;

control_variable : identifier ;

initial_value : expression ;

direction : RESERVED_TO
 | RESERVED_DOWNTO
 ;

final_value : expression ;

record_variable_list : record_variable_list comma variable_access
 | variable_access
 ;

boolean_expression : expression ;

expression : simple_expression
 | simple_expression relop simple_expression
 ;

simple_expression : term
 | simple_expression addop term
 ;

term : factor
 | term mulop factor
 ;

factor : sign factor
 | exponentiation
 ;

exponentiation : primary
 | primary POWER exponentiation
 ;

primary : variable_access
 | unsigned_constant
 | function_designator
 | set_constructor
 | LPAREN expression RPAREN
 | RESERVED_NOT primary
 ;

unsigned_constant : unsigned_number
 | STRING
 | RESERVED_NIL
 ;

unsigned_number : unsigned_integer | unsigned_real ;

unsigned_integer : DIGITSEQ
 ;

unsigned_real : REALNUMBER
 ;

function_designator : identifier params
 ;

set_constructor : L_SQUARE_BRACKET member_designator_list R_SQUARE_BRACKET
 | L_SQUARE_BRACKET R_SQUARE_BRACKET
 ;

member_designator_list : member_designator_list comma member_designator
 | member_designator
 ;

member_designator : member_designator DOTDOT expression
 | expression
 ;

addop : PLUS
 | MINUS
 | RESERVED_OR
 | RESERVED_XOR
 ;

mulop : TIMES
 | DIVIDE
 | RESERVED_DIV
 | RESERVED_MOD
 | RESERVED_AND
 ;

relop : EQ
 | NE
 | LT
 | GT
 | LEQ
 | GEQ
 | RESERVED_IN
 ;

identifier : IDENTIFIER
 ;

semicolon : SEMI_COLON
 ;

comma : COMMA
 ;
