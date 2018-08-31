#!/usr/bin/env python
# -*- encoding:utf-8 -*-

class stu(object):
	def __init__(self, name, score):
		self.name=name
		self.score=score

	def get_score(self):
		print '%s: %d' % (self.name, self.score)

if __name__=='__main__':
	kevin=stu('Kevin', 100)
	kevin.get_score()
