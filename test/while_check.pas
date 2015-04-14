program while_check;
var
   number,sum,b : Integer;
   s2,s3 : string;
begin
	number := 10;
	sum := 0;
	while number>0 do
	begin
	   sum := sum + 1;
	   number := number - 2;
	end;
	writeln(sum);
end.

