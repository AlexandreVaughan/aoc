


def get_calibration_value(line):
    first_number = _get_first_digit(line)
    second_number = _get_first_digit(line[::-1])
    return first_number*10+second_number

def calibration_sum(lines):
    cal_sum = 0
    for line in lines.splitlines():
        cal_sum += get_calibration_value(line)
    return cal_sum


def _get_first_digit(line):
    for char in line:
        if not char.isdigit():
            continue
        return int(char)
    return 0

if __name__ == "__main__":
    f = open("/media/alexandre/DATA/Sources/aoc2023/tests/day1.txt", "r")
    txt = f.read()
    print(calibration_sum(txt))
