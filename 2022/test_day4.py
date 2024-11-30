from day4 import *


def test_inclusion_disjoint_pairs():
    assert not included_pairs((2,4), (6,8))
    assert not included_pairs((2,5), (6,8))
    assert not included_pairs((2,3), (4,5))
    assert not included_pairs((69,80), (5,44))

def test_inclusion_overlapped_pairs():
    assert not included_pairs((5,7), (7,9))
    assert not included_pairs((2,6), (4,8))
    assert not included_pairs((1,2), (2,97))

def test_inclusion_included_pairs():
    assert included_pairs((2,8), (3,7))
    assert included_pairs((6,6), (4,6))

def test_overlap_disjoint_pairs():
    assert not overlapped_pairs((2,4), (6,8))
    assert not overlapped_pairs((2,5), (6,8))
    assert not overlapped_pairs((2,3), (4,5))
    assert not overlapped_pairs((69,80), (5,44))

def test_overlap_overlapped_pairs():
    assert overlapped_pairs((5,7), (7,9))
    assert overlapped_pairs((2,6), (4,8))
    assert overlapped_pairs((1,2), (2,97))

def test_overlap_included_pairs():
    assert overlapped_pairs((2,8), (3,7))
    assert overlapped_pairs((6,6), (4,6))