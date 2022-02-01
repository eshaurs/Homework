#!/usr/bin/env python3

# Write a program that computes the GC% of a DNA sequence
# Format the output for 2 decimal places
# Use all three formatting methods

# Worked on this in class with everyone.

dna = 'ACAGAGCCAGCAGATATACAGCAGATACTAT' # feel free to change
gc = 0 # represents the gc count

# fun fact: exons tend to be GC rich. It's because the most common amino acids are GC rich.

for i in range(0, len(dna)):
	if   dna[i] == 'G': gc += 1
	elif dna[i] == 'C': gc += 1
	fgc = gc/len(dna)
	
print('%.2f'% fgc)  # see 13text to format the answer more correctly. 
print(f'{fgc:.2f}')
print('{:.2f}'.format(fgc))

"""
python3 21gc.py
0.42
0.42
0.42
"""
