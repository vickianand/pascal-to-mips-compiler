program record_test;

Type
    Str25    = Array[0..9] of String;
    TBookRec = Record
                Title, Author,
                ISBN  : Str25;
                Price : Real;
               End;
Var
    myBookRec : TBookRec;

Begin
 myBookRec.Title  := 'Some Book';
 myBookRec.Author := 'Victor John Saliba';
 myBookRec.ISBN   := '0-12-345678-9';
 myBookRec.Price  := 25.5;

 Writeln('Here are the book details:');
 Writeln;
 Writeln('Title:  ', myBookRec.Title);
 Writeln('Author: ', myBookRec.Author);
 Writeln('ISBN:   ', myBookRec.ISBN);
 Writeln('Price:  ', myBookRec.Price);
 Readln;
End.