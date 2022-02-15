#!/usr/bin/env python3

# Write a program that computes typical stats
# Count, Min, Max, Mean, Std. Dev, Median
# No, you cannot import the stats library!

import sys
import math

numList = []
for i in range (1, len(sys.argv)): numList.append(int(sys.argv[i]))
numList.sort()

min = numList[0]
max = numList[len(numList)-1]
count = len(numList)
mid = 0
sum = 0

for i in range(len(numList)):
	sum += numList[i] # will divide this by the length of the list to get the mean 	

if len(numList) % 2 == 0: mid = numList[len(numList)/2] + numList[len(numList)/2-1]
else: mid = numList[len(numList)//2]

avg = sum/len(numList)	

stdnum = 0

for i in range(len(numList)):
	stdnum += (numList[i] - avg)**2

std = math.sqrt(stdnum/len(numList))

print("Count: "f'{count}')
print("Minimum: "f'{min:.1f}')
print("Maximum: "f'{max:.1f}')
print("Mean: " f'{avg:.3f}')
print("Std. dev: " f'{std:.3f}')
print("Median: " f'{mid:.3f}') #this doesn't work because you have to order the list


"""
python3 30stats.py 3 1 4 1 5
Count: 5
Minimum: 1.0
Maximum: 5.0
Mean: 2.800
Std. dev: 1.600
Median 3.000
"""
