#!/usr/bin/env python
#Make a program, which generates a list variable aa = [0, 2, 6, 8, 9, 10, 14, 16] and bb = [35, 41, 21, 14, 6, 2, 0, 2] and draws a scatter plot with aa as horizontal and bb as vertical axis. To do this, a module "matplotlib" is useful.


import matplotlib
#matplotlib.use('pygtk')#for windows, it should be no value
import matplotlib.pyplot as plt

def main():
	lia = [0, 2, 6, 8, 9, 10, 14, 16]
	lib = [35, 41, 21, 14, 6, 2, 0, 2]
	plt.plot(lia,lib)
	plt.xlabel('ordinate')
	plt.ylabel('abscissa')
	plt.show()
	print "x"
if __name__ == '__main__':
	main()
