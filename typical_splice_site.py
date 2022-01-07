from pyensembl import EnsemblRelease

ensembl = EnsemblRelease(104)
from splice_site_maker import splice_site_maker
from splice_counter import splice_counter

nucleotides = ['A', 'T', 'G', 'C', 'N']
seq_list = list()
for exon_id in ensembl.exon_ids('X', None):
    seq_list.append(splice_site_maker(exon_id))
matrix = splice_counter(seq_list)
final_string = str()
for line in matrix:
    nucleotide = 'N'
    maxprob = max(line)
    for i in range(len(line)):
        prob = line[i]
        if maxprob == prob:
            nucleotide = nucleotides[i]
    final_string += nucleotide
print(final_string)
