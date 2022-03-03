#!/usr/bin/env python3

import sys

# Write a program that predicts if a protein is trans-membrane
# Trans-membrane proteins have the following properties
#	Signal peptide: https://en.wikipedia.org/wiki/Signal_peptide
#	Hydrophobic regions(s): https://en.wikipedia.org/wiki/Transmembrane_protein
#	No prolines in hydrophobic regions (alpha helix)
# Hydrophobicity is measued via Kyte-Dolittle
#	https://en.wikipedia.org/wiki/Hydrophilicity_plot
# For our purposes:
#	Signal peptide is 8 aa long, KD > 2.5, first 30 aa
#	Hydrophobic region is 11 aa long, KD > 2.0, after 30 aa
# Hints:
#   Create a function for KD calculation
#   Create a function for amphipathic alpha-helix


def kdCalc(aaSeq):
	kd = 0
	for aa in aaSeq:
		if aa == 'I': kd += 4.5
		if aa == 'V': kd += 4.2
		if aa == 'L': kd += 3.8
		if aa == 'F': kd += 2.8
		if aa == 'C': kd += 2.5
		if aa == 'M': kd += 1.9
		if aa == 'A': kd += 1.8
		if aa == 'G': kd += -0.4
		if aa == 'T': kd += -0.7
		if aa == 'S': kd += -0.8
		if aa == 'W': kd += -0.9
		if aa == 'Y': kd += -1.3
		if aa == 'P': kd += -1.6
		if aa == 'H': kd += -3.2
		if aa == 'E': kd += -3.5
		if aa == 'Q': kd += -3.5
		if aa == 'D': kd += -3.5
		if aa == 'N': kd += -3.5
		if aa == 'K': kd += -3.9
		if aa == 'R': kd += -4.5
	return kd/len(aaSeq)
	
def has_a_helix(seq, w, t):
	for i in range(len(seq) - w + 1):
		pep = seq[i:i+w]
		if 'P' in pep: continue # if you run into a P, just skip it.
		if kdCalc(pep) >= t: return True
	return False

names = []
seqs = []
seq = ''
with open(sys.argv[1]) as fp:
	for line in fp.readlines():
		if(line[0] == '>'): #
			words = line.split()
			names.append(words[0][1:])
			if len(seq) > 0: seqs.append(seq)
			seq = ''
		else: 
			seq += line.rstrip()
	seqs.append(seq)
	
for name, seq in zip(names, seqs):
	if has_a_helix(seq[:30], 8, 2.5) and has_a_helix(seq[30:], 11, 2.0):
		print(name)


"""
python3 40transmembrane.py ../Data/at_prots.fa
AT1G75120.1
AT1G10950.1
AT1G75110.1
AT1G74790.1
AT1G12660.1
AT1G75130.1
"""
