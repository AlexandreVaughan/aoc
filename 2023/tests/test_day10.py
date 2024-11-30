from day10 import *

SIMPLE_LOOP = """.....
.S-7.
.|.|.
.L-J.
....."""

OTHER_LOOP="""-L|F7
7S-7|
L|7||
-L-J|
L|-JF"""

COMPLEX_LOOP="""7-F7-
.FJ|7
SJLL7
|F--J
LJ.LJ"""


COMPLEX_LOOP_NEST_1="""...........
.S-------7.
.|F-----7|.
.||.....||.
.||.....||.
.|L-7.F-J|.
.|..|.|..|.
.L--J.L--J.
..........."""

COMPLEX_LOOP_NEST_2="""..........
.S------7.
.|F----7|.
.||....||.
.||....||.
.|L-7F-J|.
.|..||..|.
.L--JL--J.
.........."""

COMPLEX_LOOP_NEST_3="""FF7FSF7F7F7F7F7F---7
L|LJ||||||||||||F--J
FL-7LJLJ||||||LJL-77
F--JF--7||LJLJ7F7FJ-
L---JF-JLJ.||-FJLJJ7
|F|F-JF---7F7-L7L|7|
|FFJF7L7F-JF7|JL---7
7-L-JL7||F7|L7F-7F7|
L.L7LFJ|||||FJL7||LJ
L7JLJL-JLJLJL--JLJ.L"""

def test_allowed_directions():
    assert Pipe(".").allowed_directions == []
    assert Pipe("|").allowed_directions == [NORTH,SOUTH]
    assert Pipe("-").allowed_directions == [EAST,WEST]
    assert Pipe("J").allowed_directions == [NORTH,WEST]
    assert Pipe("7").allowed_directions == [SOUTH,WEST]
    assert Pipe("L").allowed_directions == [NORTH,EAST]
    assert Pipe("F").allowed_directions == [SOUTH,EAST]
    assert Pipe("S").allowed_directions == [NORTH,SOUTH,EAST,WEST]

def test_pipe_grid():
    pipe_grid = PipeGrid(SIMPLE_LOOP)
    assert pipe_grid.directions(0,0) == []
    assert pipe_grid.starting_point == (1,1)
    assert pipe_grid.directions(3,1) == [SOUTH,WEST]
    assert pipe_grid.directions(-1,1) == []
    assert pipe_grid.directions(1,90) == []
    
def test_starting_point_directions():
    pipe_grid = PipeGrid(SIMPLE_LOOP)
    assert pipe_grid.directions(*pipe_grid.starting_point) == [SOUTH,EAST]

    pipe_grid = PipeGrid(OTHER_LOOP)
    assert pipe_grid.directions(*pipe_grid.starting_point) == [SOUTH,EAST]

def test_distance_simple_grid():
    pipe_grid = PipeGrid(SIMPLE_LOOP)
    pipe_grid.find_distances()
    assert pipe_grid.distance(*pipe_grid.starting_point) == 0
    assert pipe_grid.distance(2,1) == 1
    assert pipe_grid.distance(3,1) == 2
    assert pipe_grid.distance(3,3) == 4

def test_max_distance():
    pipe_grid = PipeGrid(SIMPLE_LOOP)
    pipe_grid.find_distances()
    assert pipe_grid.max_distance() == 4
    pipe_grid = PipeGrid(OTHER_LOOP)
    pipe_grid.find_distances()
    assert pipe_grid.max_distance() == 4
    pipe_grid = PipeGrid(COMPLEX_LOOP)
    pipe_grid.find_distances()
    assert pipe_grid.max_distance() == 8

def test_is_enclosed():
    pipe_grid = PipeGrid(SIMPLE_LOOP)
    pipe_grid.find_distances()
    assert pipe_grid.count_enclosed() == 1
    pipe_grid = PipeGrid(COMPLEX_LOOP_NEST_1)
    pipe_grid.find_distances()
    assert pipe_grid.count_enclosed() == 4
    pipe_grid = PipeGrid(COMPLEX_LOOP_NEST_2)
    pipe_grid.find_distances()
    assert pipe_grid.count_enclosed() == 4
    pipe_grid = PipeGrid(COMPLEX_LOOP_NEST_3)
    pipe_grid.find_distances()
    assert pipe_grid.count_enclosed() == 10