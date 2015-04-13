.text
main:
sub $sp $sp 120
move $fp $sp 
sub $sp 64 
lw $t1 8($sp) 
li $t1 10 
sw $t1 8($sp) 
lw $t1 0($sp) 
lw $t2 8($sp) 
move $t1 $t2 
sw $t1 0($sp) 
sw $fp -4($sp) 
move $fp $sp 
sub $sp $sp 48
addi $t0 $fp 12
sw $t0 -12($fp) 
lw $t1 0($sp) 
lw $t2 0($fp) 
move $t1 $t2 
sw $t1 0($sp) 
jal label_1  
lw $t1 16($sp) 
li $t1 1 
sw $t1 16($sp) 
lw $t1 20($sp) 
lw $t2 0($sp) 
lw $t3 16($sp) 
add $t1 $t2 $t3
sw $t1 20($sp) 
sw $fp -4($sp) 
move $fp $sp 
sub $sp $sp 48
addi $t0 $fp 24
sw $t0 -12($fp) 
lw $t1 0($sp) 
lw $t2 20($fp) 
move $t1 $t2 
sw $t1 0($sp) 
jal label_1  
lw $t1 28($sp) 
lw $t2 12($sp) 
lw $t3 24($sp) 
add $t1 $t2 $t3
sw $t1 28($sp) 
lw $t1 4($sp) 
lw $t2 28($sp) 
move $t1 $t2 
sw $t1 4($sp) 
li $v0, 10
syscall
sw $ra -8($fp) 
label_1 :  
sw $ra -8($fp) 
lw $t1 8($sp) 
li $t1 1 
sw $t1 8($sp) 
lw $t1 12($sp) 
lw $t2 0($sp) 
lw $t3 8($sp) 
add $t1 $t2 $t3
sw $t1 12($sp) 
lw $t1 4($sp) 
lw $t2 12($sp) 
move $t1 $t2 
sw $t1 4($sp) 
lw $t1 4($sp) 
lw $t0 -12($fp) 
sw $t1 0($t0) 
lw $ra -8($fp) 
move $sp $fp 
lw $fp -4($sp) 
j $ra