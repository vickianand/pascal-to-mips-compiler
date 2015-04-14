program repeatUntilLoop;
var
   a, b: integer;
begin
   a := 10;
   b := 500;
   (* repeat until loop execution *)
   repeat
      a := a + 1;
      b := b + 10;
   until a < 20;
   writeln('b: ',  b, ', a:', a);

end.
