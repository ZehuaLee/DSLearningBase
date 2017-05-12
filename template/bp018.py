#!/usr/bin/env python
#Implement a function to calculate mean of a list variable aa = [10, 20, 40, 80, 30].
import bp017 as bp

def main():
	a = [10,20,40,80,30]
	print (myvariance(a))

def myvariance(a):
	b = bp.mymean(a)
	summ = 0
	for x in a:
		summ = summ + (b-x)*(b-x)
	return summ/len(a)
if __name__ == '__main__':
	main()
