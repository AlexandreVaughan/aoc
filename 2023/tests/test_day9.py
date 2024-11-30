from day9 import Sequence

def test_delta_sequence():
    seq = Sequence("0 3 6 9 12 15")
    assert seq.initial_sequence == [0,3,6,9,12,15]
    assert seq.delta_sequence() == [3,3,3,3,3]
    seq = Sequence("1 3 6 10 15 21")
    assert seq.delta_sequence() == [2,3,4,5,6]

def test_all_delta_sequences():
    seq = Sequence("0 3 6 9 12 15")
    assert seq.initial_sequence == [0,3,6,9,12,15]
    assert seq.all_delta_sequences() == [[3,3,3,3,3]]
    seq = Sequence("1 3 6 10 15 21")
    assert seq.all_delta_sequences() == [[2,3,4,5,6],[1,1,1,1]]

def test_next_value():
    seq = Sequence("0 3 6 9 12 15")
    assert seq.next_value() == 18
    seq = Sequence("1 3 6 10 15 21")
    assert seq.next_value() == 28
    seq = Sequence("10 13 16 21 30 45")
    assert seq.next_value() == 68

def test_prev_value():
    seq = Sequence("0 3 6 9 12 15")
    assert seq.prev_value() == -3
    seq = Sequence("1 3 6 10 15 21")
    assert seq.prev_value() == 0
    seq = Sequence("10 13 16 21 30 45")
    assert seq.prev_value() == 5
