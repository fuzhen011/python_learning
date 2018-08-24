#!/usr/bin/env python
# -*- coding: utf-8 -*-
s='包含中文的str'

print 'original s=', s

print u'中文'
print u'中'
print u'\u4e2d'

print ''
print(ord('A'))

print('%2d-%02d' % (3, 1))
print('%.2f' % 3.1415926)

# Exercises
s1 = 72
s2 = 85
r = float(s2-s1)/s1
print('Increased by %.2f%%' % r)
