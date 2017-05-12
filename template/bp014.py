#!/usr/bin/env python
#Make a program, which generates a list variable aa = [10, "20", 40, "80", 30]
# and prints only numerical values from all elements.
# In this time, use "for" and "if" functions.

def main():
	a = [10, '20', 40, '80', 30]
	for x in a:
		if isinstance(x, int) or isinstance(x, float) or isinstance(x, long):
			print x

if __name__ == '__main__':
	main()
