from day2 import CubeSet, Game

def test_cubeset():
    cubeset = CubeSet("1 green, 2 blue, 3 red")
    assert cubeset.cubes["green"] == 1
    assert cubeset.cubes["blue"] == 2
    assert cubeset.cubes["red"] == 3
    cubeset = CubeSet("1 red, 2 green, 6 blue")
    assert cubeset.cubes["green"] == 2
    assert cubeset.cubes["blue"] == 6
    assert cubeset.cubes["red"] == 1

def test_cubeset_can_contain():
    cubeset = CubeSet("3 green, 4 blue, 1 red")
    max_cubeset = CubeSet("12 red, 13 green, 14 blue")
    assert max_cubeset.can_contain(cubeset)
    cubeset = CubeSet("3 green, 4 blue, 15 red")
    assert not max_cubeset.can_contain(cubeset)

def test_game():
    game = Game("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green")
    assert game.id == 1
    game = Game("Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red")
    assert game.id == 3
    assert len(game.cubesets) == 3
    assert game.cubesets[1].cubes["blue"] == 5

def test_game_valid():
    max_cubeset = CubeSet("12 red, 13 green, 14 blue")
    game = Game("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green")
    assert game.is_valid(max_cubeset)
    game = Game("Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red")
    assert not game.is_valid(max_cubeset)