#!/usr/bin/env python
import re
import sys
import os
def main(para):
	filename = para[0]
	if not os.path.exists(filename):
		print '%s not found' % filename
		return None
	result = []
	counter = 0
	#pattern = re.compile(r'[a-zA-Z]*\$[0-9]*,?[0-9]*\.[0-9]')\\\\\|()
	pattern = re.compile(r'[a-zA-Z]*\$\d+,?\d*\.\d+|[a-zA-Z]*\$\d+,?\d*')
	with open(filename,'r') as file:
		while True:
			data = file.readline()
			if not data:
				break
			temp = pattern.findall(data)
			for x in temp:
				if (x.find('CAD')== -1):
					#print x
					counter = counter+1
	print counter


if __name__ == '__main__':
	main(sys.argv[1:])