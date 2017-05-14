#!/usr/bin/env python
# -*- coding:UTF-8 -*-
#Make a program, which generates a numpy matrix variable aa = ⎛⎝⎜⎜⎜3111421111214112⎞⎠⎟⎟⎟(3414121111211112), calculates eigenvalues and eigenvectors for aa and prints them to the screen.

import math
import numpy as np
def main():
	a = [[3, 4, 1, 4], [1, 2, 1, 1], [1, 1, 2, 1], [1, 1, 1, 2]]
	a = np.matrix(a)
	d = np.linalg.eig(a)[0]
	d_a = [[ 0 for x in range(len(d))] for y in range(len(d))]
	for x in range(len(d)):
		d_a[x][x] = math.sqrt(d[x])
	d_a = np.matrix(d_a)
	p = np.linalg.eig(a)[1]
	p_i = np.linalg.inv(p)
	D = p*d_a*p_i
	print D
if __name__ == '__main__':
	main()
