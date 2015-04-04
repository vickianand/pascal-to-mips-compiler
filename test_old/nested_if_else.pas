program nested_ifelseChecking;
var
   a, b : integer;
   c, d : real;
   e, f : char;
   s1, s2, s3 : String;
begin
   a := 100;
   b:= 200;
   c := 500 ;
   d := b + c;
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


// root
// ['t10', 100, '', ':=']
// ['t1', 't10', '', ':=']
// ['t11', 200, '', ':=']
// ['t2', 't11', '', ':=']
// ['t12', 500, '', ':=']
// ['t13', 't12', '', 'INT_TO_REAL']
// ['t3', 't13', '', ':=']
// ['t15', 't2', '', 'INT_TO_REAL']
// ['t14', 't15', 't3', 'real+']
// ['t4', 't14', '', ':=']
// ['t16', 100, '', ':=']
// ['t17', 't1', 't16', 'int=']
// ['label_2', 't17', '', 'IF_FALSE_GOTO']
// ['t18', "'hello you!!'", '', ':=']
// ['t7', 't18', '', ':=']
// ['t19', 42, '', ':=']
// ['t20', 't2', 't19', 'int=']
// ['label_4', 't20', '', 'IF_FALSE_GOTO']
// ['t21', 3818, '', ':=']
// ['t2', 't21', '', ':=']
// ['label_5', '', '', 'GOTO']
// ['label_4', '', '', 'label']
// ['t22', "'allllllllllll'", '', ':=']
// ['t8', 't22', '', ':=']
// ['t23', "'hahahahaha  hjjg'", '', ':=']
// ['t8', 't23', '', ':=']
// ['label_5', '', '', 'label']
// ['t24', "'yooyoyoyyo'", '', ':=']
// ['t9', 't24', '', ':=']
// ['label_2', '', '', 'label']
// ['t25', "'Exact value of a is: '", '', ':=']
// ['t7', 't25', '', ':=']
// ['t26', "'Exact value of b is: '", '', ':=']
// ['t8', 't26', '', ':=']
