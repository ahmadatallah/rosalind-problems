#!/usr/bin/env python
'''
A solution to a code challenges that accompanies Bioinformatics Algorithms: An Active-Learning Approach by Phillip Compeau & Pavel Pevzner.
The textbook is hosted on Stepic and the problem is listed on ROSALIND under the Textbook Track.

Problem Title: Median String Problem
Chapter #: 02
Problem ID: B
'''

from itertools import product
import os 

def hamm_distance(seq1,seq2): 
    '''Calculate hamming distance between two sequences'''
    if len(seq1) != len(seq2):
        raise ValueError('undefined for sequences of unequal length.')
        return max(len(seq1), len(seq2))
    dist = 0
    for i in range(len(seq1)):
       if seq1[i] != seq2[i]:
              dist += 1
    return dist

def possible_kmer(k): 
     return  [''.join(p) for p in product(['A','C','G','T'], repeat=k)]
 
def median_string(k, dna_list):
    # Initialize the best pattern score as one greater than the maximum possible score.
    best_score = k*len(dna_list) + 1

    # Check the scores of all k-mers.
    for pattern in possible_kmer(k):
        current_score = sum([motif_score(''.join(pattern), dna) for dna in dna_list])
        if current_score < best_score:
            best_score = current_score
            min_pattern = ''.join(pattern)

    return min_pattern


def motif_score(pattern, motif):
    '''Returns the score of d(pattern, motif).'''
    return min([hamm_distance(motif[i:i+len(pattern)], pattern) for i in range(len(motif)-len(pattern)+1)])


def main():
    '''Main call. Reads, runs, and saves problem specific data.'''
    # Read the input data.
    full_path = os.path.realpath(__file__)
    with open(os.path.join(os.path.dirname(full_path),'data/rosalind_ba2b.txt')) as input_data:
        k = int(input_data.readline())
        dna_list = [line.strip() for line in input_data.readlines()]

    # Get the best pattern.
    best_pattern = median_string(k, dna_list)

    # Print and save the answer.
    print best_pattern
    with open(os.path.join(os.path.dirname(full_path),'output/Textbook_02B.txt'), 'w') as output_data:
        output_data.write(best_pattern)

if __name__ == '__main__':
    main()
