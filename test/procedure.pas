Program VAR_PARAM_EXAMPLE;

  Procedure Square(index : Integer; Var Result : Integer);
  Begin
    Result := index * index;
  End;

Var
  Res : Integer;

Begin
 Writeln('The square of 5 is: ');
 Square(5, Res);
 Writeln(Res);
End.