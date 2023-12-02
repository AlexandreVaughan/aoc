from day1 import get_calibration_value, calibration_sum


def test_1line_beginning_end():
    result = get_calibration_value("1abc2")
    assert result == 12

def test_1line_two_numbers():
    result = get_calibration_value("pqr3stu8vwx")
    assert result == 38

def test_1line_several_numbers():
    result = get_calibration_value("a1b2c3d4e5f")
    assert result == 15

def test_1line_1number():
    result = get_calibration_value("treb7uchet")
    assert result == 77

def test_several_lines():
    test_string = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet"""
    result = calibration_sum(test_string)
    assert result == 142

