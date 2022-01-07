from pyensembl import EnsemblRelease

# release 104 uses human reference genome GRCh38
data = EnsemblRelease(104)
exon_ids = data.exon_ids_of_gene_name('DMD')
print(exon_ids)
print(data.exon_by_id('ENSE00003915925'))
