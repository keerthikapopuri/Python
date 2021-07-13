l="the quick brown fox jumps over lazy dog"
for i in range(len(l)):
  for j in range(i+1,len(l),1):
    if l[i]==l[j]:
      l=l.replace(l[j]," ",1)
new=""      
for i in l:
  if i!=" ":
    new=new+str(i)
if len(new)==26:
  print("yes")       