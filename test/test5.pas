program test5;

var
	t: Integer;
	i, n: Longint;
	k, p, q: int64;
	a, b: array of int64;
	
begin
	readln(t);
	
	while (t > 0) do
	begin
		read(n);
		read(k);
		
		setlength(a, n);
		setlength(b, n);
		
		for i := 1 to n do
		begin
			read(a[i]);
		end;
		
		for i := 1 to n do
		begin
			read(b[i]);
		end;
		
		p := 0;
		q := 0;
		
		for i := 1 to n do
		begin
			q := k div a[i];
			q := q * b[i];
			
			if (q > p) then
			begin
				p := q;
			end;
		end;
		
		writeln(p);
		
		t := t - 1;
	end;
end.