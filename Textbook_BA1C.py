#!/usr/bin/env python
'''
A solution to a code challenges that accompanies Bioinformatics Algorithms: An Active-Learning Approach by Phillip Compeau & Pavel Pevzner.
The textbook is hosted on Stepic and the problem is listed on ROSALIND under the Textbook Track.

Problem Title: Find the Reverse Complement of a String
Chapter #: 01
Problem ID: C
URL: http://rosalind.info/problems/ba1c/
'''

import os

def revese_complement(s,i):
    z = []
    while (s!=""):
      if s[0] == 'A':
        s = s.replace(s[0],'T',1)
        z.append(s[0])
        s = s[1:len(s)]
      elif s [0] == 'T':
        s = s.replace(s[0],'A',1)
        z.append(s[0])
        s = s[1:len(s)]
      elif s [0] == 'G':
        s = s.replace(s[0],'C',1)
        z.append(s[0])
        s = s[1:len(s)]
      else:
        s = s.replace(s[0],'G',1)
        z.append(s[0])
        s = s[1:len(s)]
      i -= 1
    final =   ''.join(z)
    
    return final


def main():
    '''Main call. Reads, runs, and saves problem specific data.'''
    # Read the input data.
    full_path = os.path.realpath(__file__)
    
    with open(os.path.join(os.path.dirname(full_path),'data/rosalind_ba1c.txt') ) as input_data:
             dna =  input_data.readline()
             i  = len (dna)
    comp_dna = revese_complement(dna,i)
    # Print and save the answer.
    with open(os.path.join(os.path.dirname(full_path),'output/Textbook_ba1c.txt'), 'w') as output_data:
        output_data.write(comp_dna)
	
if __name__ == '__main__':
    main()
