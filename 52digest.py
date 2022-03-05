#!/usr/bin/env python3
# 52digest.py

import re
import sys

# Write a program that performs an EcoRI digest on the SARS-COV2 genome
# The program should have 2 arguments
#    1. The genome file
#    2. The restriction pattern
# The output should be the sizes of the restriction fragments

# Try and figure out how to skip all the bs until you get to origin. 
# Maybe make a variable that tells you if you've seen the origin.

filename = sys.argv[1]
# pattern = sys.argv[2]


	
	


def readGenomeFile(filename):
	seq = ''
	isOrigin = False
	with open(filename) as fp:
		for line in fp.readlines():
			line = line.rstrip()
			if 'ORIGIN' in line: 
				isOrigin = True
				continue
			if isOrigin: 
				nts = line.split()
				for i in range(1, len(nts)):
					seq += nts[i]
	return seq

genome = readGenomeFile(sys.argv[1])
last = 0
for match in re.finditer(sys.argv[2], genome):
	print(match.start()-last)
	last = match.start()
print(len(genome)-last)
"""
python3 52digest.py ../Data/sars-cov2.gb gaattc
1160
10573
5546
448
2550
2592
3569
2112
1069
"""
