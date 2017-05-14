#!/usr/bin/env python
# -*- coding:UTF-8 -*-
#Make a program, which generates a numpy matrix variable aa = ⎛⎝⎜⎜⎜3111421111214112⎞⎠⎟⎟⎟(3414121111211112), calculates eigenvalues and eigenvectors for aa and prints them to the screen.

import numpy as np
def main():
	a = [[3,4,1,4],[1,2,1,1],[1,1,2,1],[1,1,1,2]]
	b = np.matrix(a)
	print np.linalg.eig(b)

if __name__ == '__main__':
	main()
