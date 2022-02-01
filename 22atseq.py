#!/usr/bin/env python3

import random
random.seed(1) # comment-out this line to change sequence each time

# Write a program that stores random DNA sequence in a string
# The sequence should be 30 nt long
# On average, the sequence should be 60% AT
# Calculate the actual AT fraction while generating the sequence
# Report the length, AT fraction, and sequence

# create a variable for the DNA
# every time I go through the loop, I need to add an AT or a GC 

# Worked on this in class with everyone.

dna = ''
atCount = 0

for i in range(30):
	if random.random() > 0.6:  # why this fraction?
		if random.random() > 0.5: dna += 'G'
		else: dna += 'C'
	else: 
		if random.random() > 0.5: dna += 'A'
		else: dna += 'T'
		atCount += 1  #AT specifically or A's and T's?
		
print(len(dna),atCount/len(dna), dna) #it doesn't have to be the bottom seq specifically, right?

"""
for i in range(10):
	print(random.random())
"""


"""
python3 22atseq.py
30 0.6666666666666666 ATTACCGTAATCTACTATTAAGTCACAACC
"""
