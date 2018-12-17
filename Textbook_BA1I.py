#!/usr/bin/env python
'''
A solution to a code challenges that accompanies Bioinformatics Algorithms: An Active-Learning Approach by Phillip Compeau & Pavel Pevzner.
The textbook is hosted on Stepic and the problem is listed on ROSALIND under the Textbook Track.

Problem Title: Find All Approximate Occurrences of a Pattern in a String
Chapter #: 01
Problem ID: I
URL: http://rosalind.info/problems/ba1i/
'''

from collections import OrderedDict
from operator import itemgetter
from itertools import product
from collections import defaultdict
from itertools import combinations, product, izip   
import os 

def pattern_mismatches(kmer, d): 
     # initialize mismatches with the k-mer itself (i.e. d=0).
    mismatches = [kmer] 
    alt_bases = {'A':'CGT', 'C':'AGT', 'G':'ACT', 'T':'ACG'}
    for dist in xrange(1, d+1):
        for change_indices in combinations(xrange(len(kmer)), dist):
            for substitutions in product(*[alt_bases[kmer[i]] for i in change_indices]):
                new_mistmatch = list(kmer)
                for idx, sub in izip(change_indices, substitutions):
                    new_mistmatch[idx] = sub
                mismatches.append(''.join(new_mistmatch))
    return mismatches

def most_freq_words_with_mismatchs(dna, k, d):
    result_mismatch = []
    if not k <= 12 and k >= 1:
        raise ValueError("Pattern length must be between 0 and 12. {} was passed.".format(k))
    if not d <= 3 and d >= 1:
        raise ValueError("Max. mismatch must be between 0 and 3. {} was passed.".format(d))

    motif_words = defaultdict(int)
    for i in range(len(dna)-k+1): # split in every space.
        motif_words[dna[i:i+k]] += 1

    # Get all of the mismatches for each unique motif word in the sequence
    mismatch_count = defaultdict(int)
    for kmer, freq in motif_words.iteritems():
        for mismatch in pattern_mismatches(kmer, d):
            mismatch_count[mismatch] += freq

    max_count_num = max(mismatch_count.values())
    for i,word in enumerate(sorted(mismatch_count,key = mismatch_count.get,reverse = True)[:len(dna)]):
        # sorts the dict by the values, from top to botton, takes the all items sorted from high to low 
        print(word, mismatch_count[word])
        if (mismatch_count[word] == max_count_num):
            result_mismatch.append(word)
    return result_mismatch


def main():
    """
    Main call. Reads, runs, and saves problem specific data.
    """
    # Read the input data.
    full_path = os.path.realpath(__file__)

    with open(os.path.join(os.path.dirname(full_path), 'data/rosalind_ba1i.txt')) as input_data:
        dna = input_data.readline().strip()
        params = input_data.readline().strip().split('\n')
        split_params = [n for n in params[0].split(' ')]
        k_mere = int(split_params[0])
        d_mis = int(split_params[1])

    mismatches = most_freq_words_with_mismatchs(dna, k_mere, d_mis)
    print(mismatches)
    # Print and save the answer.
    with open(os.path.join(os.path.dirname(full_path), 'output/Textbook_ba1i.txt'), 'w') as output_data:
            output_data.write(" ".join(str(i) for i in mismatches))

if __name__ == '__main__':
    main()