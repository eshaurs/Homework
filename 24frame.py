#!/usr/bin/env python3

# Write a program that prints out the position, frame, and letter of the DNA
# Try coding this with a single loop
# Try coding this with nested loops

# Worked on with Majken on 01/30 and a large group of people in office hours on 01/31

dna = 'ATGGCCTTT'
frameCount = 0

# Trying it with a single loop 
for i in range(0, len(dna)):
    if frameCount == 0: 
    	print(i, frameCount, dna[i])
    	frameCount += 1
    elif frameCount == 1:
    	print(i, frameCount, dna[i])
    	frameCount += 1
    else: 
    	print(i, frameCount, dna[i])
    	frameCount = 0 
    	
# you can do this as i % 3. When we were in a big group in office hours, we came up with
# this method as well. 
for i in range(len(dna)):
	print(i, i % 3, dna[i])
	
    	
#Trying it with multiple loops
for i in range(0, len(dna),3):
	for j in range(0, 3):
		pos = i + j
		print(pos, j, dna[pos])


"""
python3 24frame.py
0 0 A
1 1 T
2 2 G
3 0 G
4 1 C
5 2 C
6 0 T
7 1 T
8 2 T
"""
