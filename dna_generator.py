import copy


def generate(len_of_seq: int):
    seq_list = []
    nucleotide_list = ['A', 'G', 'T', 'C']
    if len_of_seq != 0:
        seq_list = ['A', 'G', 'T', 'C']
    it = 0

    while len_of_seq > 1:
        new_list = copy.copy(seq_list)
        for i in new_list[it * 4:]:
            for j in nucleotide_list:
                new_list.append(i + j)
        it += 1
        len_of_seq -= 1
        seq_list = copy.copy(new_list)
    for seq in seq_list:
        yield seq
