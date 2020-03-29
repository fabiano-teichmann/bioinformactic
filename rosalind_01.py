file = open('datasets/rosalind_dna.txt', 'r')
dna = file.read()
print(dna.count('A'), dna.count('C'), dna.count('G'), dna.count('T'))
