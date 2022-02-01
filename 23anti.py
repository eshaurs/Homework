#!/usr/bin/env python3

# Write a program that prints the reverse-complement of a DNA sequence
# You must use a loop and conditional

# Worked on with Majken on 01/30 and a large group of people in office hours on 01/31

dna = 'ACTGAAAAAAAAAAA'
compDNA = ''

for i in range(len(dna)-1, -1, -1):
	if dna[i] == 'A': compDNA += 'T'
	elif dna[i] == 'T': compDNA += 'A'
	elif dna[i] == 'G': compDNA += 'C'
	else: compDNA += 'G'
	
print(compDNA)

"""
python3 23anti.py
TTTTTTTTTTTCAGT
"""
