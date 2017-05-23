#!/usr/bin/env python
import re
import sys
import os

def main(para):
	filename = para[0]
	pattern = re.compile(r'(\d{1,3}(\d*,)+(?:\d{2}5|\d{2}0))')
	result = []
	with open(filename,'r') as file:
		if not os.path.exists(filename):
			print '%s is not found' % filename
		while True:
			linedata = file.readline()
			if not linedata:
				break
			result.extend([x.group() for x in pattern.finditer(linedata)])
		for x in result:
			print x

if __name__ == '__main__':
	main(sys.argv[1:])
