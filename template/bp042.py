#!/usr/bin/env python
# -*- coding:UTF-8 -*-
#Make a program, which generates 10×1010×10 dimensional numpy matrix aa filled by random numbers between 0 and 1 ([0,1][0,1]) and prints it.

import numpy as np
def main():
	a = [np.random.uniform(0,1,10) for x in range(10)]
	a = np.matrix(a)
	print a
if __name__ == '__main__':
	main()
