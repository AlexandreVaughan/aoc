from day4 import Card

def test_nowin():
    card = Card()
    card.winning_numbers = {12,13,14}
    card.card_numbers = {20,15,16}
    assert card.win_value() == 0

def test_onewin():
    card = Card()
    card.winning_numbers = {12,13,14}
    card.card_numbers = {20,14,16}
    assert card.win_value() == 1

def test_twowins():
    card = Card()
    card.winning_numbers = {12,13,14}
    card.card_numbers = {20,14,13}
    assert card.win_value() == 2

def test_threewins():
    card = Card()
    card.winning_numbers = {12,13,14}
    card.card_numbers = {12,14,13}
    assert card.win_value() == 4

def test_fourwins():
    card = Card()
    card.winning_numbers = {41,48,83,86,17}
    card.card_numbers = {83,86,6,31,17,9,48,53}
    assert card.win_value() == 8

def test_card_definition():
    card = Card()
    card.set_definition("Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53")
    assert card.winning_numbers == {41,48,83,86,17}
    assert card.card_numbers == {83,86,6,31,17,9,48,53}