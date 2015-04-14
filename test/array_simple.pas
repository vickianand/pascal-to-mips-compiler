program array_simple;


var
	A: Array[0..9] of Integer;
	I,J : Integer;
begin
	I := 1;
	For J:=0 to 9 do
	begin
		A[J] :=  J * 11;
	end;

	For J:=0 to 9 do
	begin
		writeln(A[J]);
	end;
end.

