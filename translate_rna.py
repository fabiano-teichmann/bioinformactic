from Bio.Seq import Seq
from Bio.Alphabet import IUPAC


def translate_rna(rna: str) -> str:
    rna = Seq(rna, IUPAC.unambiguous_rna)
    return str(rna.translate(to_stop=True))


file = open('datasets/translate_rna.txt', 'r')
rna = file.read()
print(len(rna))
resp = translate_rna(rna)
print(resp)
print(len(resp))

