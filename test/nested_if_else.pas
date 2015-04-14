program nested_ifelseChecking;
var
   a, b : integer;
   c, d : real;
   e, f : char;
   s1, s2, s3 : String;
begin
   a := 100;
   b:= 42;
   c := 500 ;
   d := b + c;
   if (a = 100) then
   begin
   	s1 := 'hello you!!';
   	if ( b = 42 ) then
   		b := 3818
   	else
		begin
			writeln('allllllllllll');
		end;
   	writeln('yooyoyoyyo');
   end;
      
   writeln('Exact value of a is: ', a);
   writeln('Exact value of b is: ', b);
end.

