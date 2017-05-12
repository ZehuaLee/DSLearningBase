#!/usr/bin/env python

## Make a program,
# which generates a dictionary variable aa = {"January":1, "February":2, "May":5}
# and prints keys of aa sorted by value of the dictionary in descending order.
# In this time, use "for" function.

def main():
	a = {"January":1,"February":2,"May":5}
	items = a.items()
	invItems = [[v[1],v[0]] for v in items]
	invItems.sort(reverse = True)
	for x in invItems:
		print x[1]

if __name__ == '__main__':
	main()
