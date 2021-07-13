a=int(input("enter the first number:"))
b=int(input("enter the 2nd number: "))
if a<b:
    t=a
    a=b
    b=t
for i in range(1,a+1,1):
    if a%i==0 and b%i==0:
        greater=i
print(greater)            
