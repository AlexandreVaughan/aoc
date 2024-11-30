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

def test_1line_letterednumbers():
    result = get_calibration_value("two1nine")
    assert result == 29
    result = get_calibration_value("eightwothree")
    assert result == 83
    result = get_calibration_value("abcone2threexyz")
    assert result == 13
    result = get_calibration_value("xtwone3four")
    assert result == 24
    result = get_calibration_value("4nineeightseven2")
    assert result == 42
    result = get_calibration_value("zoneight234")
    assert result == 14    
    result = get_calibration_value("7pqrstsixteen")
    assert result == 76
    result = get_calibration_value("fiveight")
    assert result == 58
    

def test_several_lines_letterednumbers():
    test_string = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen"""
    result = calibration_sum(test_string)
    assert result == 281