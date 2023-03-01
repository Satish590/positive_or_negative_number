#there are three methods to describe
#given number is positive or negative
# lets descuess one by one
# 1 st method is brute force method
n = int(input())
if n > 0:
    print('entered number is positive')
elif n == 0:
    print('entered number is zero')
else:
    print('entered number is negative')

#2nd method nested if-else statement
if n >= 0:
    if n == 0:
        print('entered number is zero')
    else:
        print('entered number is positive')
else:
    print('entered number is negative')

#using ternary operartor

print('entered number is positive' if n >= 0  else "entered number is negative")