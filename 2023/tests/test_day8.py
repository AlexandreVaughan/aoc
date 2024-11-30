from day8 import DesertMap, is_ghost_ending_point

MAP_DEFINITION = """AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)"""

MAP_DEFINITION_2 = """AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)
"""

MAP_DEFINITION_3= """11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)"""

def test_desert_map():
    desert_map = DesertMap(MAP_DEFINITION)
    assert desert_map.left("AAA") == "BBB"
    assert desert_map.right("AAA") == "BBB"
    assert desert_map.left("BBB") == "AAA"
    assert desert_map.right("BBB") == "ZZZ"


def test_apply_instructions():
    desert_map = DesertMap(MAP_DEFINITION)
    assert desert_map.follow_instructions('R') == "BBB"
    assert desert_map.follow_instructions('RL') == "AAA"
    desert_map = DesertMap(MAP_DEFINITION_2)
    assert desert_map.follow_instructions('RL') == "ZZZ"


def test_find_destination_steps():
    desert_map = DesertMap(MAP_DEFINITION_2)
    assert desert_map.find_destination("RL") == 2
    desert_map = DesertMap(MAP_DEFINITION)
    assert desert_map.find_destination("LLR") == 6



def test_find_ghost_starting_points():
    desert_map = DesertMap(MAP_DEFINITION_3)
    assert desert_map.ghost_starting_points() == { '11A', '22A' }

def test_is_ghost_ending_point():
    assert is_ghost_ending_point('22Z')
    assert not is_ghost_ending_point('22X')

def test_find_ghost_destination():
    desert_map = DesertMap(MAP_DEFINITION_3)
    assert desert_map.find_ghost_destination('LR') == 6 