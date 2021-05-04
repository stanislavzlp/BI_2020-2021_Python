class RNA:

    def __init__(self, seq: str):

        for i in seq:
            if i == 'A' or i == 'U' or i == 'G' or i == 'C':
                pass
            else:
                raise NameError('Only A, U, G or C nucleotides are possible for RNA')
        self.seq = seq
        self.i = 0

    def gc_content(self):
        GC_count = 0
        for i in self.seq:
            if i == 'G' or i == 'C':
                GC_count += 1
        return GC_count / len(self.seq) * 100

    def reverse_complement(self):
        complement_seq = ''
        for i in self.seq:
            if i == 'A':
                complement_seq += 'U'
            elif i == 'U':
                complement_seq += 'A'
            elif i == 'G':
                complement_seq += 'C'
            elif i == 'C':
                complement_seq += 'G'
        return complement_seq

    def __next__(self):
        if self.i > len(self.seq):
            raise StopIteration
        el = self.seq[self.i]
        self.i += 1
        return el

    def __iter__(self):
        return self

    def __eq__(self, other):
        return self.seq == other.seq
