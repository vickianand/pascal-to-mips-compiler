program nested_ifelseChecking;
var
   a, b : integer;
   s1, s2, s3 : String;
begin
   a := 100;
   b:= 200;
   if (a = 100) then
   begin
   	s1 := 'hello you!!';
   	if ( b = 42 ) then
   		b := 3818
   	else
		begin
			s2 := 'allllllllllll';
			s2 := 'hahahahaha  hjjg';
		end;
   	s3 := 'yooyoyoyyo';
   end;
      
   s1 := 'Exact value of a is: ';
   s2 := 'Exact value of b is: ';
end.

