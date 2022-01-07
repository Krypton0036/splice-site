# plan: function exon-splice site
from pyfaidx import Fasta
from pyensembl import EnsemblRelease
import splice_counter

faidx = Fasta('/Users/macbookair/tmp/Homo_sapiens.GRCh38.dna.chromosome.X.fa')
ensembl = EnsemblRelease(104)


def splice_site_maker(exon_id, length=10):
    exon = ensembl.exon_by_id(exon_id)
    start = exon.start
    end = exon.end
    if exon.strand == '+':
        return (str(faidx['X'][end:end + length]))
    else:
        return (str(faidx['X'][start - length - 1:start - 1].reverse.complement))
