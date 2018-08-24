#!/usr/bin/env python

def slice(ori_list, start, end, step):
    return ori_list[start:end:step]

def g(type):
    if type == 0:
        l = [x*x for x in range(1,101) if x%2==0]
        print l
        l = [m+n for m in 'acdefg' for n in 'ABCDEFG']
        print l 
        m='abcdefg'
        n='ABCDEFG'
        l=[]
        for i in range(0, 7):
            a,b = m[i], n[i]
            l.append(a+b)
        print l
    else:
        l = (x*x for x in range(1, 101) if x%2==0)
        print l
        for n in l:
            print n
        lx = fib(20)
        for i in lx:
            print i
        
def fib(max):
    a, b, c = 0, 1, 0
    while c<max:
        yield b
        a, b = b, a+b
        c = c+1


def is_power_of_2(n):
    if not isinstance(n, int):
        raise TypeError('bad operand')
    if n%2==0:
        return True
    else:
        return False
