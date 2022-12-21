
from day5 import *

def test_crate_top():
    ship = Ship(3)
    ship.put_crate(1, 'Z')
    ship.put_crate(1, 'N')
    ship.put_crate(2, 'M')
    ship.put_crate(2, 'C')
    assert ship.top() == 'NC'
    ship.put_crate(2, 'D')
    ship.put_crate(3, 'P')
    assert ship.top() == 'NDP'

def test_one_move():
    ship = Ship(3)
    ship.put_crate(1, 'Z')
    ship.put_crate(1, 'N')
    ship.put_crate(2, 'M')
    ship.put_crate(2, 'C')
    ship.put_crate(2, 'D')
    ship.put_crate(3, 'P')
    ship.move_9000(1,2,1)
    assert ship.top() == 'DCP'

def test_move_three():
    ship = Ship(3)
    ship.put_crate(1, 'Z')
    ship.put_crate(1, 'N')
    ship.put_crate(2, 'M')
    ship.put_crate(2, 'C')
    ship.put_crate(2, 'D')
    ship.put_crate(3, 'P')
    ship.move_9000(1,2,1)
    ship.move_9000(3,1,3)
    assert ship.top() == 'CZ'

def test_move_9000_combined():
    ship = Ship(3)
    ship.put_crate(1, 'Z')
    ship.put_crate(1, 'N')
    ship.put_crate(2, 'M')
    ship.put_crate(2, 'C')
    ship.put_crate(2, 'D')
    ship.put_crate(3, 'P')
    ship.move_9000(1,2,1)
    ship.move_9000(3,1,3)
    ship.move_9000(2,2,1)
    ship.move_9000(1,1,2)
    assert ship.top() == 'CMZ'

def test_move_9001_combined():
    ship = Ship(3)
    ship.put_crate(1, 'Z')
    ship.put_crate(1, 'N')
    ship.put_crate(2, 'M')
    ship.put_crate(2, 'C')
    ship.put_crate(2, 'D')
    ship.put_crate(3, 'P')
    ship.move_9001(1,2,1)
    ship.move_9001(3,1,3)
    ship.move_9001(2,2,1)
    ship.move_9001(1,1,2)
    assert ship.top() == 'MCD'

def test_move_order():
    ship = Ship(3)
    ship.put_crate(1, 'Z')
    ship.put_crate(1, 'N')
    ship.put_crate(2, 'M')
    ship.put_crate(2, 'C')
    ship.put_crate(2, 'D')
    ship.put_crate(3, 'P')
    ship.move_order("move 1 from 2 to 1")
    ship.move_order("move 3 from 1 to 3")
    ship.move_order("move 2 from 2 to 1")
    ship.move_order("move 1 from 1 to 2")
    assert ship.top() == 'CMZ'

def test_init_ship():
    ship_desc = """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 
    """
    ship = Ship(0)
    ship.load_desc(ship_desc)
    ship.move_order("move 1 from 2 to 1")
    ship.move_order("move 3 from 1 to 3")
    ship.move_order("move 2 from 2 to 1")
    ship.move_order("move 1 from 1 to 2")
    assert ship.top() == 'CMZ'
