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

 	#calling goldbach function from main with argument in $a0
    jal goldbach

    #moving result of goldbach function to $a0 and $a1 for printing
    move $a0, $v0	#print the first result
    li $v0, 1
	syscall
	la $a0, nl_msg	#print new line
	li $v0, 4
	syscall

	move $a0, $v1 	#print the second result
    li $v0, 1
	syscall
	la $a0, nl_msg	#print new line
	li $v0, 4
	syscall

	#exit
	li $v0, 10
	syscall
 #goldbach takes argument in $a0 and returns result in $v0 and $v1
 goldbach:
  	addi $sp, $sp, -4 #space for 1 words
	sw $ra, 0($sp)    #store return address of totient function so that it can be used later 

 	li $v0 , -1 		  				#return values when input is even
 	li $v1 , -1
 	rem $t0 , $a0 , 2				#calculating remainder of input when divided by 2
 	addi $t0 , $t0 , -1 			#$t0 will be zerom iff input i.e $a0 is even
 	beqz $t0 , goldbach_return 		#return if input was even

 	beq $a0 , 2 , goldbach_return	#if input is 2 then still answer doesnot exist

 	beq $a0 , 4 , goldbach_return1  #special case for 4 , 4 = 2 + 2 sum of non odd prime

 	li $v0 , 1						#$v0+$v1=$a0
 	sub $v1 , $a0 , $v0				#answer if found when both $v1 and $v2 are prime

 	loop_goldbach:
 		addi $v0 , $v0 , 2			#updating $v0 and $v0 to check new values 
 		addi $v1 , $v1 , -2

#NOTE: A number is prime on if totient function of that number is one less than itself. Else in 
#all other cases it is non prime. 
 		move $a0 , $v0				#checking if $v0 is prime
 		jal totient 
 		move $t6 , $v0				#totient function returns answr in $v0
 		move $v0 , $a0				#restore $v0
 		addi $t6 , $t6 , 2
 		sub	$t6 , $t6 , $v0			#if $t0 is less than  or equal to zero
 		blez $t6 , loop_goldbach	#continue if $v0 is not a prime

 									#checking if $v1 is prime
 		move $t6 , $v0				#store $v0 in temporary variable $t1 as totient function returns answer in $v0
 		move $a0 , $v1				
 		jal totient 
 		move $t7 , $v0				
 		move $v1 , $a0				#restore $v1
 		move $v0 , $t6				#restore $v0
 		addi $t7 , $t7 , 2
 		sub	$t7 , $t7 , $v1			#if $t0 is less than or equal to zero
 		blez $t7 , loop_goldbach	#continue if $v0 is not a prime

 		#if program counter reaches here then $v0 and $v1 are both primes and we have found the answer
 		j goldbach_return			#return as we have found the answer	

 goldbach_return:
  		lw $ra, 0($sp)
 		addi $sp, $sp, 4
 		jr $ra
 goldbach_return1:
  		lw $ra, 0($sp)
 		addi $sp, $sp, 4
 		li $v0 , 2
 		li $v1 , 2 
 		jr $ra
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
 	#gcd function takes two arguments in $a0 and $a1 where $a0 > $a1
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