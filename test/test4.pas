const
  fi='';
  fo='';
  mn=100000;
  var
   f:text;
   i,j,n,t:longint;
   a:array[1..mn] of longint;
 
Procedure doc;
  var i,j,tong,m:longint;
   Begin
    m:=0; 
     //read(f,n);
     tong:=0;
     for i:=1 to n do
     Begin
      //read(f,a[i]);
      tong:=tong+a[i];
      if a[i]<>0 then
         inc(m);
     End;
     if tong<100 then Begin
      writeln('NO');
      //exit;
    End;
  tong:=tong-100;
  if tong/m <1 then
    writeln('YES') else
    writeln('NO');
  End;
 
Procedure Input;
 Begin
   assign(f,fi);
   reset(f);
   //read(f,t);
   for i:=1 to t do
    Begin
      doc;
 
    End;
    close(f);
 End;
// Begin
//  Input;
// End.