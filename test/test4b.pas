program nested_ifelseChecking;
var
   a, b : integer;
   s1, s2, s3 : String;
begin
   a := 100;
   b:= 200;
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

['t6', 100, '', ':=']
['t1', 't6', '', ':=']
['t7', 200, '', ':=']
['t2', 't7', '', ':=']
['t8', 100, '', ':=']
['t9', 't1', 't8', 'int=']
['label_2', 't9', '', 'IF_FALSE_GOTO']
['t10', "'hello you!!'", '', ':=']
['t3', 't10', '', ':=']
['t11', 42, '', ':=']
['t12', 't2', 't11', 'int=']
['label_4', 't12', '', 'IF_FALSE_GOTO']
['t13', 3818, '', ':=']
['t2', 't13', '', ':=']
['label_5', '', '', 'GOTO']
['label_4', '', '', 'label']
['t14', "'allllllllllll'", '', ':=']
['t4', 't14', '', ':=']
['t15', "'hahahahaha  hjjg'", '', ':=']
['t4', 't15', '', ':=']
['label_5', '', '', 'label']
['t16', "'yooyoyoyyo'", '', ':=']
['t5', 't16', '', ':=']
['label_2', '', '', 'label']
['t17', "'Exact value of a is: '", '', ':=']
['t3', 't17', '', ':=']
['t18', "'Exact value of b is: '", '', ':=']
['t4', 't18', '', ':=']