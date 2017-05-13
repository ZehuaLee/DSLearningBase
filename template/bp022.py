#!/usr/bin/env python

#Make a program, which generates a list variable aa = [10, 20, 40, 80, 30] and calculates sum of all elements in the list by a package "numpy".
import numpy as np
def main():
	a = [10,20,40,80,30]
	b = np.array(a)
	print b.sum()

if __name__ == '__main__':
	main()
