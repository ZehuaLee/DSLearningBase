#!/usr/bin/env python
# -*- coding:UTF-8 -*-
#Make a program, which generates a numpy matrix variable aa = (10301525)(10153025) and bb = (4−11155)(415−115), calculates an element-wise product of aa and bb and prints the product to to the screen.
import numpy as np
def main():
	a = [[10,15],[30,25]]
	b = [[4,15],[-11,5]]
	# a = [[1,1],[2,2]]
	# b = [[1,1],[2,2]]
	a = np.matrix(a)
	b = np.matrix(b)
	print np.multiply(a,b)
	#print a*b
if __name__ == '__main__':
	main()
