#!/usr/bin/env python
import bp020 as bp
def main():
	a = raw_input("Input a number:")
	if a.isdigit() == False:
		print "Wrong type"
	else:
		print bp.myfibo(int(a))

if __name__ == '__main__':
	main()
