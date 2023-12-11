from day11 import ImageField, distance

IMAGE_FIELD = """...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#....."""


def test_image_field():
    image_field = ImageField(IMAGE_FIELD)
    assert image_field.size() == (10,10)
    assert not image_field.has_galaxy(0,0)
    assert image_field.has_galaxy(3,0)
    assert image_field.has_galaxy(0,2)
    assert image_field.has_galaxy(7,1)
    assert not image_field.has_galaxy(8,1)
    

def test_image_field_expand():
    image_field = ImageField(IMAGE_FIELD)
    image_field.expand()
    assert image_field.size() == (13,12)
    assert not image_field.has_galaxy(0,0)
    assert not image_field.has_galaxy(3,0)
    assert image_field.has_galaxy(4,0)
    assert image_field.has_galaxy(0,11)

def test_find_galaxies():
    image_field = ImageField(IMAGE_FIELD)
    image_field.expand()
    galaxies = image_field.find_galaxies()
    assert len(galaxies) == 9
    assert galaxies[1] == (9,1)

def test_distance():
    image_field = ImageField(IMAGE_FIELD)
    image_field.expand()
    galaxies = image_field.find_galaxies()
    assert distance(galaxies[4],galaxies[8]) == 9
    assert distance(galaxies[0],galaxies[6]) == 15
    assert distance(galaxies[2],galaxies[5]) == 17
    assert distance(galaxies[7],galaxies[8]) == 5

def test_sum_distance():
    image_field = ImageField(IMAGE_FIELD)
    image_field.expand()
    assert image_field.sum_distance() == 374


def test_sum_distance_different_offsets():
    image_field = ImageField(IMAGE_FIELD)
    image_field.expand(10)
    assert image_field.sum_distance() == 1030
    image_field = ImageField(IMAGE_FIELD)
    image_field.expand(100)
    assert image_field.sum_distance() == 8410