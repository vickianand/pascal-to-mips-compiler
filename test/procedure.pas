Program VAR_PARAM_EXAMPLE;

  Procedure Square(index : Integer; Var Result : Integer);
  Begin
    Result := index * index;
  End;

Var
  Res : Integer;

Begin
 // Writeln('The square of 5 is: ');
 Square(5, Res);
 // Write(Res);
End.


// square
// ['label_1', '', '', 'label']
// ['t4', 't2', 't2', 'int*']
// ['t3', 't4', '', ':=']
// ['t6', 5, '', ':=']
// root
