program array_simple;


var
	A: Array[0..9] of Integer;
	I,J : Integer;
	st : string;
begin
	I := 1;
	st := 'pqrst';
	// For J:=0 to 9 do
	// begin
	// 	A[J] :=  J+1;
	// end;

	// For J:=0 to 9 do
	// begin
	// 	write(A[J]);
	// 	// A[J] := J;
	// end;
end.


// root
// ['t4', 2, '', 'integer:=']
// ['t2', 't4', '', 'integer:=']
// ['t6', 1, '', ':=']
// ['t5', 0, '', ':=']
// ['t7', 't2', 0, 'int-']
// ['t7', 't7', 't6', 'int*']
// ['t5', 't5', 't7', 'int+']
// ['t6', 't6', 9, 'int*']
// ['t8', 't1', 't5', 'ARRAY_MEM_ACCESS']
// ['t9', 5, '', 'integer:=']
// ['t8', 't9', '', 'integer:=']
// ['t11', 1, '', ':=']
// ['t10', 0, '', ':=']
// ['t12', 't2', 0, 'int-']
// ['t12', 't12', 't11', 'int*']
// ['t10', 't10', 't12', 'int+']
// ['t11', 't11', 9, 'int*']
// ['t13', 't1', 't10', 'ARRAY_MEM_ACCESS']
// ['', 't13', '', 'WRITE_INT']