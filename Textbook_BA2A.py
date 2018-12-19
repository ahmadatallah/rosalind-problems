#!/usr/bin/env python
'''
A solution to a code challenges that accompanies Bioinformatics Algorithms: An Active-Learning Approach by Phillip Compeau & Pavel Pevzner.
The textbook is hosted on Stepic and the problem is listed on ROSALIND under the Textbook Track.

Problem Title: Find All Approximate Occurrences of a Pattern in a String
Chapter #: 02
Problem ID: A
URL: http://rosalind.info/problems/ba2a/
'''

from Textbook_BA1I import pattern_mismatches
import os 

def motif_enumeration (k, d, dna_list):
    # Generate sets of (k,d)-motifs for each dna sequence in the list.
    motif_sets = [{kmer for i in xrange(len(dna)-k+1) for kmer in pattern_mismatches(dna[i:i+k], d)} for dna in dna_list]

    # Intersect all sets to get the common elements.  The answers are displayed as sorted, so we'll sort too.
    return sorted(list(reduce(lambda a,b: a & b, motif_sets)))

def main():
    """
    Main call. Reads, runs, and saves problem specific data.
    """
    # Read the input data.
    full_path = os.path.realpath(__file__)

    with open(os.path.join(os.path.dirname(full_path), 'data/rosalind_ba2a.txt')) as input_data:    
        nums = input_data.readline().strip().split('\n')
        numbers = [n for n in nums[0].split(' ')]
        k = int(numbers[0])
        d = int(numbers[1])
        dna_list = [line.rstrip('\n') for line in input_data] 



    motifs = motif_enumeration(k, d, dna_list)
    print ' '.join(motifs)

    # Print and save the answer.
    with open(os.path.join(os.path.dirname(full_path), 'output/Textbook_ba2a.txt'), 'w') as output_data:
            output_data.write(" ".join(str(i) for i in motifs))

if __name__ == '__main__':
    main()
