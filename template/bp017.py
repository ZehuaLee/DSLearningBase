#!/usr/bin/env python
#Implement a function to calculate mean of a list variable aa = [10, 20, 40, 80, 30].

def main():
	a = [10, 20, 40, 80, 30]
	print mymean(a)
def mymean(a):
	if isinstance(a, list) == False:
		return "This can' be a right type"
	result = 0.0
	for x in a:
		result = result+x
	return result/len(a)

if __name__ == '__main__':
	main()
