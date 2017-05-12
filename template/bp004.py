#!/usr/bin/env python
import bp002 as bp
def cal2(a, b, c):
	return bp.cal((a+b),c)

def main():
	print cal2(9, 7, 4)

if __name__ == '__main__':
	main()
