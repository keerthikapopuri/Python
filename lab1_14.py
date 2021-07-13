a=int(input("enter 1st number : "))
b=int(input("enter 2nd number : "))
for i in range(a,b,1) :
    count=0
    for j in range(2,i,1) :
        if i%j==0 :
            count=count+1

    if count==0 :
        print(i,end=' ')  
          
        

    
