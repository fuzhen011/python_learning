#!/usr/bin/env python

print '10/3 =', 10/3, '10.0/3=', 10.0/3

# Escape chacter
print('I\'m ok')
print('I\'m learning\nPython.')
# Use r'' to declare the chacters inside '' are not escaped.
print(r'/n/r/a///')
# Use '''...''' to print multiple lines
print('''line1
line2
line3
...''')
print(r'''hello,\n
world''')
# Dynamic language
a = 100
print(a)
a = 'axxc'
print(a)

# Exercises
# -*- coding: utf-8 -*-
n = 123
f = 456.789
s1 = 'Hello, world'
s2 = 'Hello, \'Adam\''
s3 = r'Hello, "Bart"'
s4 = r'''Hello,
Lisa!'''

print(n)
print(f)
print(s1)
print(s2)
print(s3)
print(s4)
