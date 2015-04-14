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
# generating code for : char:=  
lw $t1 16($sp) 
li $t1 '\n' 
sw $t1 16($sp) 
# ===========================================  
# generating code for : WRITE_CHAR  
li $v0 11 
lw $a0 16($sp) 
syscall   
# ===========================================  
# generating code for : WRITE_NL  
li $v0 11 
li $a0 10 
syscall   
# ===========================================  
# generating code for : int:=  
lw $t1 0($sp) 
lw $t2 12($sp) 
move $t1 $t2 
sw $t1 0($sp) 
# ===========================================  
# generating code for : WRITE_INT  
li $v0 1 
lw $a0 0($sp) 
syscall   
# ===========================================  
# generating code for : WRITE_NL  
li $v0 11 
li $a0 10 
syscall   
# ===========================================  
# generating code for : char:=  
lw $t1 20($sp) 
li $t1 'c' 
sw $t1 20($sp) 
# ===========================================  
# generating code for : WRITE_CHAR  
li $v0 11 
lw $a0 20($sp) 
syscall   
# ===========================================  
# generating code for : WRITE_NL  
li $v0 11 
li $a0 10 
syscall   
# ===========================================  
# generating code for : integer:=  
lw $t1 24($sp) 
li $t1 12 
sw $t1 24($sp) 
# ===========================================  
# generating code for : integer:=  
lw $t1 28($sp) 
li $t1 12 
sw $t1 28($sp) 
# ===========================================  
# generating code for : int=  
lw $t1 32($sp) 
lw $t2 24($sp) 
lw $t3 28($sp) 
seq $t1 $t2 $t3
sw $t1 32($sp) 
# ===========================================  
# generating code for : WRITE_INT  
li $v0 1 
lw $a0 32($sp) 
syscall   
# ===========================================  
# generating code for : WRITE_NL  
li $v0 11 
li $a0 10 
syscall   
# ===========================================  
li $v0, 10
syscall
