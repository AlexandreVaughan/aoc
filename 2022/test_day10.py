from day10 import *

SAMPLE_PROGRAM = """addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop"""

def test_noinst():
    cpu = CPU()
    assert cpu.X() == 1

def test_noop():
    cpu = CPU()
    cpu.load("noop")
    cpu.run(max_cycles=1)
    assert cpu.X() == 1

def test_add():
    cpu = CPU()
    cpu.load("addx 3")
    cpu.run(max_cycles=1)
    assert cpu.X() == 1
    cpu.run(max_cycles=2)
    assert cpu.X() == 1
    cpu.run(max_cycles=3)
    assert cpu.X() == 4

def test_simple_sample():
    cpu = CPU()
    cpu.load("""noop
addx 3
addx -5""")
    cpu.run(3)
    assert cpu.X() == 1
    cpu.run(4)
    assert cpu.X() == 4
    cpu.run(5)
    assert cpu.X() == 4
    cpu.run(6)
    assert cpu.X() == -1

def test_long_sample():
    cpu = CPU()
    cpu.load(SAMPLE_PROGRAM)
    assert cpu.run(20) == 420
    assert cpu.X() == 21
    assert cpu.run(140) == 2940
    assert cpu.run(180) == 2880
    assert cpu.run(220) == 3960



def test_empty_screen():
    screen = Screen()
    assert screen.pixel_lit(0,0) == False
    assert screen.pixel_lit(5,39) == False
    assert screen.pixel_at_cycle(24) == (0,23)

def test_light_pixel():
    screen = Screen()
    screen.light_pixel(24,2)
    assert screen.pixel_lit(0,23) == False
    screen.light_pixel(24,24)
    assert screen.pixel_lit(0,23) == True
    screen.light_pixel(41,1)
    assert screen.pixel_lit(1,0) == True
    screen.light_pixel(41,12)
    assert screen.pixel_lit(1,11) == False

def test_string_to_screen():
    cpu = CPU()
    cpu.load(SAMPLE_PROGRAM)
    cpu.run(-1)
    assert cpu.screen.pixel_lit(0,0)
    assert not cpu.screen.pixel_lit(0,2)