#!/usr/bin/env python
#Make a program, which generates a two dimensional list variable aa, which contains 100 of list [0, 1, 2, ..., 19] (=range(20)) inside and prints it to the screen.
def main():
	a = [[x for x in range(20)] for y in range(100)]
	for x in range(100):
		print a[x]
if __name__ == '__main__':
	main()
