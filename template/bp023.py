#!/usr/bin/env python
#Make a program, which generates a list variable aa = [10, 20, 40, 80, 30] and calculates mean of all elements in the list by numpy.

import numpy as np
def main():
	a = np.array([10,20,40,80,30])
	print a.mean()

if __name__ == '__main__':
	main()
