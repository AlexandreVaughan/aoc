class Card:
    def __init__(self) -> None:
        self.winning_numbers = set()
        self.card_numbers = set()
        self.id = 0
    
    def win_value(self):
        win_count = self.win_count()
        if win_count == 0:
            return 0
        return 2**(self.win_count()-1)
    
    def win_count(self):
        win_count = 0
        for num in self.card_numbers:
            if not num in self.winning_numbers:
                continue
            win_count+=1
        return win_count


    def set_definition(self,definition : str):
        (card_id,_,card_content) = definition.partition(":")
        (_,_,id) = card_id.partition(" ")
        self.id = int(id)
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

class CardList:
    def __init__(self) -> None:
        self.cards = []

    def set_definition(self, card_list_def: str):
        for card_def in card_list_def.splitlines():
            card = Card()
            card.set_definition(card_def)
            self.cards.append(card)
    
    def copy_count(self, card_id, recursive):
        if card_id < 1 or card_id >= len(self.cards):
            return 0
        card : Card = self.cards[card_id-1]
        if not recursive:
            return card.win_count()
        copies_count = card.win_count()
        if copies_count == 0:
            return copies_count
        for copy_id in range(card_id+1,card_id+1+copies_count):
            copies_count += self.copy_count(copy_id,recursive)
        return copies_count
    
    def total_won_card(self):
        total_count = len(self.cards)
        for card in self.cards:
            total_count += self.copy_count(card.id,True)
        return total_count



if __name__ == "__main__":
    f = open("/media/alexandre/DATA/Sources/aoc2023/tests/day4.txt", "r")
    txt = f.read()
    sum = 0
    for line in txt.splitlines():
        card = Card()
        card.set_definition(line)
        sum+=card.win_value()
    print(sum)
    card_list = CardList()
    card_list.set_definition(txt)
    print(card_list.total_won_card())

    