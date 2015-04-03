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
   a := b + c;
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
// ['t12', 100, '', ':=']
// ['t13', 't1', 't12', 'int=']
// ['label_2', 't13', '', 'IF_FALSE_GOTO']
// ['t14', "'hello you!!'", '', ':=']
// ['t7', 't14', '', ':=']
// ['t15', 42, '', ':=']
// ['t16', 't2', 't15', 'int=']
// ['label_4', 't16', '', 'IF_FALSE_GOTO']
// ['t17', 3818, '', ':=']
// ['t2', 't17', '', ':=']
// ['label_5', '', '', 'GOTO']
// ['label_4', '', '', 'label']
// ['t18', "'allllllllllll'", '', ':=']
// ['t8', 't18', '', ':=']
// ['t19', "'hahahahaha  hjjg'", '', ':=']
// ['t8', 't19', '', ':=']
// ['label_5', '', '', 'label']
// ['t20', "'yooyoyoyyo'", '', ':=']
// ['t9', 't20', '', ':=']
// ['label_2', '', '', 'label']
// ['t21', "'Exact value of a is: '", '', ':=']
// ['t7', 't21', '', ':=']
// ['t22', "'Exact value of b is: '", '', ':=']
// ['t8', 't22', '', ':=']
