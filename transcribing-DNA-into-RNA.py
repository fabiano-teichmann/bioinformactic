file = open('datasets/rosalind_rna.txt', 'r')

dna = file.read()
rna = dna.replace('T', 'U')
print(rna)
