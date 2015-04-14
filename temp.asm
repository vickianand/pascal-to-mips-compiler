.text
# generating code for : FUNC_BEGIN  
sw $ra -8($fp) 
# ===========================================  
# generating code for : label  
label_1 :  
# ===========================================  
# generating code for : FUNC_BEGIN  
sw $ra -8($fp) 
# ===========================================  
# generating code for : integer:=  
lw $t1 8($sp) 
li $t1 2 
sw $t1 8($sp) 
# ===========================================  
# generating code for : int<=  
lw $t1 12($sp) 
lw $t2 0($sp) 
lw $t3 8($sp) 
slt $t1 $t3 $t2
xori $t1 $t1 1
sw $t1 12($sp) 
# ===========================================  
# generating code for : IF_FALSE_GOTO  
lw $t1 12($sp) 
beqz $t1 label_3 
# ===========================================  
# generating code for : integer:=  
lw $t1 16($sp) 
li $t1 1 
sw $t1 16($sp) 
# ===========================================  
# generating code for : integer:=  
lw $t1 4($sp) 
lw $t2 16($sp) 
move $t1 $t2 
sw $t1 4($sp) 
# ===========================================  
# generating code for : GOTO  
j label_4  
# ===========================================  
# generating code for : label  
label_3 :  
# ===========================================  
# generating code for : integer:=  
lw $t1 20($sp) 
li $t1 1 
sw $t1 20($sp) 
# ===========================================  
# generating code for : int-  
lw $t1 24($sp) 
lw $t2 0($sp) 
lw $t3 20($sp) 
sub $t1 $t2 $t3
sw $t1 24($sp) 
# ===========================================  
# generating code for : SET_PARAM_OFFSET_WIDTH  
# ===========================================  
# generating code for : PUSH_VAL_PARAMS  
# ===========================================  
# generating code for : CALL_FUNCTION  
sw $fp -4($sp) 
move $fp $sp 
sub $sp $sp 80
addi $t0 $fp 28
sw $t0 -12($fp) 
lw $t1 0($sp) 
lw $t2 24($fp) 
move $t1 $t2 
sw $t1 0($sp) 
jal label_1  
# ===========================================  
# generating code for : integer:=  
lw $t1 32($sp) 
li $t1 2 
sw $t1 32($sp) 
# ===========================================  
# generating code for : int-  
lw $t1 36($sp) 
lw $t2 0($sp) 
lw $t3 32($sp) 
sub $t1 $t2 $t3
sw $t1 36($sp) 
# ===========================================  
# generating code for : SET_PARAM_OFFSET_WIDTH  
# ===========================================  
# generating code for : PUSH_VAL_PARAMS  
# ===========================================  
# generating code for : CALL_FUNCTION  
sw $fp -4($sp) 
move $fp $sp 
sub $sp $sp 80
addi $t0 $fp 40
sw $t0 -12($fp) 
lw $t1 0($sp) 
lw $t2 36($fp) 
move $t1 $t2 
sw $t1 0($sp) 
jal label_1  
# ===========================================  
# generating code for : int+  
lw $t1 44($sp) 
lw $t2 28($sp) 
lw $t3 40($sp) 
add $t1 $t2 $t3
sw $t1 44($sp) 
# ===========================================  
# generating code for : integer:=  
lw $t1 4($sp) 
lw $t2 44($sp) 
move $t1 $t2 
sw $t1 4($sp) 
# ===========================================  
# generating code for : label  
label_4 :  
# ===========================================  
# generating code for : FUNC_RETURN  
lw $t1 4($sp) 
lw $t0 -12($fp) 
sw $t1 0($t0) 
lw $ra -8($fp) 
move $sp $fp 
lw $fp -4($sp) 
j $ra  
# ===========================================  
main:
sub $sp $sp 120
move $fp $sp 
sub $sp 52 
# generating code for : READ_INT  
li $v0 5 
syscall   
lw $t1 0($sp) 
move $t1 $v0 
sw $t1 0($sp) 
# ===========================================  
# generating code for : SET_PARAM_OFFSET_WIDTH  
# ===========================================  
# generating code for : PUSH_VAL_PARAMS  
# ===========================================  
# generating code for : CALL_FUNCTION  
sw $fp -4($sp) 
move $fp $sp 
sub $sp $sp 80
addi $t0 $fp 8
sw $t0 -12($fp) 
lw $t1 0($sp) 
lw $t2 0($fp) 
move $t1 $t2 
sw $t1 0($sp) 
jal label_1  
# ===========================================  
# generating code for : integer:=  
lw $t1 4($sp) 
lw $t2 8($sp) 
move $t1 $t2 
sw $t1 4($sp) 
# ===========================================  
# generating code for : integer:=  
lw $t1 12($sp) 
li $t1 2 
sw $t1 12($sp) 
# ===========================================  
# generating code for : int*  
lw $t1 16($sp) 
lw $t2 4($sp) 
lw $t3 12($sp) 
mult $t2 $t3 
mflo $t1  
sw $t1 16($sp) 
# ===========================================  
# generating code for : WRITE_INT  
li $v0 1 
lw $a0 16($sp) 
syscall   
# ===========================================  
li $v0, 10
syscall
