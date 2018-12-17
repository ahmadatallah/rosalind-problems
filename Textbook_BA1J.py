#!/usr/bin/env python
'''
A solution to a code challenges that accompanies Bioinformatics Algorithms: An Active-Learning Approach by Phillip Compeau & Pavel Pevzner.
The textbook is hosted on Stepic and the problem is listed on ROSALIND under the Textbook Track.

Problem Title: Find All Approximate Occurrences of a Pattern in a String
Chapter #: 01
Problem ID: J
URL: http://rosalind.info/problems/ba1j/

'''

from Textbook_BA1I import pattern_mismatches
from collections import defaultdict, OrderedDict, Counter
from itertools import combinations, product, izip, imap
from operator import ne
from string import maketrans
import os 

def revese_complement(dna):
    '''Returns the reverse complement of a given DNA strand.'''
    transtab = maketrans('ATCG', 'TAGC')
    return dna.translate(transtab)[::-1]
     

def most_freq_words_with_mismatchs_and_reverse(dna, k, d):
    result_mismatch = []
    if not k <= 12 and k >= 1:
        raise ValueError("Pattern length must be between 0 and 12. {} was passed.".format(k))
    if not d <= 3 and d >= 1:
        raise ValueError("Max. mismatch must be between 0 and 3. {} was passed.".format(d))

    motif_words = defaultdict(int)
    for i in range(len(dna)-k+1): # split in every space.
        motif_words[dna[i:i+k]] += 1
        motif_words[revese_complement(dna[i:i+k])] += 1

    # Get all of the mismatches for each unique motif word in the sequence
    mismatch_count = defaultdict(int)
    for kmer, freq in motif_words.iteritems():
        for mismatch in pattern_mismatches(kmer, d):
            mismatch_count[mismatch] += freq

    max_count_num = max(mismatch_count.values())
    for i,word in enumerate(sorted(mismatch_count,key = mismatch_count.get,reverse = True)[:len(dna)]):
        # sorts the dict by the values, from top to botton, takes the all items sorted from high to low 
        # print(word, mismatch_count[word])
        if (mismatch_count[word] == max_count_num):
            result_mismatch.append(word)
    return result_mismatch

def main():
    """
    Main call. Reads, runs, and saves problem specific data.
    """
    # Read the input data.
    full_path = os.path.realpath(__file__)

    with open(os.path.join(os.path.dirname(full_path), 'data/rosalind_ba1j.txt')) as input_data:
        dna = input_data.readline().strip()
        params = input_data.readline().strip().split('\n')
        split_params = [n for n in params[0].split(' ')]
        k_mere = int(split_params[0])
        d_mis = int(split_params[1])

    most_mismatches = most_freq_words_with_mismatchs_and_reverse(dna, k_mere, d_mis)
    print ' '.join(most_mismatches)
    
    # Print and save the answer.
    with open(os.path.join(os.path.dirname(full_path), 'output/Textbook_ba1j.txt'), 'w') as output_data:
            output_data.write(" ".join(str(i) for i in most_mismatches))

if __name__ == '__main__':
    main()