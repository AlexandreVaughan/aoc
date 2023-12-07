from functools import cmp_to_key

FIVE_OF_A_KIND = 6
FOUR_OF_A_KIND = 5
FULL_HOUSE = 4
THREE_OF_A_KIND = 3
TWO_PAIR = 2
ONE_PAIR = 1
HIGH_CARD = 0


class Hand:
    def __init__(self, definition: str) -> None:
        self.definition = definition
        self.bid = 0
        self.type = self._find_type()


    
    def is_stronger(self,other):
        if  self.type != other.type:
            return self.type > other.type
        for idx in range(len(self.definition)):
            score_self = _map_score(self.definition[idx]) 
            score_other = _map_score(other.definition[idx])
            if score_self == score_other:
                continue
            return  score_self > score_other
        return False

    def _find_type(self):
        identical_count_list = self._create_identical_count_list()
        return _type_from_identical_count_list(identical_count_list)

    def _create_identical_count_list(self):
        identical_count_list = []
        current_number_identical = 1
        sorted_def = sorted(self.definition)
        previous_card = ''
        for card in sorted_def:
            if previous_card == '':
                previous_card = card
                continue
            if previous_card == card:
                current_number_identical += 1
            else :
                identical_count_list.append(current_number_identical)
                current_number_identical = 1
                previous_card = card
        identical_count_list.append(current_number_identical)
        return identical_count_list
    
def _type_from_identical_count_list(identical_count_list):
    max_identical = max(identical_count_list)
    if max_identical == 3 and len(identical_count_list) == 2:
        return FULL_HOUSE
    if max_identical == 2 and len(identical_count_list) == 3:
        return TWO_PAIR
    max_identical_type_map = {
        5 : FIVE_OF_A_KIND,
        4: FOUR_OF_A_KIND,
        3: THREE_OF_A_KIND,
        2: ONE_PAIR,
        1: HIGH_CARD
    }
    return max_identical_type_map[max_identical]

def _map_score(card):
    MAP_SCORE = {
        "2" : 2,
        "3" : 3,
        "4" : 4,
        "5" : 5,
        "6" : 6,
        "7" : 7,
        "8" : 8,
        "9" : 9,
        "T" : 10,
        "J" : 11,
        "Q" : 12,
        "K" : 13,
        "A" : 14,
    }
    return MAP_SCORE[card]

class HandList:
    def __init__(self, handlist_definition: str) -> None:
        self.hand_list = []
        self.ranked_list = []
        for hand_str in handlist_definition.splitlines():
            (hand_def,_,bid) = hand_str.partition(" ")
            hand = Hand(hand_def)
            hand.bid = int(bid)
            self.hand_list.append(hand)

    def rank_hands(self):
        self.ranked_list = sorted(self.hand_list, 
                                  key=cmp_to_key(
                                      lambda h1,h2: 1 if h1.is_stronger(h2) else -1))

    def rank(self,rank_number):
        return self.ranked_list[rank_number-1]
    
    def winnings(self):
        sum_winnings = 0
        for idx in range(len(self.ranked_list)):
            rank = idx+1
            hand = self.ranked_list[idx]
            sum_winnings += rank*hand.bid
        return sum_winnings
        
if __name__ == "__main__":
    f = open("D:\\Sources\\sample_projects\\aoc2023\\tests\\day7.txt", "r")
    txt = f.read()
    hand_list = HandList(txt)
    hand_list.rank_hands()
    print(hand_list.winnings())
