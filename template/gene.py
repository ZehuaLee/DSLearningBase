#!/usr/bin/env python
# -*- coding:utf-8 -*-
# For this problem, use the file s001.txt. Make a program, which counts singlet (A, C, G, T) doublet (AA, AC, ..., TT) and triplet (AAA, AAC, ..., TTT) characters in the file and prints the result to the screen.

import re
import sys
import os

def main(para):
    filename = para[0]
    if not os.path.exists(filename):
        print 'file path error.'
        exit(-1)
    ATGC = ['A','T','G','C']
    ATGCs = []
    ATGCCount = []
    for x in ATGC:
        ATGCs.append(x)

    for x in ATGC:
        for y in ATGC:
            ATGCs.append(x+y)

    for x in ATGC:
        for y in ATGC:
            for z in ATGC:
                ATGCs.append(x+y+z)
    ATGC_dic = {}
    ATGCCount = [0 for x in range(len(ATGCs))]
    for index, item in enumerate(ATGCs):
        ATGC_dic[item] = 0
    with open(filename,'r') as file:
        while True:
            strings = file.readline()
            if not strings:
                break
            strings = strings[0:-1]
            for i in range(len(strings)):
                ATGC_dic[strings[i]] += 1
                if len(strings) - i > 1:
                    ATGC_dic[strings[i:i+2]] += 1
                if len(strings) - i > 2:
                    ATGC_dic[strings[i:i+3]] += 1
    for x in ATGCs:
        print x, '\t', ATGC_dic[x]


if __name__ == '__main__':
    main(sys.argv[1:])
