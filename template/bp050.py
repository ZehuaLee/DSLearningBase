#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Make a program, which reads the input file, replaces a string, "programme" with "program" and outputs the resultant text into the screen.

import re
import sys
import os

def main(arg):
    filename = arg[0]
    pattern = re.compile(r'programme')
    if not os.path.exists(filename):
        print '%s not found' % filename
        return -1
    with open(filename, 'r') as file:
        while True:
            strings = file.readline()
            if not strings:
                break
            newString = pattern.sub('program',strings)
            print newString

if __name__ == '__main__':
	main(sys.argv[1:])
