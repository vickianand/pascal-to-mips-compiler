program testarray1;


var
	A,B : Array[0..10,0..10] of Integer;
	I,J : Integer;
begin
	For I:=0 to 9 do
		For J:=0 to 9 do
			A[I,J]:= I*J;
	For I:=0 to 9 do
	begin
		For J:=0 to 9 do
			write(A[I,J], ' ');
		write('\n');
	end
end.

