import sys
from Bio import SeqIO
import matplotlib.pyplot as plt


if ".fasta" in sys.argv[len(sys.argv) - 1]:
    file_name = sys.argv[len(sys.argv) - 1]
    print("Считаю")
else:
    print(
        "Для работы нужен файл в формате fasta")
    sys.exit()

fasta_sequences = SeqIO.parse(open(file_name), 'fasta')

dna = []
sequences = []

with open(file_name) as handle:
    for record in SeqIO.parse(handle, "fasta"):
        sequences.append(record.seq)

seq_lens = []
for i in sequences:
    seq_lens.append(len(i))

plt.hist(seq_lens)
plt.ylabel('Количество')
plt.xlabel('Длина последовательности')
plt.title('Распределение длины последовательностей')
plt.show()

