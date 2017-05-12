#!/usr/bin/env python
# Implement a function to calculate summation of a list variable aa = [10, 20, 40, 80, 30].



def main():
	a = [10, 20, 40, 80, 30]
	print (mysum(a))

def mysum(a):
	summ = 0
	if isinstance(a,list) == False:
		return "parameter should be a list"
	if len(a) == 0:
		return 0
	for x in a:
		summ = summ+x
	return summ

if __name__ == '__main__':
	main()
