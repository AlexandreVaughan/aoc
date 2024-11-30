from day3 import *


def test_split_rucksack():
    rucksack = "vJrwpWtwJgWrhcsFMMfFFhFp"
    comp1,comp2 = split_rucksack(rucksack)
    assert comp1 == "vJrwpWtwJgWr"
    assert comp2 == "hcsFMMfFFhFp"

def test_find_common_elem():
    rucksack1 = "vJrwpWtwJgWrhcsFMMfFFhFp"
    rucksack2 = "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL"
    common1 = rucksack_common_elem(rucksack1)
    assert common1 == "p"
    common2 = rucksack_common_elem(rucksack2)
    assert common2 == "L"


def test_score_common_elem():
    rucksack1 = "vJrwpWtwJgWrhcsFMMfFFhFp"
    rucksack2 = "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL"
    score1 = rucksack_score_common_elem(rucksack1)
    assert score1 == 16
    score2 = rucksack_score_common_elem(rucksack2)
    assert score2 == 38

def test_find_badge():
    group1_sacks = [ "vJrwpWtwJgWrhcsFMMfFFhFp",
        "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
        "PmmdzqPrVvPwwTWBwg"
    ]
    group1_badge = find_badge(group1_sacks)
    assert group1_badge == "r"
    group2_sacks = [ "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
        "ttgJtRGJQctTZtZT",
        "CrZsJsPPZsGzwwsLwLmpwMDw"
    ]
    group2_badge = find_badge(group2_sacks)
    assert group2_badge == "Z"
