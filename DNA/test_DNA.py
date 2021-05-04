from DNA.DNA import DNA
from DNA.RNA import RNA
from collections.abc import Iterable


# tests using pytest

def test_DNA_rev_com():
    assert DNA('AGTC').reverse_complement() == 'TCAG'


def test_DNA_GC_cont():
    assert DNA('GCGC').gc_content() == 100
    assert DNA('AAGC').gc_content() == 50
    assert DNA('ATGC').gc_content() == 50


def test_DNA_eq_DNA():
    assert DNA('ATGC') == DNA('ATGC')


def test_next_letter_DNA():
    assert next(DNA('AGCT')) == 'A'
    assert next(DNA('AGCT')) == 'A'
    checker_DNA = DNA('AGCT')
    assert next(checker_DNA) == 'A'
    assert next(checker_DNA) == 'G'
    assert next(checker_DNA) == 'C'
    assert next(checker_DNA) == 'T'


def test_iteration_DNA():
    assert isinstance(iter(DNA('AGTC').seq), Iterable)


def test_DNA_seq_to_RNA_seq():
    assert DNA('ATGC').transcribe().seq == RNA('UACG').seq


def test_DNA_to_RNA():
    assert DNA('ATGC').transcribe() == RNA('UACG')


def test_RNA_GC_cont():
    assert RNA('GCGC').gc_content() == 100
    assert RNA('AAGC').gc_content() == 50
    assert RNA('AUGC').gc_content() == 50


def test_RNA_rev_com():
    assert RNA('AGUC').reverse_complement() == 'UCAG'


def test_next_letter_RNA():
    assert next(RNA('AGCU')) == 'A'
    assert next(RNA('AGCU')) == 'A'
    checker_RNA = RNA('AGCU')
    assert next(checker_RNA) == 'A'
    assert next(checker_RNA) == 'G'
    assert next(checker_RNA) == 'C'
    assert next(checker_RNA) == 'U'


def test_iteration_RNA():
    assert isinstance(iter(RNA('AGUC').seq), Iterable)


def test_RNA_eq_RNA():
    assert RNA('AUGC') == RNA('AUGC')
