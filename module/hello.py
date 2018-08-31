#!/usr/bin/env python
# -*- encoding=utf-8 -*-

__author__ = 'Kevin Fu'

import sys

def test():
	args = sys.argv
	print 'length of arguments = ', len(args)
	if len(args)==1:
		print 'Hello world.'
	elif len(args)==2:
		print 'Hello %s!' %args[1]
	else:
		print 'Error: too many arguments!'

if __name__=='__main__':
	test()
