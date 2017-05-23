#!/usr/bin/env python
# -*- coding:UTF-8 -*-
#Make a program, which reads the input file, counts the number of occurrences of "America", "British Columbia", "Canada", "Okanagan", "UBC" and "Vancouver" respectively (Count exact match and do not count "American", "Canadas" or etc!!), draws a bar graph for the counts (Y-axis: The number of counts, X-axis: each value) and outputs it as png image file.

import re
import sys
import os
import matplotlib as plt

def main(para):
	filename = para[0]
	if not os.path.exists(filename):
		print '%s not found' %filename
		return -1
	Categ = ['America','British Columbia','Canada','Okanagan','UBC','Vancouver']
	Stat_Val = [0,0,0,0,0,0]
	Categ_re = []
	pa_America = re.compile(r'^America$')
	pa_British = re.compile(r'^British\ Columbia$')
	pa_Canada = re.compile(r'^Canada$')
	pa_Okanagan = re.compile(r'^Okanagan$')
	pa_ubc = re.compile(r'^UBC$')
	pa_van = re.compile(r'^Vancouver$')
	Categ_re.append(pa_America)
	Categ_re.append(pa_British)
	Categ_re.append(pa_Canada)
	Categ_re.append(pa_Okanagan)
	Categ_re.append(pa_ubc)
	Categ_re.append(pa_van)
	

if __name__ == '__main__':
	main(sys.argv[1:])
