var
	t, n, q, l, r, g, i: Longint;
	a, b, c: array of Longint; (*hi there
		whats up
		gsgsgsg*)
t = 2.3E4
t = 2E3
t = 2.0
t = 2344
t = 1E4
begin
	while (t > 0) do
	begin
		for i := 1 to n do
		begin
			read(a[i]);
			
			b[i] := 0;
			c[i] := 0;
		end;
		
		b[1] := a[1];
		c[n] := a[n];
		
		g := a[1];
		
		for i := 2 to n do
		begin
			g := gcd_recursive(g, a[i]);
			b[i] := g;
		end;
		
		g := a[n];
		
		for i := n - 1 downto 1 do
		begin
			g := gcd_recursive(g, a[i]);
			c[i] := g;
		end;
		
		while (q > 0) do
		begin
			readln(l, r);
			
			if l <> 1 then 
				begin
					if r <> n then
						writeln(gcd_recursive(b[l - 1], c[r + 1]))
					else
						writeln(b[l - 1])
				end
			else
				writeln(c[r + 1]);
			
			q := q - 1;
		end;
		
		t := t - 1;
	end;
end.