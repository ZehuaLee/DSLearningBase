#!/usr/bin/env python
# -*- coding:UTF-8 -*-
#Make a program, which generates 10 float values (a list variable), which are distributed under N(0,52)N(0,52) and prints it.

import numpy as np
def main():
	mu, sigma = 0, 5
	print np.random.normal(mu,sigma,10)

if __name__ == '__main__':
	main()
