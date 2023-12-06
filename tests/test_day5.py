from day5 import Almanac, AlmanacMap

TEST_ALMANAC = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"""

def test_seeds():
    almanac = Almanac(TEST_ALMANAC)
    assert almanac.seeds == {79,14,55,13}

def test_generic_map():
    MAP = """50 98 2
52 50 48"""
    almanac_map = AlmanacMap(MAP)
    assert almanac_map.map_value(0) == 0
    assert almanac_map.map_value(1) == 1
    assert almanac_map.map_value(48) == 48
    assert almanac_map.map_value(49) == 49
    assert almanac_map.map_value(50) == 52
    assert almanac_map.map_value(51) == 53
    assert almanac_map.map_value(53) == 55
    assert almanac_map.map_value(96) == 98
    assert almanac_map.map_value(97) == 99
    assert almanac_map.map_value(98) == 50
    assert almanac_map.map_value(99) == 51

def test_soil_map():
    almanac = Almanac(TEST_ALMANAC)
    assert almanac.to_soil() == {81,14,57,13}

def test_location_map():
    almanac = Almanac(TEST_ALMANAC)
    assert almanac.to_location() == {82,43,86,35}


def test_min_location_seed_range():
    almanac = Almanac(TEST_ALMANAC, True)
    assert almanac.min_location() == 46