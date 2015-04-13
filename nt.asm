.text
main:
sub $sp $sp 120
addi $sp 32 
lw $t1 0($sp) 
lw $t2 8($sp) 
move $t1 $t2 
sw $t1 0($sp) 
lw $t1 4($sp) 
lw $t2 12($sp) 
move $t1 $t2 
sw $t1 4($sp) 
label_1 :  
lw $t1 24($sp) 
lw $t2 0($sp) 
lw $t3 20($sp) 
slt $t1 $t3 $t2
xori $t1 $t1 1
sw $t1 24($sp) 
lw $t1 24($sp) 
beqz $t1 label_2 
lw $t1 28($sp) 
lw $t2 4($sp) 
lw $t3 0($sp) 
add $t1 $t2 $t3
sw $t1 28($sp) 
lw $t1 4($sp) 
lw $t2 28($sp) 
move $t1 $t2 
sw $t1 4($sp) 
lw $t1 0($sp) 
lw $t2 0($sp) 
addi $t1 $t2 1
sw $t1 0($sp) 
j label_1  
label_2 :  
lw $t1 0($sp) 
lw $t2 4($sp) 
move $t1 $t2 
sw $t1 0($sp) 
li $v0, 10
syscall
