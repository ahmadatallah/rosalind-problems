#!/usr/bin/env python
'''
A solution to a code challenges that accompanies Bioinformatics Algorithms: An Active-Learning Approach by Phillip Compeau & Pavel Pevzner.
The textbook is hosted on Stepic and the problem is listed on ROSALIND under the Textbook Track.

Problem Title: Find the Most Frequent Words in a String
Chapter #: 01
Problem ID: B
URL: http://rosalind.info/problems/ba1b/
'''

import operator
import os

def most_frequent_words(dna, n): 
    word_counter = {}
    most_freq_words = []
    for i in range(len(dna)): # split in every space.
        word = dna[i:n+i]
        if len(word) > 0 and word != '\r\n':
            if word not in word_counter: # if 'word' not in word_counter, add it, and set value to 1
                word_counter[word] = 1
            else:
                word_counter[word] += 1 # if 'word' already in word_counter, increment it by 1

    # get the maximum count            
    max_count_num = max(word_counter.values())

    #iterate over sorted words 
    for i,word in enumerate(sorted(word_counter,key=word_counter.get,reverse = True)[:len(dna)]):
        # sorts the dict by the values, from top to botton, takes the all items sorted from high to low 
        if (word_counter[word] == max_count_num):
            most_freq_words.append(word)

    return most_freq_words
      
def main():
    '''Main call. Reads, runs, and saves problem specific data.'''
    # Read the input data.
    full_path = os.path.realpath(__file__)
    #init dna and n count 
    dna = ""
    n = 0
    with open(os.path.join(os.path.dirname(full_path),'data/rosalind_ba1b.txt') ) as input_data:
        dna = input_data.readline().strip()
        n = int(input_data.readline().strip())
                
    words = most_frequent_words (dna, n)
    # Print and save the answer.
    with open(os.path.join(os.path.dirname(full_path),'output/Textbook_ba1b.txt'), 'w') as output_data:
        output_data.write(' '.join(words))

if __name__ == '__main__':
    main()
