#!/usr/bin/env python
#Implement a function to calculate the Fibonacci numbers. Print 10th Fibonacci number to the screen.

def main():
	n = 13
	print myfibo(n)

def myfibo(n):
	a1 = 0
	a2 = 1
	for x in xrange(n):
		temp = a1
		a1 = a2
		a2 = a2 + temp
	return a1

if __name__ == '__main__':
	main()
