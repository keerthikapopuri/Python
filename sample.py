s=input()
c=0
n=len(s)
for i in range(1,n,1):
    for j in range(0,n-1,1):
        new=s[j:j+i+1]
        if new==new[::-1]:
            a=len(new)
            if a>c:
                c=a
print(c)            
