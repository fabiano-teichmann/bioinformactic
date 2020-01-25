from Bio import SeqIO


sequences = SeqIO.parse("rosalind_gc.fasta", "fasta")
bigger = 0
for s in sequences:
    cg = s.seq.count('G') + s.seq.count('C')
    if cg > bigger:
        at = s.seq.count('A') + s.seq.count('T')
        percent =  cg * 100 / (cg + at)
        name = s.name
       
    bigger = cg
print(name)
print(f"{round(percent, 6)}%")
