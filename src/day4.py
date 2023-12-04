class Card:
    def __init__(self) -> None:
        self.winning_numbers = set()
        self.card_numbers = set()
    
    def win_value(self):
        win_val = 0
        for num in self.card_numbers:
            if not num in self.winning_numbers:
                continue
            if win_val == 0:
                win_val = 1
            else:
                win_val *= 2
        return win_val

    def set_definition(self,definition : str):
        (_,_,card_content) = definition.partition(":")
        (winning_numbers_str,_,card_numbers_str) = card_content.partition("|")
        self.winning_numbers = _read_num_list(winning_numbers_str)
        self.card_numbers = _read_num_list(card_numbers_str)

def _read_num_list(numbers_list_str):
    numbers_list = set()
    for num in numbers_list_str.strip().split(" "):
        if num == "":
            continue
        numbers_list.add(int(num))
    return numbers_list

if __name__ == "__main__":
    f = open("D:\\Sources\\sample_projects\\aoc2023\\tests\\day4.txt", "r")
    txt = f.read()
    sum = 0
    for line in txt.splitlines():
        card = Card()
        card.set_definition(line)
        sum+=card.win_value()
    print(sum)

    