from itertools import product
import os 

def d_neighborhood(dna, d):
    mis = []
    possible_k_mer = [''.join(p) for p in product(['A','C','G','T'], repeat=len(dna))]
    for i in range(len(possible_k_mer)):
        for j in range(len(dna)):
            p = sum( c1 != c2 for c1,c2 in zip(dna,possible_k_mer[i]))
            if p <= d:
                mis.append(possible_k_mer[i])

    return mis 

def main():
    """
    Main call. Reads, runs, and saves problem specific data.
    """
    # Read the input data.
    full_path = os.path.realpath(__file__)

    with open(os.path.join(os.path.dirname(full_path), 'data/rosalind_ba1n.txt')) as input_data:
        dna = input_data.readline().strip()
        d = int(input_data.readline().strip())
    
    d_neighbors = d_neighborhood(dna, d)
    d_neighbors_list = list(set(d_neighbors))
    print '\n'.join(d_neighbors_list)
    # Print and save the answer.
    with open(os.path.join(os.path.dirname(full_path), 'output/Textbook_ba1n.txt'), 'w') as output_data:
            output_data.write("\n".join(str(i) for i in d_neighbors_list))

if __name__ == '__main__':
    main()


