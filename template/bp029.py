#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# Make a program, which prints log1010log10⁡10, log210log2⁡10, ln10ln⁡10 and cos180∘cos⁡180∘ to the screen. To do this, a module "math" is useful.
import math
def main():
	print 'log_10(10)','\t',math.log(10,10)
	print 'log_2(10)\t', math.log(10,2)
	print 'log_e(10)\t', math.log(10,math.e)
	print 'cos(180)\t', math.cos(180/180*math.pi)
if __name__ == '__main__':
	main()
