program basic;

function basic(n:integer): integer;
begin
    basic := n + 100;
end;

var
    i:integer;
    out : integer;

begin
    read(i);
    out := basic(i);
    writeln(out)
end.