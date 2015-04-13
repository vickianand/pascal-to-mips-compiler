#maccarthy91.asm
.text
 .globl main
 main:
 	#prompting to enter an integer input
 	 la $a0, input
 	 li $v0, 4
	 syscall
	 #taking input
	 li $v0, 5 
	 syscall
	 move $a0 , $v0
	 jal maccarthy91
	 #moving result of mccarthy function to $a0 for printing
    move $a0, $v0
     li $v0, 1
	 syscall

	la $a0, nl_msg
	li $v0, 4
	syscall
	#exit
	 li $v0, 10
	syscall
#maccarthy91 takes argument in $a0 and returns result in $v0
maccarthy91:
	addi $sp, $sp, -4 #space for 1 words
	sw $ra, 0($sp)    #storing the return address for later use so that when $ra is updated to another vale, prsent return value is not lost
	li $t1, 100 
	bgt $a0, $t1 , mccarthy_decrease #taking the mccarthy_decrease branch to put $v0 = $a0 - 10 and then returning
	addi $a0, $a0 , 11 #adding $a0 = $a0 + 11 so as to call maccarthy91($a0 + 11)
	jal maccarthy91   #calling maccarthy91(n + 11)
	move $a0 $v0     #updating the result of previous function call to the argument of next call so as to call maccarthy91(maccarthy91(n + 11))
	jal maccarthy91 #calling maccarthy91(maccarthy91(n + 11)
mccarthy_return:
	lw $ra, 0($sp)  #restoring the value of return address
	addi $sp, $sp, 4 #restoring stack pointer
	jr $ra 				#jumping to return address
mccarthy_decrease:
	addi $v0, $a0, -10 #storing result = n - 10
	j mccarthy_return
.data
	nl_msg: .asciiz "\n"
	input: .asciiz "Enter the integer input : "