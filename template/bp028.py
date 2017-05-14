#!/usr/bin/env python
#Make a program, which generates a list variable aa = [35, 41, 21, 14, 6, 2, 0, 2] and draws a bar plot with aa as horizontal axis

from matplotlib import pyplot as plt
import numpy as np
def main():
	a = [35,41,21,14,6,2,0,2]
	b = ['A','B','C','D','E','F','G','H']
	index = np.arange(8)
	#bar_width = 0.35
	result = plt.bar(index, a)
	plt.xticks(index, b)
	plt.show()
if __name__ == '__main__':
	main()
