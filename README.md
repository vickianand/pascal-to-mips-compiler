*	This is the course project for CS335A(compiler design) at IIT Kanpur.
*	We are implementing a compiler of pascal language for MIPS platform.
*	We will use python as the implementation language.

Instructions for running the lexer
==================================

*       lexer.py is present in src/ directory.
*       Five test programs are present in test/ directory.
*       You can either run command: "python ./src/lexer.py test1.pas" or: "./src/lexer.py test1.pas".

Language feature not handled by our lexer
=========================================
*       We are not handling the multiline comments involving unbalanced number of comment start and end symbols.
*		As of version 2.5.1 it is possible to use reserved words as identifiers by escaping them with a & sign. But we are not handling it
