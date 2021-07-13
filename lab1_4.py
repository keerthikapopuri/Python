import math
a=int(input('enter a'))
b=int(input('enter b'))
c=int(input('enter c'))
d=(b*b)-(4*a*c)
if d>0 :
    print("real and distinct roots")
    r1=(-b)+(math.sqrt(d/(2*a)))
    r2=(-b)-(math.sqrt(d/(2*a)))
    print(r1,r2)

if d==0 :
    print(" real and same roots") 
    r1=-b/(2*a)
    print(r1)

else :
     print("roots are complex")
   
