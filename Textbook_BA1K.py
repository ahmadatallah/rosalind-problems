#!/usr/bin/env python
'''
A solution to a code challenges that accompanies Bioinformatics Algorithms: An Active-Learning Approach by Phillip Compeau & Pavel Pevzner.
The textbook is hosted on Stepic and the problem is listed on ROSALIND under the Textbook Track.

Problem Title: Generate the Frequency Array of a String
Chapter #: 01
Problem ID: K
URL: http://rosalind.info/problems/ba1k/
'''

from itertools import product
import os 

def count_motif(dna,k):
     motif_words = {} 
     for i in range(len(dna)-k+1): # split in every space.
          word = dna[i:k+i]
          if len(word) > 0 and word != '\r\n':
              if word not in motif_words: # if 'word' not in word_counter, add it, and set value to 1
                    motif_words[word] = 1
              else:
                    motif_words[word] += 1 # if 'word' already in word_counter, increment it by

     possible_k_mer = [''.join(p) for p in product(['A','C','G','T'], repeat=k)]
     for i in range(len(possible_k_mer)):
             if possible_k_mer[i] not in motif_words:
                    motif_words[possible_k_mer[i]] = 0
     
          
     return motif_words

''' 
sort motif words alphabetically 
'''
def sort_alphabetic(motif_words): 
      result = []
      for item in motif_words:
            if item not in result:
               result.append(item)
      return result


def main():
    """
    Main call. Reads, runs, and saves problem specific data.
    """
    # Read the input data.
    full_path = os.path.realpath(__file__)

    with open(os.path.join(os.path.dirname(full_path), 'data/rosalind_ba1k.txt')) as input_data:
      dna = input_data.readline().strip()
      k   = int(input_data.readline().strip())

    motif_words = count_motif(dna, k)
    sorted_alpha_motif = sort_alphabetic(motif_words) 

    freq_array = []

    #iterates through the sorted items.
    for item in sorted(sorted_alpha_motif): 
          print motif_words[item],
          freq_array.append(motif_words[item])  

    # Print and save the answer.
    with open(os.path.join(os.path.dirname(full_path), 'output/Textbook_ba1k.txt'), 'w') as output_data:
            output_data.write(" ".join(str(i) for i in freq_array))

if __name__ == '__main__':
    main()