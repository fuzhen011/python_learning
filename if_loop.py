#!/usr/bin/env python

age=int(raw_input('Input the birth year: '))
if age<1980:
    print '70 hou or older'
elif age>=1980 and age<1990:
    print '80 hou'
elif age>=1990 and age<2000:
    print '90 hou'
else:
    print '00 hou'

# for in loop
sum = 0
for i in range(101):
    sum = sum + i
print sum

# while loop
sum = 0
n = 100
while n>0:
    sum = sum + n
    n = n -1
print sum
