program CLPERM;
// uses math;
 
var	a: array[ 1..100001 ] of integer;
 
procedure qsort( l, r: integer );
var	i, j, t, med: integer;
begin
	if ( l < r ) then
	begin
		i := l;
		j := r;
		med := a[ l + (r - l + 1) div 2 ];
		while ( i <= j ) do
		begin
			while ( a[i] < med ) do
				// inc( i );
				i := i+1;
			while ( a[j] > med ) do
				// dec( j );
				j := j-1;
			
			if ( i <= j ) then
			begin
				t := a[i];
				a[i] := a[j];
				a[j] := t;
				
				// inc( i );
				i := i+1;
				// dec( j );
				j := j-1;
			end;
		end;
		
		qsort( l, j );
		qsort( i, r );
	end;
end;
 
var	t, n, k, i, last, next: integer;
	bufIn, bufOut: array[ 1..4096 ] of char;
	sum: integer;
	out_str : String;
 
begin
	// setTextBuf( input, bufIn );
	// setTextBuf( output, bufOut );
	
	// readln( t );
	while ( t > 0 ) do
	begin
		// readln( n, k );
		
		for i := 1 to k do
			// read( a[i] );
			a[i] := i*i;

		qsort( 1, k );
		
		// inc( k );
		k := k+1;
		a[k] := n + 1;
		
		sum := 0;
		last := 0;
		i := 1;
		while ( i <= k ) do
		begin
			if ( a[i] <= last + 1 ) then
			begin
				if ( a[i] = last + 1 ) then
					// inc( last );
					last := last +1;			
				// inc( i );
				i := i+1;				
				// continue;
			end;
		
			if ( sum + 1 < a[i] - 1 ) then
				next := sum + 1
			else
				next := a[i] - 1;

			if ( next <= last ) then
				// break;
				i := k+1;
			
			sum := sum + ( next * (next + 1) - last * (last + 1) ) div 2 ;
			
			last := next;
		end;
		
		if ( (sum mod 2) = 1 ) then
			// writeln( 'Mom' )
			out_str := 'Mom'
		else
			// writeln( 'Chef' );
			out_str := 'Chef';
		
		// dec( t );
		t := t - 1;
	end;
end.


