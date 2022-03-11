#!/usr/bin/env python3
# 61dust.py

import argparse
import mcb185
import math

# Write a program that finds and masks low entropy sequence
# Use argparse for the following parameters
#   sequence file
#   window size
#   entropy threshold
#   lowercase or N-based masking
# The program should output a FASTA file (but with Ns or lowercase)
# Use argparse
# Use the mcb185.read_fasta() function
# Put more functions in your mcb185.py library

parser = argparse.ArgumentParser(description='Finds and masks low entropy sequence.')

parser.add_argument('fasta', type=str,
	metavar='<str>', help='required sequence file')
parser.add_argument('--win', required=False, type=int, default=11,
	metavar='<int>', help='window size [%(default)i]')
parser.add_argument('--threshold', required=False, type=float, default=1.5,
	metavar='<float>', help='entropy threshold [%(default).3f]')
parser.add_argument('--N', action='store_true',
	help='switching to N-based masking, the default is lowercase.')
	
# takes a fasta file in, and then a fasta file comes out (with the appropriate
# letters made lowercase)
arg = parser.parse_args()

#seq = 'ATGCGTAGCGAAAAAAGCT'

def letterCount(seq):
	probs = {}
	for i in range(len(seq)):
		letter = seq[i] 
		if letter not in probs: probs[letter] = 0
		probs[letter] += 1
	for letter in probs:
		probs[letter] /= len(seq)
	return probs.values() # not returning the whole dictionary.

def entropy(probs):
	assert(math.isclose(sum(probs), 1.0))
	h = 0
	for p in probs:
		h += p * math.log2(p)
	return -h
	
# also need to add arg parse to provide options regarding the output sequence
outputSeq = ''
for name, seq in mcb185.read_fasta(arg.fasta):
	seq = seq.upper()
	for i in range(0, len(seq)):
		piece = seq[i:i+arg.win]
		probs = letterCount(piece)
		if entropy(probs) >= arg.threshold: 
			outputSeq += seq[i]
		else: 
			if arg.N: outputSeq += 'N'
			else: outputSeq += seq[i].lower()
	print(f'>{name}')
	for i in range(0, len(outputSeq), 60):
		print(outputSeq[i:i+60])
