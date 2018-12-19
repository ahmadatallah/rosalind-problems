#!/usr/bin/env python
'''
A solution to a code challenges that accompanies Bioinformatics Algorithms: An Active-Learning Approach by Phillip Compeau & Pavel Pevzner.
The textbook is hosted on Stepic and the problem is listed on ROSALIND under the Textbook Track.

Problem Title: Number To Pattern Problem 
Chapter #: 01
Problem ID: M
URL: http://rosalind.info/problems/ba1m/
'''
import os 

number_to_symbol = {0:'A', 1:'C', 2:'G', 3:'T'}
    
def number_to_pattern(index, k):
    if k == 1:
        return number_to_symbol[index]
    prefixIndex = index / 4
    r = index % 4
    prefixPattern = number_to_pattern(prefixIndex, k - 1)
    return prefixPattern + number_to_symbol[r]


if __name__ == "__main__":
    full_path = os.path.realpath(__file__)
    with open(os.path.join(os.path.dirname(full_path),'data/rosalind_ba1m.txt')) as input_data:
        number = int(input_data.readline().strip())
        k = int(input_data.readline())
    
    pattern = number_to_pattern(number, k)
    print(pattern)

    # Print and save the answer.
    with open(os.path.join(os.path.dirname(full_path), 'output/Textbook_ba1m.txt'), 'w') as output_data:
        output_data.write("".join(str(pattern)))
