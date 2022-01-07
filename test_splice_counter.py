import splice_counter

test = ['AGC', 'GTG', 'CAA', 'CGG', 'TCA']
if splice_counter.splice_counter(test) == [[0.2, 0.2, 0.2, 0.4],
                                           [0.2, 0.2, 0.4, 0.2],
                                           [0.4, 0.0, 0.4, 0.2]]:
    print('YES')
else:
    print('NO')
