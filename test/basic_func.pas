program basic;

function basic(n:integer): integer;
begin
    basic := n + 1;
end;

var
    i:integer;
    out : integer;

begin
    i := 10;
    out := basic(i) + basic(i+1);
    write(out, i);
end.