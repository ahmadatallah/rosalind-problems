#!/usr/bin/env python
'''
A solution to a code challenges that accompanies Bioinformatics Algorithms: An Active-Learning Approach by Phillip Compeau & Pavel Pevzner.
The textbook is hosted on Stepic and the problem is listed on ROSALIND under the Textbook Track.

Problem Title: Find All Occurrences of a Pattern in a String
Chapter #: 01
Problem ID: D
URL: http://rosalind.info/problems/ba1d/
'''

from __future__ import print_function
import os
def pattern_occurence(dna,pattern):
	occurences  = [] 
	for i in range(len(dna)):
		if dna[i:].startswith(pattern):
			occurences.append(i)
	return occurences

def main():
    '''Main call. Reads, runs, and saves problem specific data.'''
    # Read the input data.
    full_path = os.path.realpath(__file__)
    
    with open(os.path.join(os.path.dirname(full_path),'data/rosalind_ba1d.txt') ) as input_data:
			 pattern = input_data.readline().strip()
			 dna = input_data.readline().strip()
		
    occurence_index = pattern_occurence(dna,pattern)
    # Print and save the answer.
    print (*occurence_index, sep = " ")
    with open(os.path.join(os.path.dirname(full_path),'output/Textbook_ba1d.txt'), 'w') as output_data:
			 output_data.write(" ".join(str(i) for i in occurence_index ))
	
if __name__ == '__main__':
    main()
