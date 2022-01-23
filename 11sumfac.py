#!/usr/bin/env python3

# Write a program that computes the running sum from 1..n (if n = 5, then sum = 1+2+3+4+5)
# Also, have it compute the factorial of n while you're at it
# No, you may not use math.factorial()
# Use the same loop for both calculations

n = 5
runningSum = 0
factorial = 1

# your code goes here
for i in range(1, n+1):
	runningSum += i
	factorial *= i
print(n, runningSum, factorial)
"""
python3 11sumfac.py
5 15 120
"""
