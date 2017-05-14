#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#Make a program, which randomly samples 10 numbers from integer list variable, [0, 1, 2, ..., 999] (=range(1000)) and prints the sampling numbers.

import numpy as np
def main():
	a = np.random.uniform(0,999,10)
	print a
if __name__ == '__main__':
	main()
