#!/usr/bin/env python
#Make a program, which generates a numpy matrix variable aa = (10301525)(10153025) and prints it to the screen.

import numpy as np
def main():
	a = [[10, 15], [30,25]]
	b = np.matrix(a)
	print b

if __name__ == '__main__':
	main()
