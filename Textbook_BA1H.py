#!/usr/bin/env python
'''
A solution to a code challenges that accompanies Bioinformatics Algorithms: An Active-Learning Approach by Phillip Compeau & Pavel Pevzner.
The textbook is hosted on Stepic and the problem is listed on ROSALIND under the Textbook Track.

Problem Title: Find All Approximate Occurrences of a Pattern in a String
Chapter #: 01
Problem ID: H
URL: http://rosalind.info/problems/ba1h/
'''
from __future__ import print_function
import os


def dna_pattern(dna, pattern, n_mis):
    # init mismatch indices array            
    mismatches_indices = []
    for i in xrange(len(dna)-len(pattern)+1):
        mismatch_count = 0
        for j in xrange(len(pattern)):
            # get sample of dna based on given pattern
            sample = dna[i:(len(pattern)+i)]
            #check mismatch
            if sample[j] != pattern[j]:
                mismatch_count += 1
        
        if mismatch_count <= n_mis:
            mismatches_indices.append(str(i))

    return mismatches_indices


def main():
    """
    Main call. Reads, runs, and saves problem specific data.
    """
    # Read the input data.
    full_path = os.path.realpath(__file__)

    with open(os.path.join(os.path.dirname(full_path), 'data/rosalind_ba1h.txt')) as input_data:
            pattern= input_data.readline().strip()
            dna = input_data.readline().strip()
            n_mismatches = int(input_data.readline().strip())
    mismatches_indices = dna_pattern(dna, pattern, n_mismatches)
    # Print and save the answer.
    print(*mismatches_indices, sep=" ")
    with open(os.path.join(os.path.dirname(full_path), 'output/Textbook_ba1h.txt'), 'w') as output_data:
            output_data.write(" ".join(str(i) for i in mismatches_indices))

if __name__ == '__main__':
    main()


     
                

