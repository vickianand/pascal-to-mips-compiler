program arrays;

Var
    myVar   : Integer;
    myArray : Array[1..5] of Integer;

Begin
 myArray[2] := 25;
 myVar := myArray[2];
End.

// root
// ['t3', 2, '', ':=']
// ['t5', 1, '', ':=']
// ['t4', 0, '', ':=']
// ['t6', 't3', 1, 'int-']
// ['t6', 't6', 't5', 'int*']
// ['t4', 't4', 't6', 'int+']
// ['t5', 't5', 4, 'int*']
// ['t7', 't2', 't4', 'ARRAY_ACCESS']
// ['t8', 25, '', ':=']

// ['t9', 2, '', ':=']
// ['t11', 1, '', ':=']
// ['t10', 0, '', ':=']
// ['t12', 't9', 1, 'int-']
// ['t12', 't12', 't11', 'int*']
// ['t10', 't10', 't12', 'int+']
// ['t11', 't11', 4, 'int*']
// ['t13', 't2', 't10', 'ARRAY_ACCESS']
