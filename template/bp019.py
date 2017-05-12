#!/usr/bin/env python
#Implement a function to calculate a (unbiased estimated) standard deviation of a list variable aa = [10, 20, 40, 80, 30].

import bp018 as bp
import math
def main():
	aa = [10, 20, 40, 80, 30]
	print mysd(aa)

def mysd(a):
	if isinstance(a, list)==False:
		return "fatel type error"
	var = bp.myvariance(a)
	return math.sqrt(var)

if __name__ == '__main__':
	main()
