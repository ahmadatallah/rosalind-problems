#!/usr/bin/env python
'''
A solution to a code challenges that accompanies Bioinformatics Algorithms: An Active-Learning Approach by Phillip Compeau & Pavel Pevzner.
The textbook is hosted on Stepic and the problem is listed on ROSALIND under the Textbook Track.

Problem Title: Pattern To Number Problem
Chapter #: 01
Problem ID: L
URL: http://rosalind.info/problems/ba1l/
'''

import os 
symbol_to_number = {'A':0, 'C':1, 'G':2, 'T':3}
def pattern_to_number(pattern):
    if len(pattern)  == 0:
        return 0
    return 4 * pattern_to_number(pattern[:-1]) + symbol_to_number[pattern[-1]]

if __name__ == "__main__":
    full_path = os.path.realpath(__file__)
    with open(os.path.join(os.path.dirname(full_path),'data/rosalind_ba1l.txt')) as input_data:
        dna_motif = input_data.readline().strip()

    num = pattern_to_number(dna_motif)
    
    # Print and save the answer.
    with open(os.path.join(os.path.dirname(full_path), 'output/Textbook_ba1l.txt'), 'w') as output_data:
            output_data.write("".join(str(num)))