#!/usr/bin/env python
## Implement a function to sort input list variable aa = [10, 20, 40, 80, 30] in descending order.

def main():
	a = [10, 20, 40, 80, 30]
	print (mysort(a))

def mysort(a):
	if isinstance(a,list) == False:
		return "wrong type"
	a.sort(reverse=True)
	return a

if __name__ == '__main__':
	main()
