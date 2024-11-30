

class CubeSet:
    def __init__(self, set_definition: str) -> None:
        self.cubes = {
            "red" : 0,
            "green" : 0,
            "blue" : 0
        }
        self._read_definition(set_definition)

    def _read_definition(self, set_definition):
        for cube_type_count in set_definition.split(","):
            (count, _, cube_type) = cube_type_count.strip().partition(" ")
            self.cubes[cube_type] += int(count)
    
    def can_contain(self, other_cubeset):
        for cube_type,count in self.cubes.items():
            if not cube_type in other_cubeset.cubes:
                continue
            if count < other_cubeset.cubes[cube_type]:
                return False
        return True
    
    def power(self):
        product = 1
        for val in self.cubes.values():
            product *= val
        return product
    
class Game:
    def __init__(self, game_results: str) -> None:
        self.id = 0
        self.cubesets = []
        definition = self._extract_definition(game_results)
        self._load_games(definition)

    def _load_games(self, definition):
        for cubeset_definition in definition.split(";"):
            cubeset = CubeSet(cubeset_definition)
            self.cubesets.append(cubeset)

    def _extract_definition(self, game_results):
        definition = ""
        (id_str,_,definition) = game_results.strip().partition(":")
        (_,_,id) = id_str.partition(" ")
        self.id = int(id)
        return definition

    def is_valid(self, max_cubeset: CubeSet):
        for cubeset in self.cubesets:
            if not max_cubeset.can_contain(cubeset):
                return False
        return True
    
    def minimum_set(self):
        min_set = CubeSet("0 blue, 0 red, 0 green")
        for cubeset in self.cubesets:
            for cube_type, cube_count in cubeset.cubes.items():
                min_set.cubes[cube_type] = max(min_set.cubes[cube_type], cube_count)
        return min_set

if __name__ == "__main__":
    f = open("D:\\Sources\\sample_projects\\aoc2023\\tests\\day2.txt", "r")
    txt = f.read()
    sum_id = 0
    sum_powers = 0
    max_cubeset = CubeSet("12 red, 13 green, 14 blue")
    for game_def in txt.splitlines():
        game = Game(game_def)
        sum_powers += game.minimum_set().power()
        if not game.is_valid(max_cubeset):
            continue
        sum_id += game.id
    print(sum_id)
    print(sum_powers)

