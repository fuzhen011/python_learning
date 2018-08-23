#!/usr/bin/env python

def power(x, n):
    if (not isinstance(x, (int, float))) or (not isinstance(n, (int))) :
        raise TypeError('bad operand type')
    sum=1
    for i in range(n):
        sum = sum*x
    return sum

def calc(*numbers):
    num=0
    for n in numbers:
        num = num + n*n
    return num
