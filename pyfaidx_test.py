from pyfaidx import Fasta

genes = Fasta('/Users/macbookair/tmp/Homo_sapiens.GRCh38.dna.chromosome.X.fa')
print(genes['X'][31169443:31169556])
