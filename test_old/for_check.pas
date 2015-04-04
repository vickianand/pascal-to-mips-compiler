program for_check;
var
   i,j, a, b : Integer;
   s1, s2, s3 : string;
begin
	for i := 1 to 1000 do
	begin
	j := j + i;
	if ( b = 42 ) then
   		b := 3818
   	else
		begin
			s2 := 'allllllllllll';
			s2 := 'hahahahaha  hjjg';
		end;
   	s3 := 'yooyoyoyyo';
	j := i + 8;
	end;
	s1 := 'hello world';
end.

// root
// ['t8', 1, '', ':=']
// ['t9', 1000, '', ':=']
// ['t1', 't8', '', ':=']
// ['label_1', '', '', 'label']
// ['t10', 't1', 't9', '<=']
// ['label_2', 't10', '', 'IF_FALSE_GOTO']
// ['t11', 't2', 't1', 'int+']
// ['t2', 't11', '', ':=']
// ['t12', 42, '', ':=']
// ['t13', 't4', 't12', 'int=']
// ['label_4', 't13', '', 'IF_FALSE_GOTO']
// ['t14', 3818, '', ':=']
// ['t4', 't14', '', ':=']
// ['label_5', '', '', 'GOTO']
// ['label_4', '', '', 'label']
// ['t15', "'allllllllllll'", '', ':=']
// ['t6', 't15', '', ':=']
// ['t16', "'hahahahaha  hjjg'", '', ':=']
// ['t6', 't16', '', ':=']
// ['label_5', '', '', 'label']
// ['t17', "'yooyoyoyyo'", '', ':=']
// ['t7', 't17', '', ':=']
// ['t18', 8, '', ':=']
// ['t19', 't1', 't18', 'int+']
// ['t2', 't19', '', ':=']
// ['t1', 't1', 1, 'int+']
// ['label_1', '', '', 'GOTO']
// ['label_2', '', '', 'label']
// ['t20', "'hello world'", '', ':=']
// ['t5', 't20', '', ':=']

