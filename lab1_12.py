a=int(input('enter year: '))
if (a%100==0)or(a%4==0)or(a%400==0) :
    print(a,' is a leap year')

else :
    print(a,' is not a leap year')    