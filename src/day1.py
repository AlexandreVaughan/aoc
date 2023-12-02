


def get_calibration_value(line):
    normalized_line = _replace_lettered_numbers(line, FORWARD)
    first_number = _get_first_digit(normalized_line)
    normalized_line = _replace_lettered_numbers(line,BACKWARD)
    second_number = _get_first_digit(normalized_line[::-1])
    return first_number*10+second_number

def calibration_sum(lines):
    cal_sum = 0
    for line in lines.splitlines():
        cal_sum += get_calibration_value(line)
    return cal_sum

def _replace_lettered_number(line, char_index):
    number_map = {
        "one" : 1,
        "two" : 2,
        "three" : 3,
        "four" : 4,
        "five" : 5,
        "six" : 6,
        "seven" : 7,
        "eight" : 8,
        "nine" : 9,
    }
    for letters,value in number_map.items():
        if line[char_index:].startswith(letters):
            return (letters, str(value))
    return ("","")

FORWARD = 0
BACKWARD = 1

def _replace_lettered_numbers(line, direction):
    normalized_line = ""
    if direction == FORWARD:
        char_index = 0
        while char_index < len(line):
            (letters,value) = _replace_lettered_number(line,char_index)
            if letters != "":
                normalized_line += str(value)
                char_index += len(letters)
                continue
            normalized_line += line[char_index]
            char_index+=1
    else:
        char_index = len(line) -1
        while char_index >= 0:
            (letters,value) = _replace_lettered_number(line,char_index)
            if letters != "":
                normalized_line = value + normalized_line
                char_index -= len(letters)
                continue
            normalized_line = line[char_index] + normalized_line
            char_index-=1

    return normalized_line
            
def _get_first_digit(line):
    for char in line:
        if not char.isdigit():
            continue
        return int(char)
    return 0

if __name__ == "__main__":
    f = open("D:\\Sources\\sample_projects\\aoc2023\\tests\\day1.txt", "r")
    txt = f.read()
    print(calibration_sum(txt))
