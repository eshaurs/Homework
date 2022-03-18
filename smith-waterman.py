import argparse
import math
import random
import sys

parser = argparse.ArgumentParser(description='Finds maximum scoring pair btwn 2 seqs.')
	
# match, mismatch, and gap score option
parser.add_argument('--match', required=True, type=int, default=3,
	metavar='<int>', help='match [%(default)i]')
parser.add_argument('--mismatch', required=True, type=int, default=-3,
	metavar='<int>', help='mismatch [%(default)i]')
parser.add_argument('--gap', required=True, type=int, default=-2,
	metavar='<int>', help='gap [%(default)i]')
	
arg = parser.parse_args()

# Functions
# generate two random sequences
def rand_seq(length): # takes in the length of the sequences we want to make
	seq = ''
	for i in range(length):
		seq += random.choice('ACGT')
	return seq

# make/initialize the scoring matrix
def initialize_matrix(seq1, seq2):
	matrix = []
	for row in range(len(seq1) + 1):
		matrix.append([0]*(len(seq2)+1))
	return matrix

# score each element in the matrix, from left to right, top to bottom
def score_matrix(matrix, match_num, mismatch, gap, seq1, seq2):
	traceback = initialize_matrix(seq1, seq2)
	# traceback = traceback[1:][1:]
	# print(traceback)
	# sys.exit()
	for i in range(1, len(seq1) + 1):
		for j in range(1, len(seq2) + 1):
			vertical = matrix[i-1][j] + gap
			horizontal = matrix[i][j-1] + gap
			if seq1[i-1] == seq2[j-1]: diag = matrix[i-1][j-1] + match_num
			else: diag = matrix[i-1][j-1] + mismatch
			
			if vertical < 0: vertical = 0
			if horizontal < 0: horizontal = 0
			if diag < 0: diag = 0
			
			if diag > vertical and diag > horizontal: 
				matrix[i][j] = diag
				traceback[i][j] = "d"
			elif vertical > diag and vertical > horizontal: 
				matrix[i][j] = vertical
				traceback[i][j] = "v"
			elif horizontal > diag and horizontal > vertical: 
				matrix[i][j] = horizontal
				traceback[i][j] = "h"
			else: 
				matrix[i][j] = diag
				traceback[i][j] = "d"
	return matrix, traceback
	
# traceback and aligning the sequences
def make_alignment(seq1, seq2, score_matrix, traceback):
	max = -1
	align_seq1 = ''
	align_seq2 = ''
	for i in range(len(seq1)+1):
		for j in range(len(seq2)+1):
			if score_matrix[i][j] > max: 
				max = score_matrix[i][j]
				max_pos = [i, j]
	trace = True 
	# print(max_pos)
	while trace:
		source = traceback[max_pos[0]][max_pos[1]]
		# print(source, max_pos)
		if source == 'd': 
			max_pos[0] -= 1
			max_pos[1] -= 1
			align_seq1 = seq1[max_pos[0]] + align_seq1
			align_seq2 = seq2[max_pos[1]] + align_seq2
		elif source == 'v':
			max_pos[0] -= 1
			align_seq2 = '-' + align_seq2
			align_seq1 = seq1[max_pos[0]] + align_seq1
			# print(max_pos, seq2, seq2[max_pos[1]])
		elif source == 'h':
			max_pos[1] -= 1
			align_seq2 = seq2[max_pos[1]] + align_seq2
			align_seq1 = '-' + align_seq1
		elif source == 0: trace = False
	return align_seq1, align_seq2
	
# Calling the functions
seq1 = rand_seq(10)
seq2 = rand_seq(10)
print("Sequence 1:", seq1)
print("Sequence 2:", seq2)

m, tb = score_matrix(initialize_matrix(seq1, seq2), arg.match, arg.mismatch, arg.gap, seq1, seq2)	

as1, as2 = make_alignment(seq1, seq2, m, tb)
print("Alignment:")
print(as1)
print(as2)
	