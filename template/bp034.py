#!/usr/bin/env python
#Make a program, which generates a numpy matrix variable aa = (10301525)(10153025) and prints the second column of it to the screen.

import numpy as np
def main():
	a = [[10,15],[30,25]]
	a = np.matrix(a)
	print [a[0,1],a[1,1]]

if __name__ == '__main__':
	main()
