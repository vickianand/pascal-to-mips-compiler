.text
main:
sub $sp $sp 120
move $fp $sp 
sub $sp 64 
# generating code for : integer:=  
lw $t1 8($sp) 
li $t1 0 
sw $t1 8($sp) 
# ===========================================  
# generating code for : integer:=  
lw $t1 0($sp) 
lw $t2 8($sp) 
move $t1 $t2 
sw $t1 0($sp) 
# ===========================================  
# generating code for : integer:=  
lw $t1 12($sp) 
li $t1 0 
sw $t1 12($sp) 
# ===========================================  
# generating code for : integer:=  
lw $t1 4($sp) 
lw $t2 12($sp) 
move $t1 $t2 
sw $t1 4($sp) 
# ===========================================  
# generating code for : integer:=  
lw $t1 16($sp) 
li $t1 1 
sw $t1 16($sp) 
# ===========================================  
# generating code for : integer:=  
lw $t1 20($sp) 
li $t1 10 
sw $t1 20($sp) 
# ===========================================  
# generating code for : int:=  
lw $t1 0($sp) 
lw $t2 16($sp) 
move $t1 $t2 
sw $t1 0($sp) 
# ===========================================  
# generating code for : label  
label_1 :  
# ===========================================  
# generating code for : int<=  
lw $t1 24($sp) 
lw $t2 0($sp) 
lw $t3 20($sp) 
sle $t1 $t2 $t3
sw $t1 24($sp) 
# ===========================================  
# generating code for : IF_FALSE_GOTO  
lw $t1 24($sp) 
beqz $t1 label_2 
# ===========================================  
# generating code for : int+  
lw $t1 28($sp) 
lw $t2 4($sp) 
lw $t3 0($sp) 
add $t1 $t2 $t3
sw $t1 28($sp) 
# ===========================================  
# generating code for : integer:=  
lw $t1 4($sp) 
lw $t2 28($sp) 
move $t1 $t2 
sw $t1 4($sp) 
# ===========================================  
# generating code for : int+  
lw $t1 0($sp) 
lw $t2 0($sp) 
addi $t1 $t2 1
sw $t1 0($sp) 
# ===========================================  
# generating code for : GOTO  
j label_1  
# ===========================================  
# generating code for : label  
label_2 :  
# ===========================================  
# generating code for : WRITE_INT  
li $v0 1 
lw $a0 4($sp) 
syscall   
# ===========================================  
# generating code for : WRITE_NL  
li $v0 11 
li $a0 10 
syscall   
# ===========================================  
li $v0, 10
syscall
