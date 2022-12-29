from day9 import *

def test_nomove():
    rope = Rope()
    assert rope.head() == (0,0)
    assert rope.tail() == (0,0)
    assert rope.tail_visited_positions() == { (0,0) }

def test_moveright1():
    rope = Rope()
    rope.move_h(RIGHT,1)
    assert rope.head() == (1,0)
    assert rope.tail() == (0,0)
    assert rope.tail_visited_positions() == { (0,0) }


def test_moveright2():
    rope = Rope()
    rope.move_h(RIGHT,2)
    assert rope.head() == (2,0)
    assert rope.tail() == (1,0)
    assert rope.tail_visited_positions() == { (0,0), (1,0), (2,0)}

def test_moveright4():
    rope = Rope()
    rope.move_h(RIGHT,4)
    assert rope.head() == (4,0)
    assert rope.tail() == (3,0)
    assert rope.tail_visited_positions() == { (0,0), (1,0), (2,0), (3,0), (4,0)}

def test_moveleft1():
    rope = Rope()
    rope.move_h(LEFT,1)
    assert rope.head() == (-1,0)
    assert rope.tail() == (0,0)
    assert rope.tail_visited_positions() == { (0,0) }


def test_moveright2():
    rope = Rope()
    rope.move_h(LEFT,2)
    assert rope.head() == (-2,0)
    assert rope.tail() == (-1,0)
    assert rope.tail_visited_positions() == { (0,0), (-1,0)}

def test_moveright4():
    rope = Rope()
    rope.move_h(LEFT,4)
    assert rope.head() == (-4,0)
    assert rope.tail() == (-3,0)
    assert rope.tail_visited_positions() == { (0,0), (-1,0), (-2,0), (-3,0) }


def test_moveup1():
    rope = Rope()
    rope.move_v(UP,1)
    assert rope.head() == (0,1)
    assert rope.tail() == (0,0)
    assert rope.tail_visited_positions() == { (0,0) }


def test_moveup2():
    rope = Rope()
    rope.move_v(UP,2)
    assert rope.head() == (0,2)
    assert rope.tail() == (0,1)
    assert rope.tail_visited_positions() == { (0,0), (0,1) }

def test_moveup4():
    rope = Rope()
    rope.move_v(UP,4)
    assert rope.head() == (0,4)
    assert rope.tail() == (0,3)
    assert rope.tail_visited_positions() == { (0,0), (0,1), (0,2), (0,3) }

def test_movedown1():
    rope = Rope()
    rope.move_v(DOWN,1)
    assert rope.head() == (0,-1)
    assert rope.tail() == (0,0)
    assert rope.tail_visited_positions() == { (0,0)}


def test_movedown2():
    rope = Rope()
    rope.move_v(DOWN,2)
    assert rope.head() == (0,-2)
    assert rope.tail() == (0,-1)
    assert rope.tail_visited_positions() == { (0,0), (0,-1)}

def test_movedown4():
    rope = Rope()
    rope.move_v(DOWN,4)
    assert rope.head() == (0,-4)
    assert rope.tail() == (0,-3)
    assert rope.tail_visited_positions() == { (0,0), (0,-1), (0,-2), (0,-3) }

def test_movediagonally_h_first():
    rope = Rope()
    rope.move_h(RIGHT,3)
    rope.move_v(UP, 3)
    assert rope.head() == (3,3)
    assert rope.tail() == (3,2)
    assert rope.tail_visited_positions() == { (0,0), (1,0), (2,0), (3,1), (3,2)  }

def test_movediagonally_v_first():
    rope = Rope()
    rope.move_v(UP, 3)
    rope.move_h(RIGHT,3)
    assert rope.head() == (3,3)
    assert rope.tail() == (2,3)
    assert rope.tail_visited_positions() == { (0,0), (0,1), (0,2), (1,3), (2,3)  }

def test_sample():
    rope = Rope()
    rope.move_h(RIGHT,4)
    rope.move_v(UP,4)
    rope.move_h(LEFT,3)
    rope.move_v(DOWN,1)
    rope.move_h(RIGHT,4)
    rope.move_v(DOWN,1)
    rope.move_h(LEFT,5)
    rope.move_h(RIGHT,2)
    assert(len(rope.tail_visited_positions()) == 13)


def test_sample_size10_simple():
    rope = Rope(size=10)
    rope.move_h(RIGHT,4)
    rope.move_v(UP,4)
    rope.move_h(LEFT,3)
    rope.move_v(DOWN,1)
    rope.move_h(RIGHT,4)
    rope.move_v(DOWN,1)
    rope.move_h(LEFT,5)
    rope.move_h(RIGHT,2)
    assert(len(rope.tail_visited_positions()) == 1)

def test_sample_size10_advanced():
    rope = Rope(size=10)
    moves = """R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20
"""
    rope.exec_moves(moves)
    assert(len(rope.tail_visited_positions()) == 36)