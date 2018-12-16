#!/usr/bin/env python
'''
A solution to a code challenges that accompanies Bioinformatics Algorithms: An Active-Learning Approach by Phillip Compeau & Pavel Pevzner.
The textbook is hosted on Stepic and the problem is listed on ROSALIND under the Textbook Track.

Problem Title: Compute the Number of Times a Pattern Appears in a Text
Chapter #: 01
Problem ID: A
URL: http://rosalind.info/problems/ba1a/
'''

import os
def count_pattern(dna,pattern):
	count = 0
	for i in range(len(dna)):
		if dna.startswith(pattern ,i ,i+len(pattern)):
			count += 1
	return count

def main():
    '''Main call. Reads, runs, and saves problem specific data.'''
    # Read the input data.
    full_path = os.path.realpath(__file__)
    
    with open(os.path.join(os.path.dirname(full_path),'data/rosalind_ba1a.txt') ) as input_data:
		dna =  input_data.readline().strip()
		pattern = input_data.readline().strip()
			   
    count = count_pattern(dna,pattern)
    # Print and save the answer.
    print (count)
    with open(os.path.join(os.path.dirname(full_path),'output/Textbook_ba1a.txt'), 'w') as output_data:
        output_data.write(str(count))
	
if __name__ == '__main__':
    main()
