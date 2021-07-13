import math
n=int(input("enter the number : "))
sum=0
k=n
while n!=0 :
    r=n%10
    sum=sum+math.pow(r,3)
    n=n//10
if sum==k :
    print(k," is a armstrong number")
else :
    print(k," is not a armstrong number")    