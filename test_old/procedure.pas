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
// root
// ['t6', 5, '', ':=']
// ['', 8, '', 'SET_PARAM_OFFSET_WIDTH']
// ['t6', '', '', 'PUSH_VAL_PARAMS']
// ['t5', '', '', 'PUSH_VAR_PARAMS']
// ['label_1', '', '', 'CALL_PROCEDURE']

