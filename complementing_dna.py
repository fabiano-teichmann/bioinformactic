from Bio.Seq import Seq
file = open('rosalind_revc.txt', 'r')
dna = Seq(file.read())
reverse_complement_dna = dna.reverse_complement()
print(reverse_complement_dna)