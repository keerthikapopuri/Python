name=input("enter string:")
string=name.split(", ")
for i in range(len(string)-1):
      if string[i]>string[i+1]:
        str=string[i]
        string[i]=string[i+1]
        string[i+1]=str 
new=" ".join(string)
print(new)