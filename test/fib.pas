
program fibonacci;

function fib(n:integer): integer;
begin
    if (n <= 2) then
        fib := 1
    else
        fib := fib(n-1) + fib(n-2);
end;

var
    i:integer;
    out : integer;

begin
    for i := 1 to 11 do
    begin
        out := fib(i);
        writeln(out);
        writeln('=');
    end;
end.
