program sum_n;
var
   i,j: Integer;
begin
	i := 0;
	j := 0;
	for i := 1 to 10 do
	begin
	j := j + i;
	end;
	i := j;
end.


// root
// ['t3', 0, '', ':=']
// ['t1', 't3', '', ':=']
// ['t4', 0, '', ':=']
// ['t2', 't4', '', ':=']
// ['t5', 1, '', ':=']
// ['t6', 10, '', ':=']
// ['t1', 't5', '', ':=']
// ['label_1', '', '', 'label']
// ['t7', 't1', 't6', '<=']
// ['label_2', 't7', '', 'IF_FALSE_GOTO']
// ['t8', 't2', 't1', 'int+']
// ['t2', 't8', '', ':=']
// ['t1', 't1', 1, 'int+']
// ['label_1', '', '', 'GOTO']
// ['label_2', '', '', 'label']
// ['t1', 't2', '', ':=']

// .text
// main:
// sub $sp $sp 120
// lw $t1 8($sp) 
// li $t1 0 
// sw $t1 8($sp) 
// lw $t1 0($sp) 
// lw $t2 8($sp) 
// move $t1 $t2 
// sw $t1 0($sp) 
// lw $t1 12($sp) 
// li $t1 0 
// sw $t1 12($sp) 
// lw $t1 4($sp) 
// lw $t2 12($sp) 
// move $t1 $t2 
// sw $t1 4($sp) 
// lw $t1 16($sp) 
// li $t1 1 
// sw $t1 16($sp) 
// lw $t1 20($sp) 
// li $t1 10 
// sw $t1 20($sp) 
// lw $t1 0($sp) 
// lw $t2 16($sp) 
// move $t1 $t2 
// sw $t1 0($sp) 
// label_1 :  
// lw $t1 24($sp) 
// lw $t2 0($sp) 
// lw $t3 20($sp) 
// slt $t1 $t3 $t2
// xori $t1 $t1 1
// sw $t1 24($sp) 
// lw $t1 24($sp) 
// beqz $t1 label_2 
// lw $t1 28($sp) 
// lw $t2 4($sp) 
// lw $t3 0($sp) 
// add $t1 $t2 $t3
// sw $t1 28($sp) 
// lw $t1 4($sp) 
// lw $t2 28($sp) 
// move $t1 $t2 
// sw $t1 4($sp) 
// lw $t1 0($sp) 
// lw $t2 0($sp) 
// addi $t1 $t2 1
// sw $t1 0($sp) 
// j label_1  
// label_2 :  
// lw $t1 0($sp) 
// lw $t2 4($sp) 
// move $t1 $t2 
// sw $t1 0($sp) 
// li $v0, 10
// syscall