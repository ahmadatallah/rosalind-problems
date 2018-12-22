#!/usr/bin/env python
'''
A solution to a code challenges that accompanies Bioinformatics Algorithms: An Active-Learning Approach by Phillip Compeau & Pavel Pevzner.
The textbook is hosted on Stepic and the problem is listed on ROSALIND under the Textbook Track.

Problem Title: Profile-most Probable k-mer Problem
Chapter #: 02
Problem ID: C
URL: http://rosalind.info/problems/ba2c/
'''

import os

def profile_most_probable_kmer(dna, k, profile):
    
    '''Returns the profile most probable k-mer for the given input data.'''
    # A dictionary relating nucleotides to their position within the profile.
    nuc_dict = {nucleotide:index for index,nucleotide in enumerate('ACGT')}

    # maximum probability.
    max_probability = -1

    # Compute the probability of the each k-mer, store it if it's currently a maximum.
    for i in xrange(len(dna)-k+1):
        # Get the current probability.
        current_probability = 1
        for j, nucleotide in enumerate(dna[i:i+k]):   
            current_probability *= profile[nuc_dict[nucleotide]][j]

        # Check for a maximum.
        if current_probability > max_probability:
            max_probability = current_probability
            most_probable = dna[i:i+k]

    return most_probable

def main():
    '''Main call. Reads, runs, and saves problem specific data.'''
    # Read the input data.
    full_path = os.path.realpath(__file__)
    with open(os.path.join(os.path.dirname(full_path),'data/rosalind_ba2c.txt')) as input_data:
        dna = input_data.readline().strip()
        k = int(input_data.readline())
        profile = [map(float,line.strip().split()) for line in input_data.readlines()]

    # Get the profile most probable k-mer.
    most_probable = profile_most_probable_kmer(dna, k, profile)

    # Print and save the answer.
    print most_probable
    with open(os.path.join(os.path.dirname(full_path),'output/Textbook_ba2c.txt'), 'w') as output_data:
        output_data.write(most_probable)

if __name__ == '__main__':
    main()
