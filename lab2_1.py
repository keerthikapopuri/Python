a=int(input("enter 1st number:"))
b=int(input("enter 2nd number:"))
if a<b:
    t=a
    a=b
    b=t
    
for i in range(2,a+1,1):
    c=0
    if(a%i==0 and b%i==0):
        c=i
        break
if c==0:
    res=a*b
    print(res)
else:
    print(c)    
