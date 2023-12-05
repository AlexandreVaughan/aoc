class Almanac:
    def __init__(self, data: str) -> None:
        self.seeds = set()
        self.maps = {}
        data_lines = data.splitlines()
        self._read_seeds(data_lines)
        self._read_maps(data_lines)

    def _read_maps(self, data_lines):
        current_map_def = ""
        current_map_name = ""
        for line in data_lines[1:]:
            if line == "":
                continue
            if line.endswith("map:"):
                self._add_map(current_map_def, current_map_name)
                (current_map_name,_,_) = line.partition(" ")
                current_map_def = ""
            else:
                current_map_def += line+"\n"
        self._add_map(current_map_def, current_map_name)

    def _add_map(self, current_map_def, current_map_name):
        if current_map_def == "":
            return
        map = AlmanacMap(current_map_def)
        self.maps[current_map_name] = map
                    
    def _read_seeds(self, data_lines):
        seeds_line = data_lines[0]
        assert seeds_line.startswith("seeds:")
        seeds_str = seeds_line[7:]
        for seed_str in seeds_str.split(" "):
            self.seeds.add(int(seed_str))

    def to_soil(self):
        return self._map_set("seed-to-soil", self.seeds)
    
    def to_location(self):
        soil = self._map_set("seed-to-soil", self.seeds)
        fertilizer = self._map_set("soil-to-fertilizer", soil)
        water = self._map_set("fertilizer-to-water", fertilizer)
        light = self._map_set("water-to-light", water)
        temperature = self._map_set("light-to-temperature", light)
        humidity = self._map_set("temperature-to-humidity", temperature)
        return self._map_set("humidity-to-location", humidity)

    def min_location(self):
        return min(self.to_location())

    def _map_set(self, map_name, original_set):
        map = self.maps[map_name]
        mapped_set = set()
        for item in original_set:
            mapped_set.add(map.map(item))
        return mapped_set
        

class AlmanacMap:
    def __init__(self, data: str) -> None:
        self.ranges = []
        for data_line in data.splitlines():
            self.ranges.append(list(map(int,data_line.split(" "))))
            

    def map(self, value: int):
        for range in self.ranges:
            source_min = range[1]
            source_max = range[1]+range[2]
            if value < source_min or value > source_max:
                continue
            delta = value-source_min
            dest_min = range[0]
            return dest_min+delta
        return value
    
if __name__ == "__main__":
    f = open("D:\\Sources\\sample_projects\\aoc2023\\tests\\day5.txt", "r")
    txt = f.read()
    almanac = Almanac(txt)
    print(almanac.min_location())
