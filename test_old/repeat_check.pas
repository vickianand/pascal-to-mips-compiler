program repeatUntilLoop;
var
   a, b: integer;
begin
   a := 20;
   b := 10;
   (* repeat until loop execution *)
   repeat
      b := b + 1;
      if b > 20 then
      	a := a + 1;
   until a = 20;
   a := 321;
end.


// root
// ['t3', 20, '', ':=']
// ['t1', 't3', '', ':=']
// ['t4', 10, '', ':=']
// ['t2', 't4', '', ':=']
// ['label_1', '', '', 'label']
// ['t5', 1, '', ':=']
// ['t6', 't2', 't5', 'int+']
// ['t2', 't6', '', ':=']
// ['t7', 20, '', ':=']
// ['t8', 't2', 't7', 'int>']
// ['label_3', 't8', '', 'IF_FALSE_GOTO']
// ['t9', 1, '', ':=']
// ['t10', 't1', 't9', 'int+']
// ['t1', 't10', '', ':=']
// ['label_3', '', '', 'label']
// ['t11', 20, '', ':=']
// ['t12', 't1', 't11', 'int=']
// ['label_1', 't12', '', 'IF_TRUE_GOTO']
// ['t13', 321, '', ':=']
// ['t1', 't13', '', ':=']
