#!/usr/bin/env python
# -*- coding:UTF-8 -*-
#Make a program, which generates a numpy matrix variable aa = ⎛⎝⎜4−1121554468⎞⎠⎟(4154−1156248), calculates a determinant and inverse matrix respectively and prints them to the screen.

import numpy as np
def main():
	a = [[4,15,4],[-11,5,6],[2,4,8]]
	b = np.matrix(a)
	print np.linalg.det(b)
	print np.linalg.inv(b)

if __name__ == '__main__':
	main()
