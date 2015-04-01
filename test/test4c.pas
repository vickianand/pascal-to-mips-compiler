program while_check;
var
   number,sum,b : Integer;
   s2,s3 : string;
begin
	number := 1;
	sum := 0;
	while number>0 do
	begin
	   sum := sum + number;
	   number := number - 2;
	end;
	if ( b = 42 ) then
   		b := 3818
   	else
   		begin
   			s2 := 'allllllllllll';
   			s2 := 'hahahahaha  hjjg';
   		end;
   		s3 := 'yooyoyoyyo';
end.

['t6', 1, '', ':=']
['t1', 't6', '', ':=']
['t7', 0, '', ':=']
['t2', 't7', '', ':=']
['t8', 0, '', ':=']
['t9', 't1', 't8', 'int>']
['label_2', 't9', '', 'IF_FALSE_GOTO']
['t10', 't2', 't1', 'int+']
['t2', 't10', '', ':=']
['t11', 2, '', ':=']
['t12', 't1', 't11', 'int-']
['t1', 't12', '', ':=']
['label_2', '', '', 'label']
['t13', 42, '', ':=']
['t14', 't3', 't13', 'int=']
['label_4', 't14', '', 'IF_FALSE_GOTO']
['t15', 3818, '', ':=']
['t3', 't15', '', ':=']
['label_5', '', '', 'GOTO']
['label_4', '', '', 'label']
['t16', "'allllllllllll'", '', ':=']
['t4', 't16', '', ':=']
['t17', "'hahahahaha  hjjg'", '', ':=']
['t4', 't17', '', ':=']
['label_5', '', '', 'label']
['t18', "'yooyoyoyyo'", '', ':=']
['t5', 't18', '', ':=']