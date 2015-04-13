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
    // for i := 1 to 16 do
        write(fib(11));
        // out := fib(i);
    // write('...');
    // out := -111;
end.


// fib
// ['label_1', '', '', 'label']
// ['t3', 2, '', ':=']
// ['t4', 't1', 't3', 'int<=']
// ['label_3', 't4', '', 'IF_FALSE_GOTO']
// ['t5', 1, '', ':=']
// ['t2', 't5', '', ':=']
// ['label_4', '', '', 'GOTO']
// ['label_3', '', '', 'label']
// ['t6', 1, '', ':=']
// ['t7', 't1', 't6', 'int-']
// ['', 4, '', 'SET_PARAM_OFFSET_WIDTH']
// ['t7', '', '', 'PARAMS']
// ['label_1', '', '', 'CALL_FUNCTION']
// ['t9', 2, '', ':=']
// ['t10', 't1', 't9', 'int-']
// ['', 4, '', 'SET_PARAM_OFFSET_WIDTH']
// ['t10', '', '', 'PARAMS']
// ['label_1', '', '', 'CALL_FUNCTION']
// ['t12', 't8', 't11', 'int+']
// ['t2', 't12', '', ':=']
// ['label_4', '', '', 'label']
// ['', '', '', 'FUNC_RETURN']
// root
// ['t15', 1, '', ':=']
// ['t16', 16, '', ':=']
// ['t13', 't15', '', ':=']
// ['label_5', '', '', 'label']
// ['t17', 't13', 't16', '<=']
// ['label_6', 't17', '', 'IF_FALSE_GOTO']
// ['', 4, '', 'SET_PARAM_OFFSET_WIDTH']
// ['t13', '', '', 'PARAMS']
// ['label_1', '', '', 'CALL_FUNCTION']
// ['t14', 't18', '', ':=']
// ['t13', 't13', 1, 'int+']
// ['label_5', '', '', 'GOTO']
// ['label_6', '', '', 'label']
// ['t19', 111, '', ':=']
// ['t20', 0, 't19', '-']
// ['t14', 't20', '', ':=']

