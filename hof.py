#!/usr/bin/env python
# -*- encode: utf-8 -*-

import functools

def str2num(s):
    def char2num(s):
        #l = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
        #i=l[s]
        # print i 
        i = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
        return i
    def fn(x, y):
        return x*10+y
    return reduce(fn, map(char2num, s))

def test(s):
    print str2num(s)


def to_int(s, base=2):
    def char2num(s):
        #l = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
        #i=l[s]
        # print i
		i = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15, 'A': 11, 'B': 12, 'C': 13, 'D': 14, 'E': 15, 'F': 16}[s]
		return i
    def fn(x, y):
        return x*base+y
    return reduce(fn, map(char2num, s))

def test(s):
    print to_int(s)

int2 = functools.partial(to_int, base=2)
int8 = functools.partial(to_int, base=8)
int10 = functools.partial(to_int, base=10)
int16 = functools.partial(to_int, base=16)

def to_ints():
	print int2('10010100101')
	print int8('3782116')
	print int10('2350127517250')
	print int16('88c8a6dddf')

# Exercises
# Align the chacters to 'Xxxxx' format (first UPPER then lower)

#def format(s):

def sushu_filter():
	def no_sushu(n):
		for i in range(2, n):
			if n%i==0:
				return 1
		return 0

	l=filter(no_sushu, range(1, 101))
	print l		

			

























