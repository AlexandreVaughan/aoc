from day8 import *

def test_visible_1tree():
    grid = [[1]]
    visible_count = count_visible_trees(grid)
    assert visible_count == 1

def test_visible_treeline():
    grid = [[1,8,5]]
    visible_count = count_visible_trees(grid)
    assert visible_count == 3

def test_visible_twotreelines():
    grid = [[1,8,5],
            [7,9,2]
            ]
    visible_count = count_visible_trees(grid)
    assert visible_count == 6

def test_visible_threelines_centralvisible():
    grid = [[1,8,5],
            [7,9,2],
            [1,2,3]
            ]
    visible_count = count_visible_trees(grid)
    assert visible_count == 9


def test_visible_threelines_centralinvisible():
    grid = [[1,8,5],
            [7,1,2],
            [1,2,3]
            ]
    visible_count = count_visible_trees(grid)
    assert visible_count == 8



def test_visible_fourlines():
    grid = [[1,8,5,4],
            [7,1,2,5],
            [2,1,3,4],
            [8,2,1,4],
            ]
    visible_count = count_visible_trees(grid)
    assert visible_count == 13


def test_aoc_example():
    grid = [
        [3,0,3,7,3],
        [2,5,5,1,2],
        [6,5,3,3,2],
        [3,3,5,4,9],
        [3,5,3,9,0],
    ]
    visible_count = count_visible_trees(grid)
    assert visible_count == 21

def test_scenic_score():
    forest = [
        [3,0,3,7,3],
        [2,5,5,1,2],
        [6,5,3,3,2],
        [3,3,5,4,9],
        [3,5,3,9,0],
    ]
    grid = Grid(forest)
    score = grid.scenic_score(0,2)
    assert score == 0
    score = grid.scenic_score(1,2)
    assert score == 4
    score = grid.scenic_score(3,2)
    assert score == 8