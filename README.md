Pascal to MIPS compiler written in python
=============================================

*	This is the course project for CS335A(compiler design) at IIT Kanpur.
*	We are implementing a compiler of pascal language for MIPS platform.
*	We will use python as the implementation language.


### Instructions for running the lexer
*       lexer.py is present in src/ directory.
*       Five test programs are present in test/ directory.
*       You can either run command: ```python src/lexer.py test/test1.pas``` or: ```./src/lexer.py test/test1.pas```.


### Instructions for running the parser
*       parser.py is present in src/ directory.
*       Run command: ```python src/parser.py test/hello.pas 2> debug_parse.out``` . We need the stderr debug content in debug_parse.out file.
*       Then run command: ```python scripts/tree_script.py``` .  This will generate productions.out and parse_tree.dot file.
*		Finally run ```dot -Tps parse_tree.dot -o parse_tree.ps``` . The generated parse_tree.ps file contailns the image of the tree.


### Language feature not handled by our lexer
*       We are not handling the multiline comments involving unbalanced number of comment start and end symbols.
*		As of version 2.5.1 it is possible to use reserved words as identifiers by escaping them with a '&' symbol. But we are not handling it.
*       Remark: Predefined types such as Byte, Boolean and constants such as maxint are not reserved words. They are identifiers, declared in the system unit. This means that these types can be redefined in other units. The programmer is however not encouraged to do this, as it will cause a lot of confusion. Lexer therefore recognises types as identifiers only.

