#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#Make a program, which generates a numpy matrix variable aa = (10301525)(10153025), calculates sum, mean, variance and standard deviation of the elements and prints them to the screen.
import numpy as np
def main():
	a = [[10,15],[30,25]]
	a = np.array(a)

	print "sum \t",np.sum(a)
	print 'mean \t',np.mean(a)
	print 'var \t',np.var(a)
	print 'std \t',np.std(a)
if __name__ == '__main__':
	main()
