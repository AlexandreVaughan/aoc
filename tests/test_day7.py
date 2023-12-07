from day7 import *

def test_hand_type():
    hand = Hand("AAAAA")
    assert hand.type == FIVE_OF_A_KIND
    hand = Hand("AA8AA")
    assert hand.type == FOUR_OF_A_KIND
    hand = Hand("23332")
    assert hand.type == FULL_HOUSE
    hand = Hand("TTT98")
    assert hand.type == THREE_OF_A_KIND
    hand = Hand("23432")
    assert hand.type == TWO_PAIR
    hand = Hand("A23A4")
    assert hand.type == ONE_PAIR
    hand = Hand("23456")
    assert hand.type == HIGH_CARD

def test_hand_type_joker():
    hand = Hand("QJJQ2")
    assert hand.type == TWO_PAIR
    hand = Hand("QJJQ2", joker_rule_active=True)
    assert hand.type == FOUR_OF_A_KIND
    hand = Hand("JJJJJ", joker_rule_active=True)
    assert hand.type == FIVE_OF_A_KIND


def test_is_stronger_different_types():
    hand1 = Hand("AAAAA")
    hand2 = Hand("TTT98")
    assert hand1.is_stronger(hand2)
    assert not hand2.is_stronger(hand1)
    hand1 = Hand("23456")
    hand2 = Hand("A23A4")
    assert not hand1.is_stronger(hand2)

def test_is_stronger_same_type():
    hand1 = Hand("33332")
    hand2 = Hand("2AAAA")
    assert hand1.is_stronger(hand2)
    assert not hand2.is_stronger(hand1)
    hand1 = Hand("77888")
    hand2 = Hand("77788")
    assert hand1.is_stronger(hand2)
    assert not hand2.is_stronger(hand1)
    hand1 = Hand("KK677")
    hand2 = Hand("KTJJT")
    assert hand1.is_stronger(hand2)
    assert not hand2.is_stronger(hand1)
    hand1 = Hand("32T3K")
    hand2 = Hand("KTJJT")
    assert hand2.is_stronger(hand1)
    assert not hand1.is_stronger(hand2)

def test_is_stronger_same_type_joker():

    hand1 = Hand("JKKK2",joker_rule_active=True)
    hand2 = Hand("QQQQ2", joker_rule_active=True)
    assert not hand1.is_stronger(hand2)



HAND_LIST_DEF = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483"""

def test_hand_list():
    hand_list = HandList(HAND_LIST_DEF)
    assert len(hand_list.hand_list) == 5
    assert hand_list.hand_list[2].bid == 28
    assert hand_list.hand_list[1].definition == "T55J5"

def test_hand_list_rank():
    hand_list = HandList(HAND_LIST_DEF)
    hand_list.rank_hands()
    assert hand_list.rank(1).definition == "32T3K"
    assert hand_list.rank(2).definition == "KTJJT"
    assert hand_list.rank(3).definition == "KK677"


def test_hand_list_winnings():
    hand_list = HandList(HAND_LIST_DEF)
    hand_list.rank_hands()
    assert hand_list.winnings() == 6440


def test_hand_list_winnings_joker():
    hand_list = HandList(HAND_LIST_DEF, joker_rule_active=True)
    hand_list.rank_hands()
    assert hand_list.winnings() == 5905