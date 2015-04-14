.text
main:
sub $sp $sp 120
move $fp $sp 
sub $sp 56 
# generating code for : string:=  
lw $t1 12($sp) 
la $t1 t4 
sw $t1 12($sp) 
# ===========================================  
# generating code for : string:=  
lw $t1 0($sp) 
lw $t2 12($sp) 
move $t1 $t2 
sw $t1 0($sp) 
# ===========================================  
# generating code for : string:=  
lw $t1 16($sp) 
la $t1 t5 
sw $t1 16($sp) 
# ===========================================  
# generating code for : string:=  
lw $t1 4($sp) 
lw $t2 16($sp) 
move $t1 $t2 
sw $t1 4($sp) 
# ===========================================  
# generating code for : WRITE_STRING  
li $v0 4 
lw $a0 0($sp) 
syscall   
# ===========================================  
# generating code for : char:=  
lw $t1 20($sp) 
li $t1 '\n' 
sw $t1 20($sp) 
# ===========================================  
# generating code for : WRITE_CHAR  
li $v0 11 
lw $a0 20($sp) 
syscall   
# ===========================================  
# generating code for : WRITE_STRING  
li $v0 4 
lw $a0 4($sp) 
syscall   
# ===========================================  
# generating code for : string:=  
lw $t1 8($sp) 
lw $t2 4($sp) 
move $t1 $t2 
sw $t1 8($sp) 
# ===========================================  
# generating code for : WRITE_STRING  
li $v0 4 
lw $a0 8($sp) 
syscall   
# ===========================================  
li $v0, 10
syscall
.data
t4: .asciiz "hello"
t5: .asciiz "world"
