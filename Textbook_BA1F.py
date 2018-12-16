#!/usr/bin/env python
'''
A solution to a code challenges that accompanies Bioinformatics Algorithms: An Active-Learning Approach by Phillip Compeau & Pavel Pevzner.
The textbook is hosted on Stepic and the problem is listed on ROSALIND under the Textbook Track.

Problem Title: Find Patterns Forming Clumps in a String
Chapter #: 01
Problem ID: F
URL: http://rosalind.info/problems/ba1f/
'''

from __future__ import print_function
import os

def minimum_skew(sequence):
	skew_value, min_skew, skew_list  = 0, 1, []
	g=0
	c=0
	for i in range (len(sequence)):
		if sequence[i] == 'C':
			#c += 1
			skew_value -= 1
		if sequence[i] == 'G':
			#g += 1
			skew_value += 1
		#skew_value = g - c
		if skew_value < min_skew:
			skew_list = [str(i+1)]
			min_skew = skew_value
		if skew_value == min_skew and (i+1) not in skew_list:
			skew_list.append(str(i+1))
			#print skew_list
	return skew_list

def main():
    '''Main call. Reads, runs, and saves problem specific data.'''
    # Read the input data.
    full_path = os.path.realpath(__file__)
    
    with open(os.path.join(os.path.dirname(full_path),'data/rosalind_ba1f.txt') ) as input_data:
	    sequence = input_data.readline().strip()
						
    min_skew_index = minimum_skew(sequence)
	
    # Print and save the answer.
    print(*min_skew_index, sep = " ")
	
    with open(os.path.join(os.path.dirname(full_path),'output/Textbook_ba1f.txt'), 'w') as output_data:
            output_data.write(" ".join(str(i) for i in min_skew_index ))

if __name__ == '__main__':
    main()

