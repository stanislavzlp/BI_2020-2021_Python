from Bio import SeqIO


def translation(path_to_fasta, table_for_translation="Standard"):
    with open(path_to_fasta, 'r') as fasta_file:
        for record in SeqIO.parse(fasta_file, 'fasta'):
            coding_dna = record.seq
            protein_seq = coding_dna.translate(table=table_for_translation)
            yield protein_seq


# proteins_from_fasta = translation('/exapmle.fasta', "Standard")

# next(proteins_from_fasta)
