#!/usr/bin/env python3

# Write a program that simulates random read coverage over a chromosome
# Report min, max, and average coverage
# Make variables for genome size, read number, read length
# Input values from the command line
# Note that you will not sample the ends of a chromosome very well
# So don't count the first and last parts of a chromosome

import sys
import random

gensize = 49
readnum = 10000
readlen = 3
coverage = []

# Filling the coverage with zeros
for i in range(gensize):
	coverage.append(0)

# Random reads
for i in range(readnum):
	r = random.randint(0, gensize-readlen)
	for j in range(readlen):
		coverage[r+j] += 1
		
# print(coverage)
print(min(coverage[readlen:-readlen]), max(coverage[readlen:-readlen]), 
sum(coverage[readlen:-readlen])/(gensize-(2*readlen)))



"""
python3 32xcoverage.py 1000 100 100
5 20 10.82375
"""
