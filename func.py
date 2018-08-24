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

def person(name, age, **kw):
    print 'name', name, 'age', age, 'other:', kw

def fact(n):
    if not isinstance(n, (int)):
        raise TypeError('bad oprand type')
    if n==1:
        return 1
    return n*fact(n-1)
