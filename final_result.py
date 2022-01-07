from pyensembl import EnsemblRelease

ensembl = EnsemblRelease(104)
from splice_site_maker import splice_site_maker
from splice_counter import splice_counter

seq_list = list()
for exon_id in ensembl.exon_ids('X', None):
    seq_list.append(splice_site_maker(exon_id))
print(splice_counter(seq_list))