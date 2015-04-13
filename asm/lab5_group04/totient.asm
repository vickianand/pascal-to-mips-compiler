 #totient.asm
 #this will take input an integer >= 0 and print number of integers less than the input which are co-prime to this
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
 	#moving the input to $a0 which is passed to the totient function
 	move $a0, $v0
 	#calling totient function from main with argument in $a0
    jal totient
    #moving result of totient function to $a0 for printing
    move $a0, $v0
     li $v0, 1
	 syscall
	la $a0, nl_msg
	li $v0, 4
	#exit
	syscall
	 li $v0, 10
	syscall
 #totient takes argument in $a0 and returns result in $v0
 totient:
 	addi $sp, $sp, -4 #space for 1 words
	sw $ra, 0($sp)    #store return address of totient function so that it can be used later 
 	#$vo stores my answer
 	li $v0, 0
 	li $t1, 1
 	#loop invariant for loop_totient is that $v0 contains number of integers less than $t0 which are co-prime to $a0
 	#in each run of loop_totient $to is incremented by 1
 	loop_totient:
 		# if $t0 contains value equal to $a0 i.e input then we have reached end of the loop and we return
 		bgt $t1 , $a0 ,return_totient
 		move $a1, $t1
 		move $t5 ,$a0
 		#$t3 will contain gcd of 
 		jal gcd
 		move $a0, $t5
 		#$t4 will contain 1 if $t3 i.e gcd of $t0 $a0 is less than 2 i.e. equal to 1, in other cases it'll contain 0
 		slti $t4, $t3, 2
 		#we updating the result $v0 based on whether gcd $a0 $t0 is 1
 		add $v0, $v0, $t4
 		addi $t1, $t1, 1
 		j loop_totient
 return_totient:
 		lw $ra, 0($sp)
 		addi $sp, $sp, 4
 		jr $ra



 	#gcd function takes two arguments in $a0 and $a1 where $a0 > $a1 and returns result in $t3
gcd:
	div $a0, $a1  #dividing the value of $a0 by $a1 and storing dividend in lo and remainder in hi
	mfhi $t0     #transfering the value of remainder to a temp register
	beqz $t0, gcd_return #if remainder is zero we'll go to gcd_return to print $a1 which we'll contain gcd
	move $a0, $a1     #using euclids algorithm to find gcd temp = a mod b; a = b; b = temp
	move $a1, $t0
	j gcd           #recursively calling the function to compute gcd
gcd_return:
	move $t3, $a1
	jr $ra

 .data
	nl_msg: .asciiz "\n"
	input: .asciiz "Enter the integer input : "