a=int(input('Enter the first number : '))
b = int(input('Enter second number : '))
c=int(input('Enter the third number:'))

if(a<b and a<c):
    print('The smallest number is :',a)
elif(b<a and b<c):
    print('The smallest number is :',b)
else:
    print('The smallest number is :',c)
