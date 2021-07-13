n=int(input("enter the number of terms : "))
a=0
b=1
print(a,b,end=" ")
for i in range(3,n+1,1) :
    c=a+b
    print(c,end=" ")
    a=b
    b=c
