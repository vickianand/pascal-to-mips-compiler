program CLPERM;
uses math;
 
var	a: array[ 1..100001 ] of longInt;
 
procedure qsort( l, r: longInt );
var	i, j, t, med: longInt;
begin
	if ( l < r ) then
	begin
		i := l;
		j := r;
		med := a[ l + random(r - l + 1) ];
		while ( i <= j ) do
		begin
			while ( a[i] < med ) do
				inc( i );
			while ( a[j] > med ) do
				dec( j );
			
			if ( i <= j ) then
			begin
				t := a[i];
				a[i] := a[j];
				a[j] := t;
				
				inc( i );
				dec( j );
			end;
		end;
		
		qsort( l, j );
		qsort( i, r );
	end;
end;
 
var	t, n, k, i, last, next: longInt;
	bufIn, bufOut: array[ 1..1 shl 16 ] of byte;
	sum: int64;
 
begin
	setTextBuf( input, bufIn );
	setTextBuf( output, bufOut );
	
	readln( t );
	while ( t > 0 ) do
	begin
		readln( n, k );
		
		for i := 1 to k do
			read( a[i] );
		
		qsort( 1, k );
		
		inc( k );
		a[k] := n + 1;
		
		sum := 0;
		last := 0;
		i := 1;
		while ( i <= k ) do
		begin
			if ( a[i] <= last + 1 ) then
			begin
				if ( a[i] = last + 1 ) then
					inc( last );
			
				inc( i );
				
				continue;
			end;
		
			next := min( sum + 1, a[i] - 1 );
			
			if ( next <= last ) then
				break;
			
			inc( sum, ( next * int64(next + 1) - last * int64(last + 1) ) div 2 );
			
			last := next;
		end;
		
		if ( odd(sum) ) then
			writeln( 'Mom' )
		else
			writeln( 'Chef' );
		
		dec( t );
	end;
end.