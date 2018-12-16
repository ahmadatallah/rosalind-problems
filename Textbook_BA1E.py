#!/usr/bin/env python
'''
A solution to a code challenges that accompanies Bioinformatics Algorithms: An Active-Learning Approach by Phillip Compeau & Pavel Pevzner.
The textbook is hosted on Stepic and the problem is listed on ROSALIND under the Textbook Track.

Problem Title: Find Patterns Forming Clumps in a String
Chapter #: 01
Problem ID: E
URL: http://rosalind.info/problems/ba1e/
'''

import os 
def clumps_patterns(dna,k,t,l):
     words = []
     for i in range(len(dna)):
          clump = dna[i:(l+i)]  # l in lenght of interval
          
          # A dictionary for storing 
          wordcounter={}
          if len(clump) == l:
               #counts all possible pattern of the interval  
               for j in range(len(clump)):
                    word  = clump[j:k+j]  # k-mers
                    if len(word) > 0 and word != '\r\n':
                         if word not in wordcounter:
                              wordcounter[word] = 1
                         else:
                              wordcounter[word] += 1
               for n,word in enumerate(wordcounter):
                    if wordcounter[word] >= t and word not in words:  # pattern appears at least t times
                              words.append(word)

     return words
##remove dublicates

def main():
    '''Main call. Reads, runs, and saves problem specific data.'''
    # Read the input data.
    full_path = os.path.realpath(__file__)
    
    with open(os.path.join(os.path.dirname(full_path),'data/rosalind_ba1e.txt') ) as input_data:
               dna = input_data.readline().strip()
               
               # map for mapping string list into int 
               k, L, t = map(int, input_data.readline().split())
              
                
    patterns = clumps_patterns(dna,k,t,L)
    # Print and save the answer.
    print " ".join(patterns)
    with open(os.path.join(os.path.dirname(full_path),'output/Textbook_ba1e.txt'), 'w') as output_data:
               output_data.write(" ".join(str(i) for i in patterns ))
if __name__ == '__main__':
    main()

