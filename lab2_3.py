
import math
def binary(d):
    i=0
    binary=0
    while d!=0:
        rem=d%2
        binary=binary+rem*math.pow(10,i)
        d=d//2
        i=i+1
    print("the binary number is :",int(binary))

def octal(d):
    i=0
    octal=0
    while d!=0:
        rem=d%8
        octal=octal+rem*math.pow(10,i)
        d=d//8
        i=i+1
    print("the octal number is :",octal)

def hexadecimal(d):
    i=0
    hex=0
    while d!=0:
        rem=d%16
        hex=hex+rem*math.pow(10,i)
        d=d//16
        i=i+1
    print("the hexadecimal number is :",hex)

d=int(input("enter the decimal number :"))
print("1.convert into binary")
print("2.convert into octal")
print("3.convert into hexadecimal")
choice=int(input("enter a choice:"))
if choice==1:
    binary(d)
if choice==2:
    octal(d)
if choice==3:
    hexadecimal(d)    



       