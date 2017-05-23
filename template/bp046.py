#!/usr/bin/env python
import re
import sys
def main(para):
	filename = para[0]
	file = open(filename,'r')
	pattern = re.compile(r'[a-zA-Z]*act[a-zA-Z]*',re.I)
	result = []
	while True:
		rl = file.readline()
		if not rl:
			break
		result.extend(pattern.findall(rl))
	file.close()
	for x in result:
		print x

if __name__ == '__main__':
	main(sys.argv[1:])
