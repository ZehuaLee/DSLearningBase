#!/usr/bin/env python
#Make a program, which generates a two dimensional list variable aa, which contains 100 of list [0, 1, 2, ..., 19] (=range(20)) inside and calculates sum of all elements in the list.
def main():
	a = [[x for x in range(20)] for y in range(100)]
	b = 0
	for y in range(len(a)):
		for x in range(len(a[y])):
			b = b + a[y][x]
	print b

if __name__ == '__main__':
	main()
