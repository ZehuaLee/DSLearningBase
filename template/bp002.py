#!/usr/bin/env python
def cal(a, n):
	result = 1
	if n > 0:
		for x in range(n):
			result = result*a
	if n < 0:
		for x in range(-1*n):
			result = result/a
	return result


def main():
	print cal(15,9)

if __name__ == '__main__':
	main()
