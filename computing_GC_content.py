from Bio import SeqIO


def computing_GC_content():
    """
    http://rosalind.info/problems/gc/ 
    """
    sequences = SeqIO.parse("datasets/rosalind_gc.fasta", "fasta")
    bigger = 0
    for s in sequences:
        cg = s.seq.count('CG') + s.seq.count('CG')
        if cg > bigger:
            at = s.seq.count('A') + s.seq.count('T')
            percent =  cg * 100 / (cg + at)
            name = s.name

        bigger = cg
    return name, round(percent, 6)


name, percent = computing_GC_content()
print(name)
print(f"{round(percent, 6)}%")
