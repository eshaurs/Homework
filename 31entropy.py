#!/usr/bin/env python3

# Write a Shannon entropy calculator: H = -sum(pi * log(pi))
# The values should come from the command line
# E.g. python3 entropy.py 0.4 0.3 0.2 0.1
# Put the probabilities into a new list
# Don't forget to convert them to numbers

import math
import sys

numList = []
for i in range (1, len(sys.argv)): numList.append(float(sys.argv[i]))

sum = 0

for num in numList:
	sum += num * math.log2(num) # we're not using pi 

print(-sum)

"""
python3 31entropy.py 0.1 0.2 0.3 0.4
1.846
"""
