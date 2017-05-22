#!/usr/bin/env python
import sys
import re
def main(para):
	counter = 0
	if isinstance(para[0],str) == False:
		print 'Parameter errors'
		return counter
	filename = para[0]
	f = open(filename, 'r')
	pattern = re.compile(r'\[\d+\]')
	while True:
		rl = f.readline()
		if not rl:
			break
		match = re.search(pattern, rl)
		if match:
			counter = counter+1
	f.close()
	print counter
	return counter


if __name__ == '__main__':
	main(sys.argv[1:])

