.text
main:
sub $sp $sp 120
move $fp $sp 
sub $sp 772 
# generating code for : integer:=  
lw $t1 656($sp) 
li $t1 0 
sw $t1 656($sp) 
# ===========================================  
# generating code for : integer:=  
lw $t1 660($sp) 
li $t1 9 
sw $t1 660($sp) 
# ===========================================  
# generating code for : int:=  
lw $t1 648($sp) 
lw $t2 656($sp) 
move $t1 $t2 
sw $t1 648($sp) 
# ===========================================  
# generating code for : label  
label_1 :  
# ===========================================  
# generating code for : int<=  
lw $t1 664($sp) 
lw $t2 648($sp) 
lw $t3 660($sp) 
sle $t1 $t2 $t3
sw $t1 664($sp) 
# ===========================================  
# generating code for : IF_FALSE_GOTO  
lw $t1 664($sp) 
beqz $t1 label_2 
# ===========================================  
# generating code for : integer:=  
lw $t1 668($sp) 
li $t1 0 
sw $t1 668($sp) 
# ===========================================  
# generating code for : integer:=  
lw $t1 672($sp) 
li $t1 9 
sw $t1 672($sp) 
# ===========================================  
# generating code for : int:=  
lw $t1 652($sp) 
lw $t2 668($sp) 
move $t1 $t2 
sw $t1 652($sp) 
# ===========================================  
# generating code for : label  
label_3 :  
# ===========================================  
# generating code for : int<=  
lw $t1 676($sp) 
lw $t2 652($sp) 
lw $t3 672($sp) 
sle $t1 $t2 $t3
sw $t1 676($sp) 
# ===========================================  
# generating code for : IF_FALSE_GOTO  
lw $t1 676($sp) 
beqz $t1 label_4 
# ===========================================  
# generating code for : int:=  
lw $t1 684($sp) 
li $t1 4 
sw $t1 684($sp) 
# ===========================================  
# generating code for : int:=  
lw $t1 680($sp) 
li $t1 0 
sw $t1 680($sp) 
# ===========================================  
# generating code for : int-  
lw $t1 688($sp) 
lw $t2 652($sp) 
sub $t1 $t2 0
sw $t1 688($sp) 
# ===========================================  
# generating code for : int*  
lw $t1 688($sp) 
lw $t2 688($sp) 
lw $t3 684($sp) 
mult $t2 $t3 
mflo $t1  
sw $t1 688($sp) 
# ===========================================  
# generating code for : int+  
lw $t1 680($sp) 
lw $t2 680($sp) 
lw $t3 688($sp) 
add $t1 $t2 $t3
sw $t1 680($sp) 
# ===========================================  
# generating code for : int*  
lw $t1 684($sp) 
lw $t2 684($sp) 
li $s7 9 
mult $t2 $s7 
mflo $t1  
sw $t1 684($sp) 
# ===========================================  
# generating code for : int-  
lw $t1 688($sp) 
lw $t2 648($sp) 
sub $t1 $t2 0
sw $t1 688($sp) 
# ===========================================  
# generating code for : int*  
lw $t1 688($sp) 
lw $t2 688($sp) 
lw $t3 684($sp) 
mult $t2 $t3 
mflo $t1  
sw $t1 688($sp) 
# ===========================================  
# generating code for : int+  
lw $t1 680($sp) 
lw $t2 680($sp) 
lw $t3 688($sp) 
add $t1 $t2 $t3
sw $t1 680($sp) 
# ===========================================  
# generating code for : int*  
lw $t1 684($sp) 
lw $t2 684($sp) 
li $s7 9 
mult $t2 $s7 
mflo $t1  
sw $t1 684($sp) 
# ===========================================  
# generating code for : ARRAY_MEM_ACCESS  
lw $t1 692($sp) 
lw $t2 680($sp) 
addi $t3 $sp 0
add $t1 $t2 $t3
sw $t1 692($sp) 
# ===========================================  
# generating code for : int*  
lw $t1 696($sp) 
lw $t2 648($sp) 
lw $t3 652($sp) 
mult $t2 $t3 
mflo $t1  
sw $t1 696($sp) 
# ===========================================  
# generating code for : integer:=  
lw $t9 692($sp) 
lw $t1 0($t9) 
lw $t2 696($sp) 
move $t1 $t2 
lw $t9 692($sp) 
sw $t1 0($t9) 
# ===========================================  
# generating code for : int+  
lw $t1 652($sp) 
lw $t2 652($sp) 
addi $t1 $t2 1
sw $t1 652($sp) 
# ===========================================  
# generating code for : GOTO  
j label_3  
# ===========================================  
# generating code for : label  
label_4 :  
# ===========================================  
# generating code for : int+  
lw $t1 648($sp) 
lw $t2 648($sp) 
addi $t1 $t2 1
sw $t1 648($sp) 
# ===========================================  
# generating code for : GOTO  
j label_1  
# ===========================================  
# generating code for : label  
label_2 :  
# ===========================================  
# generating code for : integer:=  
lw $t1 700($sp) 
li $t1 0 
sw $t1 700($sp) 
# ===========================================  
# generating code for : integer:=  
lw $t1 704($sp) 
li $t1 9 
sw $t1 704($sp) 
# ===========================================  
# generating code for : int:=  
lw $t1 648($sp) 
lw $t2 700($sp) 
move $t1 $t2 
sw $t1 648($sp) 
# ===========================================  
# generating code for : label  
label_5 :  
# ===========================================  
# generating code for : int<=  
lw $t1 708($sp) 
lw $t2 648($sp) 
lw $t3 704($sp) 
sle $t1 $t2 $t3
sw $t1 708($sp) 
# ===========================================  
# generating code for : IF_FALSE_GOTO  
lw $t1 708($sp) 
beqz $t1 label_6 
# ===========================================  
# generating code for : integer:=  
lw $t1 712($sp) 
li $t1 0 
sw $t1 712($sp) 
# ===========================================  
# generating code for : integer:=  
lw $t1 716($sp) 
li $t1 9 
sw $t1 716($sp) 
# ===========================================  
# generating code for : int:=  
lw $t1 652($sp) 
lw $t2 712($sp) 
move $t1 $t2 
sw $t1 652($sp) 
# ===========================================  
# generating code for : label  
label_7 :  
# ===========================================  
# generating code for : int<=  
lw $t1 720($sp) 
lw $t2 652($sp) 
lw $t3 716($sp) 
sle $t1 $t2 $t3
sw $t1 720($sp) 
# ===========================================  
# generating code for : IF_FALSE_GOTO  
lw $t1 720($sp) 
beqz $t1 label_8 
# ===========================================  
# generating code for : int:=  
lw $t1 728($sp) 
li $t1 4 
sw $t1 728($sp) 
# ===========================================  
# generating code for : int:=  
lw $t1 724($sp) 
li $t1 0 
sw $t1 724($sp) 
# ===========================================  
# generating code for : int-  
lw $t1 732($sp) 
lw $t2 652($sp) 
sub $t1 $t2 0
sw $t1 732($sp) 
# ===========================================  
# generating code for : int*  
lw $t1 732($sp) 
lw $t2 732($sp) 
lw $t3 728($sp) 
mult $t2 $t3 
mflo $t1  
sw $t1 732($sp) 
# ===========================================  
# generating code for : int+  
lw $t1 724($sp) 
lw $t2 724($sp) 
lw $t3 732($sp) 
add $t1 $t2 $t3
sw $t1 724($sp) 
# ===========================================  
# generating code for : int*  
lw $t1 728($sp) 
lw $t2 728($sp) 
li $s7 9 
mult $t2 $s7 
mflo $t1  
sw $t1 728($sp) 
# ===========================================  
# generating code for : int-  
lw $t1 732($sp) 
lw $t2 648($sp) 
sub $t1 $t2 0
sw $t1 732($sp) 
# ===========================================  
# generating code for : int*  
lw $t1 732($sp) 
lw $t2 732($sp) 
lw $t3 728($sp) 
mult $t2 $t3 
mflo $t1  
sw $t1 732($sp) 
# ===========================================  
# generating code for : int+  
lw $t1 724($sp) 
lw $t2 724($sp) 
lw $t3 732($sp) 
add $t1 $t2 $t3
sw $t1 724($sp) 
# ===========================================  
# generating code for : int*  
lw $t1 728($sp) 
lw $t2 728($sp) 
li $s7 9 
mult $t2 $s7 
mflo $t1  
sw $t1 728($sp) 
# ===========================================  
# generating code for : ARRAY_MEM_ACCESS  
lw $t1 736($sp) 
lw $t2 724($sp) 
addi $t3 $sp 0
add $t1 $t2 $t3
sw $t1 736($sp) 
# ===========================================  
# generating code for : WRITE_INT  
li $v0 1 
lw $a0 736($sp) 
lw $a0 0($a0) 
syscall   
# ===========================================  
# generating code for : int+  
lw $t1 652($sp) 
lw $t2 652($sp) 
addi $t1 $t2 1
sw $t1 652($sp) 
# ===========================================  
# generating code for : GOTO  
j label_7  
# ===========================================  
# generating code for : label  
label_8 :  
# ===========================================  
# generating code for : int+  
lw $t1 648($sp) 
lw $t2 648($sp) 
addi $t1 $t2 1
sw $t1 648($sp) 
# ===========================================  
# generating code for : GOTO  
j label_5  
# ===========================================  
# generating code for : label  
label_6 :  
# ===========================================  
li $v0, 10
syscall
