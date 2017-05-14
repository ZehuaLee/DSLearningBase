#!/usr/bin/env python
#Make a program, which generates a two dimensional list variable aa, which contains 100 of list [0, 1, 2, ..., 19] (=range(20)) inside and one dimensional list variable bb = [0, 1, 2, ..., 9], merge them (aa and bb) and prints the resultant list to the screen. For this, "append" function is useful.
def main():
	a = [[x for x in range(20)] for y in range(100)]
	b = range(10)
	a.append(b)
	for x in a:
		print x

if __name__ == '__main__':
	main()
