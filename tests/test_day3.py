from day3 import Engine

SCHEMATIC="""467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
"""

def test_simple_engine():
    engine = Engine()
    engine.add_serial((2,2),"124")
    engine.add_serial((8,5),"44")
    engine.add_symbol((8,4),"*")
    assert engine.symbol(0,0) == ""
    assert engine.symbol(8,4) != ""
    assert engine.serial(0,0) == ""
    assert engine.serial(2,2) == "124"
    assert engine.serial(3,2) == ""

def test_load_engine_schematic():
    engine = Engine()
    engine.load_schematic(SCHEMATIC)
    assert engine.serial(0,0) == '467'
    assert engine.serial(4,0) == ''
    assert engine.symbol(6,3) != ""
    assert engine.symbol(6,4) == ""
    assert engine.serial(0,4) == '617'


def test_is_valid_serial():
    engine = Engine()
    engine.load_schematic(SCHEMATIC)
    assert engine.is_valid_serial(0,0)
    assert not engine.is_valid_serial(4,0)
    assert not engine.is_valid_serial(5,0)
    assert not engine.is_valid_serial(7,5)
    assert engine.is_valid_serial(2,6)

def test_serial_sum():
    engine = Engine()
    engine.load_schematic(SCHEMATIC)
    assert engine.serial_sum() == 4361

def test_serial_sum_2():
    engine = Engine()
    schematic=""".......358..........31.....
...............415..*......
.........182..+.....873.756
..579...@.........$........
.....*.........875.........
......991..$............-..
"""
    engine.load_schematic(schematic)
    assert engine.serial_sum() == 1570

def test_serial_sum_2():
    engine = Engine()
    schematic="""...........................
...........................
...........................
...........................
...406*864.................
...........................
...........................
...........................
...........................
...........................
...........................
...........................
"""
    engine.load_schematic(schematic)
    assert engine.serial_sum() == 1270

def test_is_gear():
    engine = Engine()
    engine.load_schematic(SCHEMATIC)
    (serial1,serial2) = engine.gear(0,0)
    assert serial1 == 0 and serial2 == 0
    (serial1,serial2) = engine.gear(3,1)
    assert serial1 == 467 and serial2 == 35
    

def test_sum_gear_ratios():
    engine = Engine()
    engine.load_schematic(SCHEMATIC)
    assert engine.sum_gear_ratios() == 467835