.text
main:
sub $sp $sp 120
move $fp $sp 
sub $sp 68 
# generating code for : READ_CHAR  
li $v0 12 
syscall   
lw $t1 12($sp) 
move $t1 $v0 
sw $t1 12($sp) 
# ===========================================  
# generating code for : WRITE_CHAR  
li $v0 11 
lw $a0 12($sp) 
syscall   
# ===========================================  
# generating code for : WRITE_NL  
li $v0 11 
li $a0 10 
syscall   
# ===========================================  
# generating code for : integer:=  
lw $t1 16($sp) 
li $t1 42 
sw $t1 16($sp) 
# ===========================================  
# generating code for : integer:=  
lw $t1 20($sp) 
li $t1 12 
sw $t1 20($sp) 
# ===========================================  
# generating code for : INT_TO_REAL  
l.s $f1 28($sp) 
lw $t2 16($sp) 
mtc1 $t2 $f1 
cvt.s.w $f1 $f1 
s.s $f1 28($sp) 
# ===========================================  
# generating code for : INT_TO_REAL  
l.s $f1 32($sp) 
lw $t2 20($sp) 
mtc1 $t2 $f1 
cvt.s.w $f1 $f1 
s.s $f1 32($sp) 
# ===========================================  
# generating code for : /  
l.s $f1 24($sp) 
l.s $f2 28($sp) 
l.s $f3 32($sp) 
div.s $f1 $f2 $f3
s.s $f1 24($sp) 
# ===========================================  
# generating code for : WRITE_REAL  
li $v0 2 
l.s $f12 24($sp) 
syscall   
# ===========================================  
# generating code for : WRITE_NL  
li $v0 11 
li $a0 10 
syscall   
# ===========================================  
li $v0, 10
syscall
