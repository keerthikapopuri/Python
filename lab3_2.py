string=input("enter a string:")
index=0
for i in range(len(string)):
    if not((string[i]>='a' and string[i]<='z') or (string[i]>='A' and string[i]<='Z') or (string[i]>='1' and string[i]<='9')):
        print(string[index:i],end=" ")
        index=i+1

