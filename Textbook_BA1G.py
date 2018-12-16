
#!/usr/bin/env python
'''
A solution to a code challenges that accompanies Bioinformatics Algorithms: An Active-Learning Approach by Phillip Compeau & Pavel Pevzner.
The textbook is hosted on Stepic and the problem is listed on ROSALIND under the Textbook Track.

Problem Title: Compute the Hamming Distance Between Two Strings
Chapter #: 01
Problem ID: G
URL: http://rosalind.info/problems/ba1g/
'''

from  __future__ import print_function
import os


def hamming_distance(dna_s1, dna_s2):
    n = 0
    for i in range(len(dna_s1)):
            if dna_s1[i] != dna_s2[i]:
                        n += 1
    return n


def main():
    """
    Main call. Reads, runs, and saves problem specific data.
    """
    # Read the input data.
    full_path = os.path.realpath(__file__)

    with open(os.path.join(os.path.dirname(full_path), 'data/rosalind_ba1g.txt')) as input_data:
            dna_s1= input_data.readline().strip()
            dna_s2 = input_data.readline().strip()
    hamming_dist = hamming_distance(dna_s1, dna_s2)
    # Print and save the answer.
    print(hamming_dist)
    with open(os.path.join(os.path.dirname(full_path), 'output/Textbook_ba1g.txt'), 'w') as output_data:
            output_data.write(" ".join(str(hamming_dist)))

if __name__ == '__main__':
    main()

