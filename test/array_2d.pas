program testarray1;


var
	A,B : Array[0..9,0..9] of Integer;
	I,J : Integer;
begin
	For I:=0 to 9 do
		For J:=0 to 9 do
			A[I,J]:=I*J;
	For I:=0 to 9 do
	begin
		For J:=0 to 9 do
			Write(A[I,J],' ');
			Writeln;
			A[I,J] := 111;
	end;
	B:=A;
	Writeln;
	For I:=0 to 9 do
		For J:=0 to 9 do
			A[9-I,9-J]:=I*J;
	For I:=0 to 9 do
	begin
		For J:=0 to 9 do
			Write(B[I,J],' ');
			Writeln;
			A[I,J] := 222;
	end;
end.


// ['t5', 0, '', ':=']
// ['t6', 9, '', ':=']
// ['t3', 't5', '', ':=']
// ['label_1', '', '', 'label']
// ['t7', 't3', 't6', '<=']
// ['label_2', 't7', '', 'IF_FALSE_GOTO']
// ['t8', 0, '', ':=']
// ['t9', 9, '', ':=']
// ['t4', 't8', '', ':=']
// ['label_3', '', '', 'label']
// ['t10', 't4', 't9', '<=']
// ['label_4', 't10', '', 'IF_FALSE_GOTO']
// ['t12', 1, '', ':=']
// ['t11', 0, '', ':=']
// ['t13', 't4', 0, 'int-']
// ['t13', 't13', 't12', 'int*']
// ['t11', 't11', 't13', 'int+']
// ['t12', 't12', 9, 'int*']
// ['t13', 't3', 0, 'int-']
// ['t13', 't13', 't12', 'int*']
// ['t11', 't11', 't13', 'int+']
// ['t12', 't12', 9, 'int*']
// ['t14', 't1', 't11', 'ARRAY_MEM_ACCESS']
// ['t15', 't3', 't4', 'int*']
// ['t14', 't15', '', ':=']
// ['t4', 't4', 1, 'int+']
// ['label_3', '', '', 'GOTO']
// ['label_4', '', '', 'label']
// ['t3', 't3', 1, 'int+']
// ['label_1', '', '', 'GOTO']
// ['label_2', '', '', 'label']
// ['t16', 0, '', ':=']
// ['t17', 9, '', ':=']
// ['t3', 't16', '', ':=']
// ['label_5', '', '', 'label']
// ['t18', 't3', 't17', '<=']
// ['label_6', 't18', '', 'IF_FALSE_GOTO']
// ['t19', 0, '', ':=']
// ['t20', 9, '', ':=']
// ['t4', 't19', '', ':=']
// ['label_7', '', '', 'label']
// ['t21', 't4', 't20', '<=']
// ['label_8', 't21', '', 'IF_FALSE_GOTO']
// ['t23', 1, '', ':=']
// ['t22', 0, '', ':=']
// ['t24', 't4', 0, 'int-']
// ['t24', 't24', 't23', 'int*']
// ['t22', 't22', 't24', 'int+']
// ['t23', 't23', 9, 'int*']
// ['t24', 't3', 0, 'int-']
// ['t24', 't24', 't23', 'int*']
// ['t22', 't22', 't24', 'int+']
// ['t23', 't23', 9, 'int*']
// ['t25', 't1', 't22', 'ARRAY_MEM_ACCESS']
// ['t26', 111, '', ':=']
// ['t25', 't26', '', ':=']
// ['t4', 't4', 1, 'int+']
// ['label_7', '', '', 'GOTO']
// ['label_8', '', '', 'label']
// ['t3', 't3', 1, 'int+']
// ['label_5', '', '', 'GOTO']
// ['label_6', '', '', 'label']
// ['t2', 't1', '', ':=']
// ['t27', 0, '', ':=']
// ['t28', 9, '', ':=']
// ['t3', 't27', '', ':=']
// ['label_9', '', '', 'label']
// ['t29', 't3', 't28', '<=']
// ['label_10', 't29', '', 'IF_FALSE_GOTO']
// ['t30', 0, '', ':=']
// ['t31', 9, '', ':=']
// ['t4', 't30', '', ':=']
// ['label_11', '', '', 'label']
// ['t32', 't4', 't31', '<=']
// ['label_12', 't32', '', 'IF_FALSE_GOTO']
// ['t33', 9, '', ':=']
// ['t34', 't33', 't3', 'int-']
// ['t35', 9, '', ':=']
// ['t36', 't35', 't4', 'int-']
// ['t38', 1, '', ':=']
// ['t37', 0, '', ':=']
// ['t39', 't36', 0, 'int-']
// ['t39', 't39', 't38', 'int*']
// ['t37', 't37', 't39', 'int+']
// ['t38', 't38', 9, 'int*']
// ['t39', 't34', 0, 'int-']
// ['t39', 't39', 't38', 'int*']
// ['t37', 't37', 't39', 'int+']
// ['t38', 't38', 9, 'int*']
// ['t40', 't1', 't37', 'ARRAY_MEM_ACCESS']
// ['t41', 't3', 't4', 'int*']
// ['t40', 't41', '', ':=']
// ['t4', 't4', 1, 'int+']
// ['label_11', '', '', 'GOTO']
// ['label_12', '', '', 'label']
// ['t3', 't3', 1, 'int+']
// ['label_9', '', '', 'GOTO']
// ['label_10', '', '', 'label']
// ['t42', 0, '', ':=']
// ['t43', 9, '', ':=']
// ['t3', 't42', '', ':=']
// ['label_13', '', '', 'label']
// ['t44', 't3', 't43', '<=']
// ['label_14', 't44', '', 'IF_FALSE_GOTO']
// ['t45', 0, '', ':=']
// ['t46', 9, '', ':=']
// ['t4', 't45', '', ':=']
// ['label_15', '', '', 'label']
// ['t47', 't4', 't46', '<=']
// ['label_16', 't47', '', 'IF_FALSE_GOTO']
// ['t49', 1, '', ':=']
// ['t48', 0, '', ':=']
// ['t50', 't4', 0, 'int-']
// ['t50', 't50', 't49', 'int*']
// ['t48', 't48', 't50', 'int+']
// ['t49', 't49', 9, 'int*']
// ['t50', 't3', 0, 'int-']
// ['t50', 't50', 't49', 'int*']
// ['t48', 't48', 't50', 'int+']
// ['t49', 't49', 9, 'int*']
// ['t51', 't1', 't48', 'ARRAY_MEM_ACCESS']
// ['t52', 222, '', ':=']
// ['t51', 't52', '', ':=']
// ['t4', 't4', 1, 'int+']
// ['label_15', '', '', 'GOTO']
// ['label_16', '', '', 'label']
// ['t3', 't3', 1, 'int+']
// ['label_13', '', '', 'GOTO']
// ['label_14', '', '', 'label']
