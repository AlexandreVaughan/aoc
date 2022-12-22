
from day6 import *

def test_emptystream():
    stream = ""
    assert find_marker_end(stream) == 0

def test_allsame():
    stream = "aaaaaaaaaa"
    assert find_marker_end(stream) == 0

def test_smallstream():
    stream = "abc"
    assert find_marker_end(stream) == 0

def test_markerstart():
    stream = "abcd"
    assert find_marker_end(stream) == 4
    stream = "abce"
    assert find_marker_end(stream) == 4

def test_markerend():
    stream = "aabcd"
    assert find_marker_end(stream) == 5

def test_examples():
    assert find_marker_end("mjqjpqmgbljsphdztnvjfqwrcgsmlb") == 7
    assert find_marker_end("bvwbjplbgvbhsrlpgdmjqwftvncz") == 5
    assert find_marker_end("nppdvjthqldpwncqszvftbrmjlhg") == 6
    assert find_marker_end("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg") == 10
    assert find_marker_end("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw") == 11

def test_messages():
    assert find_marker_end("mjqjpqmgbljsphdztnvjfqwrcgsmlb",MESSAGE_MARKER_SIZE) == 19
    assert find_marker_end("bvwbjplbgvbhsrlpgdmjqwftvncz",MESSAGE_MARKER_SIZE) == 23
    assert find_marker_end("nppdvjthqldpwncqszvftbrmjlhg",MESSAGE_MARKER_SIZE) == 23
    assert find_marker_end("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg",MESSAGE_MARKER_SIZE) == 29
    assert find_marker_end("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw",MESSAGE_MARKER_SIZE) == 26
