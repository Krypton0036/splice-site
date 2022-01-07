# GTATGAGACT
import splice_site_maker

if splice_site_maker.splice_site_maker('ENSE00003915925') == 'GTATGAGACT':
    print('YES')
else:
    print('NO')
    print(splice_site_maker.splice_site_maker('ENSE00003915925'))
if splice_site_maker.splice_site_maker('ENSE00001832009') == 'GTGTGTGGGG':
    print('YES')
else:
    print('NO')
    print(splice_site_maker.splice_site_maker('ENSE00001832009'))
