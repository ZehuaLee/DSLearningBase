#!/usr/bin/env python

#
def main():
	a = {"January":1,"February":2,"May":5}
	items = a.items()
	invItems = [[v[1],v[0]] for v in items]
	invItems.sort(reverse = True)
	for x in invItems:
		print x[1]

if __name__ == '__main__':
	main()
