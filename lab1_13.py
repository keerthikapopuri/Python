n=int(input("enter number : "))
count=0
for i in range(2,n-1,1) :
    if n%i==0 :
        count=count+1

if count==0 :
    print(n,"is prime")
else :
    print(n,"is composite")    