// qsort
// ['label_1', '', '', 'label']
// ['t9', 't3', 't4', 'int<']
// ['label_3', 't9', '', 'IF_FALSE_GOTO']
// ['t5', 't3', '', ':=']
// ['t6', 't4', '', ':=']
// ['t10', 't4', 't3', 'int-']
// ['t11', 1, '', ':=']
// ['t12', 't10', 't11', 'int+']
// ['t13', 2, '', ':=']
// ['t14', 't12', 't13', 'intdiv']
// ['t15', 't3', 't14', 'int+']
// ['t17', 1, '', ':=']
// ['t16', 0, '', ':=']
// ['t18', 't15', 1, 'int-']
// ['t18', 't18', 't17', 'int*']
// ['t16', 't16', 't18', 'int+']
// ['t17', 't17', 100000, 'int*']
// ['t19', 't1', 't16', 'ARRAY_MEM_ACCESS']
// ['t8', 't19', '', ':=']
// ['t20', 't5', 't6', 'int<=']
// ['label_5', 't20', '', 'IF_FALSE_GOTO']
// ['t22', 1, '', ':=']
// ['t21', 0, '', ':=']
// ['t23', 't5', 1, 'int-']
// ['t23', 't23', 't22', 'int*']
// ['t21', 't21', 't23', 'int+']
// ['t22', 't22', 100000, 'int*']
// ['t24', 't1', 't21', 'ARRAY_MEM_ACCESS']
// ['t25', 't24', 't8', 'int<']
// ['label_7', 't25', '', 'IF_FALSE_GOTO']
// ['t26', 1, '', ':=']
// ['t27', 't5', 't26', 'int+']
// ['t5', 't27', '', ':=']
// ['label_7', '', '', 'label']
// ['t29', 1, '', ':=']
// ['t28', 0, '', ':=']
// ['t30', 't6', 1, 'int-']
// ['t30', 't30', 't29', 'int*']
// ['t28', 't28', 't30', 'int+']
// ['t29', 't29', 100000, 'int*']
// ['t31', 't1', 't28', 'ARRAY_MEM_ACCESS']
// ['t32', 't31', 't8', 'int>']
// ['label_9', 't32', '', 'IF_FALSE_GOTO']
// ['t33', 1, '', ':=']
// ['t34', 't6', 't33', 'int-']
// ['t6', 't34', '', ':=']
// ['label_9', '', '', 'label']
// ['t35', 't5', 't6', 'int<=']
// ['label_11', 't35', '', 'IF_FALSE_GOTO']
// ['t37', 1, '', ':=']
// ['t36', 0, '', ':=']
// ['t38', 't5', 1, 'int-']
// ['t38', 't38', 't37', 'int*']
// ['t36', 't36', 't38', 'int+']
// ['t37', 't37', 100000, 'int*']
// ['t39', 't1', 't36', 'ARRAY_MEM_ACCESS']
// ['t7', 't39', '', ':=']
// ['t41', 1, '', ':=']
// ['t40', 0, '', ':=']
// ['t42', 't5', 1, 'int-']
// ['t42', 't42', 't41', 'int*']
// ['t40', 't40', 't42', 'int+']
// ['t41', 't41', 100000, 'int*']
// ['t43', 't1', 't40', 'ARRAY_MEM_ACCESS']
// ['t45', 1, '', ':=']
// ['t44', 0, '', ':=']
// ['t46', 't6', 1, 'int-']
// ['t46', 't46', 't45', 'int*']
// ['t44', 't44', 't46', 'int+']
// ['t45', 't45', 100000, 'int*']
// ['t47', 't1', 't44', 'ARRAY_MEM_ACCESS']
// ['t43', 't47', '', ':=']
// ['t49', 1, '', ':=']
// ['t48', 0, '', ':=']
// ['t50', 't6', 1, 'int-']
// ['t50', 't50', 't49', 'int*']
// ['t48', 't48', 't50', 'int+']
// ['t49', 't49', 100000, 'int*']
// ['t51', 't1', 't48', 'ARRAY_MEM_ACCESS']
// ['t51', 't7', '', ':=']
// ['t52', 1, '', ':=']
// ['t53', 't5', 't52', 'int+']
// ['t5', 't53', '', ':=']
// ['t54', 1, '', ':=']
// ['t55', 't6', 't54', 'int-']
// ['t6', 't55', '', ':=']
// ['label_11', '', '', 'label']
// ['label_5', '', '', 'label']
// ['', 8, '', 'SET_PARAM_OFFSET_WIDTH']
// ['t3', '', '', 'PUSH_VAL_PARAMS']
// ['t6', '', '', 'PUSH_VAL_PARAMS']
// ['label_1', '', '', 'CALL_PROCEDURE']
// ['', 8, '', 'SET_PARAM_OFFSET_WIDTH']
// ['t5', '', '', 'PUSH_VAL_PARAMS']
// ['t4', '', '', 'PUSH_VAL_PARAMS']
// ['label_1', '', '', 'CALL_PROCEDURE']
// ['label_3', '', '', 'label']
// root
// ['t68', 0, '', ':=']
// ['t69', 't58', 't68', 'int>']
// ['label_13', 't69', '', 'IF_FALSE_GOTO']
// ['t70', 1, '', ':=']
// ['t61', 't70', '', ':=']
// ['label_14', '', '', 'label']
// ['t71', 't61', 't60', '<=']
// ['label_15', 't71', '', 'IF_FALSE_GOTO']
// ['t73', 1, '', ':=']
// ['t72', 0, '', ':=']
// ['t74', 't61', 1, 'int-']
// ['t74', 't74', 't73', 'int*']
// ['t72', 't72', 't74', 'int+']
// ['t73', 't73', 100000, 'int*']
// ['t75', 't1', 't72', 'ARRAY_MEM_ACCESS']
// ['t76', 't61', 't61', 'int*']
// ['t75', 't76', '', ':=']
// ['t61', 't61', 1, 'int+']
// ['label_14', '', '', 'GOTO']
// ['label_15', '', '', 'label']
// ['t77', 1, '', ':=']
// ['', 8, '', 'SET_PARAM_OFFSET_WIDTH']
// ['t77', '', '', 'PUSH_VAL_PARAMS']
// ['t60', '', '', 'PUSH_VAL_PARAMS']
// ['label_1', '', '', 'CALL_PROCEDURE']
// ['t79', 1, '', ':=']
// ['t80', 't60', 't79', 'int+']
// ['t60', 't80', '', ':=']
// ['t82', 1, '', ':=']
// ['t81', 0, '', ':=']
// ['t83', 't60', 1, 'int-']
// ['t83', 't83', 't82', 'int*']
// ['t81', 't81', 't83', 'int+']
// ['t82', 't82', 100000, 'int*']
// ['t84', 't1', 't81', 'ARRAY_MEM_ACCESS']
// ['t85', 1, '', ':=']
// ['t86', 't59', 't85', 'int+']
// ['t84', 't86', '', ':=']
// ['t87', 0, '', ':=']
// ['t66', 't87', '', ':=']
// ['t88', 0, '', ':=']
// ['t62', 't88', '', ':=']
// ['t89', 1, '', ':=']
// ['t61', 't89', '', ':=']
// ['t90', 't61', 't60', 'int<=']
// ['label_17', 't90', '', 'IF_FALSE_GOTO']
// ['t92', 1, '', ':=']
// ['t91', 0, '', ':=']
// ['t93', 't61', 1, 'int-']
// ['t93', 't93', 't92', 'int*']
// ['t91', 't91', 't93', 'int+']
// ['t92', 't92', 100000, 'int*']
// ['t94', 't1', 't91', 'ARRAY_MEM_ACCESS']
// ['t95', 1, '', ':=']
// ['t96', 't62', 't95', 'int+']
// ['t97', 't94', 't96', 'int<=']
// ['label_19', 't97', '', 'IF_FALSE_GOTO']
// ['t99', 1, '', ':=']
// ['t98', 0, '', ':=']
// ['t100', 't61', 1, 'int-']
// ['t100', 't100', 't99', 'int*']
// ['t98', 't98', 't100', 'int+']
// ['t99', 't99', 100000, 'int*']
// ['t101', 't1', 't98', 'ARRAY_MEM_ACCESS']
// ['t102', 1, '', ':=']
// ['t103', 't62', 't102', 'int+']
// ['t104', 't101', 't103', 'int=']
// ['label_21', 't104', '', 'IF_FALSE_GOTO']
// ['t105', 1, '', ':=']
// ['t106', 't62', 't105', 'int+']
// ['t62', 't106', '', ':=']
// ['label_21', '', '', 'label']
// ['t107', 1, '', ':=']
// ['t108', 't61', 't107', 'int+']
// ['t61', 't108', '', ':=']
// ['label_19', '', '', 'label']
// ['t109', 1, '', ':=']
// ['t110', 't66', 't109', 'int+']
// ['t112', 1, '', ':=']
// ['t111', 0, '', ':=']
// ['t113', 't61', 1, 'int-']
// ['t113', 't113', 't112', 'int*']
// ['t111', 't111', 't113', 'int+']
// ['t112', 't112', 100000, 'int*']
// ['t114', 't1', 't111', 'ARRAY_MEM_ACCESS']
// ['t115', 1, '', ':=']
// ['t116', 't114', 't115', 'int-']
// ['t117', 't110', 't116', 'int<']
// ['label_23', 't117', '', 'IF_FALSE_GOTO']
// ['t118', 1, '', ':=']
// ['t119', 't66', 't118', 'int+']
// ['t63', 't119', '', ':=']
// ['label_24', '', '', 'GOTO']
// ['label_23', '', '', 'label']
// ['t121', 1, '', ':=']
// ['t120', 0, '', ':=']
// ['t122', 't61', 1, 'int-']
// ['t122', 't122', 't121', 'int*']
// ['t120', 't120', 't122', 'int+']
// ['t121', 't121', 100000, 'int*']
// ['t123', 't1', 't120', 'ARRAY_MEM_ACCESS']
// ['t124', 1, '', ':=']
// ['t125', 't123', 't124', 'int-']
// ['t63', 't125', '', ':=']
// ['label_24', '', '', 'label']
// ['t126', 't63', 't62', 'int<=']
// ['label_26', 't126', '', 'IF_FALSE_GOTO']
// ['t127', 1, '', ':=']
// ['t128', 't60', 't127', 'int+']
// ['t61', 't128', '', ':=']
// ['label_26', '', '', 'label']
// ['t129', 1, '', ':=']
// ['t130', 't63', 't129', 'int+']
// ['t131', 't63', 't130', 'int*']
// ['t132', 1, '', ':=']
// ['t133', 't62', 't132', 'int+']
// ['t134', 't62', 't133', 'int*']
// ['t135', 't131', 't134', 'int-']
// ['t136', 2, '', ':=']
// ['t137', 't135', 't136', 'intdiv']
// ['t138', 't66', 't137', 'int+']
// ['t66', 't138', '', ':=']
// ['t62', 't63', '', ':=']
// ['label_17', '', '', 'label']
// ['t139', 2, '', ':=']
// ['t140', 't66', 't139', 'intmod']
// ['t141', 1, '', ':=']
// ['t142', 't140', 't141', 'int=']
// ['label_28', 't142', '', 'IF_FALSE_GOTO']
// ['t143', "'Mom'", '', ':=']
// ['t67', 't143', '', ':=']
// ['label_29', '', '', 'GOTO']
// ['label_28', '', '', 'label']
// ['t144', "'Chef'", '', ':=']
// ['t67', 't144', '', ':=']
// ['label_29', '', '', 'label']
// ['t145', 1, '', ':=']
// ['t146', 't58', 't145', 'int-']
// ['t58', 't146', '', ':=']
// ['label_13', '', '', 'label']