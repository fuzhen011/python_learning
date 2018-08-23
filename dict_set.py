#!/usr/bin/env python

d1 = {'Michael':95, 'Bob':75, 'Tracy':85}
print d1['Michael']
d1['Adam'] = 67
d1['Jack'] = 90
print d1['Jack']
d1['Jack'] = 88
print d1['Jack']

# set
s = set([1, 3, 4])
print s
s.add(2)
print s
s.remove(4)
print s
s1 = set([2, 3, 5])
print 's&s1 =', s&s1
print 's|s1 =', s|s1
