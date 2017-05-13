#!/usr/bin/env python
#Make a program, which generates a list variable aa = [10, 20, 40, 80, 30] and finds an index of minimum value (argmin) of the list by numpy.

import numpy as np
def main():
	a = [10, 20, 40, 80, 30]
	b = np.array(a)
	print b.min()

if __name__ == '__main__':
	main()
