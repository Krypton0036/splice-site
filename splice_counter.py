def splice_counter(seq_list):
    nucleotides = ('A', 'T', 'G', 'C', 'N')  # in the needed order
    nucleotide_amount_zeros = {}  # helper dict: keys - nucleotides, values - zeros (2 lines below do it)
    for nucleotide in nucleotides:
        nucleotide_amount_zeros[nucleotide] = 0
    list_len = len(seq_list)
    seq_len = len(seq_list[0])
    matrix = []  # the function's future output
    for line_number in range(seq_len):
        nucleotide_amount = dict(nucleotide_amount_zeros)  # clears (or defines) nucleotide_amount
        for i in range(list_len):
            nucleotide = seq_list[i][line_number]  # line_number'th nucleotide of i'th sequence
            nucleotide_amount[nucleotide] += 1
        matrix_line = list()  # creates a future line of the matrix
        for nucleotide in nucleotides:
            matrix_line.append(nucleotide_amount[nucleotide] / list_len)  # adds probabilities to the future line
        matrix.append(matrix_line)
    return (matrix)
