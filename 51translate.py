#!/usr/bin/env python3
# 51translate.py

import sys

# Make a program that translates coding sequences into proteins
# You have been provided with the genetic code as a dictionary
# Use the actin sequence in the Data directory

gcode = {
	'AAA' : 'K',	'AAC' : 'N',	'AAG' : 'K',	'AAT' : 'N',
	'ACA' : 'T',	'ACC' : 'T',	'ACG' : 'T',	'ACT' : 'T',
	'AGA' : 'R',	'AGC' : 'S',	'AGG' : 'R',	'AGT' : 'S',
	'ATA' : 'I',	'ATC' : 'I',	'ATG' : 'M',	'ATT' : 'I',
	'CAA' : 'Q',	'CAC' : 'H',	'CAG' : 'Q',	'CAT' : 'H',
	'CCA' : 'P',	'CCC' : 'P',	'CCG' : 'P',	'CCT' : 'P',
	'CGA' : 'R',	'CGC' : 'R',	'CGG' : 'R',	'CGT' : 'R',
	'CTA' : 'L',	'CTC' : 'L',	'CTG' : 'L',	'CTT' : 'L',
	'GAA' : 'E',	'GAC' : 'D',	'GAG' : 'E',	'GAT' : 'D',
	'GCA' : 'A',	'GCC' : 'A',	'GCG' : 'A',	'GCT' : 'A',
	'GGA' : 'G',	'GGC' : 'G',	'GGG' : 'G',	'GGT' : 'G',
	'GTA' : 'V',	'GTC' : 'V',	'GTG' : 'V',	'GTT' : 'V',
	'TAA' : '*',	'TAC' : 'Y',	'TAG' : '*',	'TAT' : 'Y',
	'TCA' : 'S',	'TCC' : 'S',	'TCG' : 'S',	'TCT' : 'S',
	'TGA' : '*',	'TGC' : 'C',	'TGG' : 'W',	'TGT' : 'C',
	'TTA' : 'L',	'TTC' : 'F',	'TTG' : 'L',	'TTT' : 'F',
}

filename = sys.argv[1]

def translate(seq, frame = 0):
	protein = ''
	for i in range(frame, len(seq), 3):
		codon = seq[i:i+3]
		if codon in gcode: protein += gcode[codon]
		else: protein += 'X'
		#aa = gcode[codon]
		#print(codon, aa)
	return protein
		

def readfasta(filename):
	records = []
	seq = ''
	with open(filename) as fp:
		for line in fp.readlines():
			line = line.rstrip()
			if len(line) == 0: continue
			if line[0] == '>':
				if seq != '': records.append(id, seq)
				words = line.split()
				id = words[0][1:]
				seq = ''
			else: 
				seq += line.upper()
		records.append((id, seq))
	return records

for name, seq in readfasta(filename):
	for f in range(3): # printing out three of the frames, not just one. 
		print(name, f, translate(seq, frame = f)) 



"""
python3 51translate.py ../Data/act1.fa
MCDDEVAALVVDNGSGMCKAGFAGDDAPRAVFPSIVGRPRHQGVMVGMGQKDSYVGDEAQ
SKRGILTLKYPIEHGIVTNWDDMEKIWHHTFYNELRVAPEEHPVLLTEAPLNPKANREKM
TQIMFETFNTPAMYVAIQAVLSLYASGRTTGVVLDSGDGVTHTVPIYEGYALPHAILRLD
LAGRDLTDYLMKILTERGYSFTTTAEREIVRDIKEKLCYVALDFEQEMATAASSSSLEKX
YELPDGQVITVGNERFRCPEAMFQPSFLGMESAGIHETSYNSIMKCDIDIRKDLYANTVL
SGGTTMYPGIADRMQKEITALAPSTMKIKIIAPPERKYSVWIGGSILASLSTFQQMWISK
QEYDESGPSIVHRKCF*
"""
