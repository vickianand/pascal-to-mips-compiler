var a:array[1..40] of longint;
    t,i,j,n,x,y:longint;
 begin
  a[1]:=1;
   for i:=2 to 40 do a[i]:=a[i-1] xor i;
    read(t);
     for i:=1 'to the' do begin'
      read(n);
       for j:=1 to n do read(x,y);
        writeln(a[n]);	/* print the result */
      end;		{ and we are done }


end.