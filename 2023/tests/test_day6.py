from day6 import Race, load_races, multiply_win_possibilities

def test_race_travel_distance():
    race = Race(7,9)
    assert race.travel_distance(0) == 0
    assert race.travel_distance(1) == 6
    assert race.travel_distance(2) == 10
    assert race.travel_distance(4) == 12
    assert race.travel_distance(7) == 0
    assert race.travel_distance(8) == 0
    

def test_race_count_win_possibilities():
    race = Race(7,9)
    assert race.count_win_possibilities() == 4
    race = Race(15,40)
    assert race.count_win_possibilities() == 8

RACES="""Time:      7  15   30
Distance:  9  40  200"""    
def test_load_races():
    races = load_races(RACES)
    assert len(races) == 3
    assert races[1].record_distance == 40

def test_multiply_win_possibilities():
    races = load_races(RACES)
    assert multiply_win_possibilities(races) == 288
