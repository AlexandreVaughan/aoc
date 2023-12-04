from day4 import Card, CardList

def test_nowin():
    card = Card()
    card.winning_numbers = {12,13,14}
    card.card_numbers = {20,15,16}
    assert card.win_value() == 0
    assert card.win_count() == 0

def test_onewin():
    card = Card()
    card.winning_numbers = {12,13,14}
    card.card_numbers = {20,14,16}
    assert card.win_value() == 1
    assert card.win_count() == 1

def test_twowins():
    card = Card()
    card.winning_numbers = {12,13,14}
    card.card_numbers = {20,14,13}
    assert card.win_value() == 2
    assert card.win_count() == 2

def test_threewins():
    card = Card()
    card.winning_numbers = {12,13,14}
    card.card_numbers = {12,14,13}
    assert card.win_value() == 4
    assert card.win_count() == 3

def test_fourwins():
    card = Card()
    card.winning_numbers = {41,48,83,86,17}
    card.card_numbers = {83,86,6,31,17,9,48,53}
    assert card.win_value() == 8
    assert card.win_count() == 4

def test_card_definition():
    card = Card()
    card.set_definition("Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53")
    assert card.winning_numbers == {41,48,83,86,17}
    assert card.card_numbers == {83,86,6,31,17,9,48,53}
    assert card.id == 1

CARD_LIST_DEF = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""

def test_card_list():
    card_list = CardList()
    card_list.set_definition(CARD_LIST_DEF)
    assert len(card_list.cards) == 6
    assert card_list.cards[2].id == 3

def test_card_list_copy_1card_1level():
    card_list = CardList()
    card_list.set_definition(CARD_LIST_DEF)
    assert card_list.copy_count(1,False) == 4

def test_card_list_copy_1card_recursive():
    card_list = CardList()
    card_list.set_definition(CARD_LIST_DEF)
    assert card_list.copy_count(1,True) == 14

def test_card_list_total_won_cards():
    card_list = CardList()
    card_list.set_definition(CARD_LIST_DEF)
    assert card_list.total_won_card() == 30

