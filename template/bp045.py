#!/usr/bin/env python
import re
import sys

def main(para):
	filename = para[0]
	file = open(filename,'r')
	pattern = re.compile(r'[a-zA-Z]+://[^\s]*')
	result = []
	while True:
		rl = file.readline()
		if not rl:
			break
		temp = re.findall(pattern,rl)
		result.extend(temp)
	for x in result:
		print x


if __name__ == '__main__':
	main(sys.argv[1:])
