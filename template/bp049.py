#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# Make a program, which reads the input file, counts the number of occurrences of "America", "British Columbia", "Canada", "Okanagan", "UBC" and "Vancouver" respectively (Count exact match and do not count "American", "Canadas" or etc!!), draws a bar graph for the counts (Y-axis: The number of counts, X-axis: each value) and outputs it as png image file.

import re
import sys
import os
from matplotlib import pyplot as plt
import numpy as np

def main(para):
    filename = para[0]
    if not os.path.exists(filename):
        print '%s not found' % filename
        return -1
    Categ = ['America', 'British Columbia', 'Canada', 'Okanagan', 'UBC', 'Vancouver']
    non_s = r'[;,\.\s\(\)\:\'\"]\s?'

    pa_strings = re.compile(non_s)
    Stat_Val = [0, 0, 0, 0, 0, 0]
    Categ_re = []
    pa_America = re.compile(r'America$')
    pa_British = re.compile(r'^British$')
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
    with open(filename, 'r') as file:
        while True:
            dataline = file.readline()
            if not dataline:
                break
            strings = pa_strings.split(dataline)
            for i in range(len(strings)):
                if strings[i] == 'British' and strings[i+1]!='Columbia':
                    print strings[i], strings[i+1]
                for j in range(len(Categ_re)):
                    if Categ_re[j].match(strings[i]):
                        Stat_Val[j] +=1
    index = np.arange(len(Stat_Val))
    result = plt.bar(index, Stat_Val)
    plt.xticks(index+0.4, Categ)
    plt.show()

if __name__ == '__main__':
    main(sys.argv[1:])
