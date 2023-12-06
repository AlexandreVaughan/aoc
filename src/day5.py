import sys

class Almanac:
    def __init__(self, data: str, seed_as_range = False) -> None:
        self.seeds = set()
        self.seeds_as_range = seed_as_range
        self.maps = [None]*7
        data_lines = data.splitlines()
        self._read_seeds(data_lines, seed_as_range)
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
        map_toidx = { 
            "seed-to-soil": 0,
            "soil-to-fertilizer": 1,
            "fertilizer-to-water": 2,
            "water-to-light": 3,
            "light-to-temperature": 4,
            "temperature-to-humidity": 5,
            "humidity-to-location": 6
        }
        map = AlmanacMap(current_map_def)
        self.maps[map_toidx[current_map_name]]= map
                    
    def _read_seeds(self, data_lines, seed_as_range):
        seeds_line = data_lines[0]
        assert seeds_line.startswith("seeds:")
        seeds_str = seeds_line[7:]
        seed_start = -1
        for seed_str in seeds_str.split(" "):
            if not seed_as_range:
                self.seeds.add(int(seed_str))
            else:
                if (seed_start == -1):
                    seed_start = int(seed_str)
                    continue
                seed_range = int(seed_str)
                self.seeds.add((seed_start,seed_range))
                seed_start = -1


    def to_soil(self):
        if self.seeds_as_range:
            return {} # not supported
        mapped_set = set()
        for item in self.seeds:
            mapped_set.add(self._map_value(0,item))
        return mapped_set
    
    def to_location(self):
        if self.seeds_as_range:
            return {} # not supported
        mapped_set = set()
        for item in self.seeds:
            mapped_set.add(self._to_location_value(item))
        return mapped_set

    def min_location(self):
        if not self.seeds_as_range:
            return min(self.to_location())
        min_value = 2**31
        intervals = self._to_location_intervals(list(self.seeds))
        for (start,_) in intervals:
            min_value = min(min_value,start)
        return min_value
    
    def _map_value(self, map_id, value):
        map = self.maps[map_id]
        return map.map_value(value)
    
    def _map_intervals(self, map_id, value):
        map = self.maps[map_id]
        return map.map_intervals(value)
    
    def _to_location_value(self,seed_value):
        value = self._map_value(0, seed_value)
        value = self._map_value(1, value)
        value = self._map_value(2, value)
        value = self._map_value(3, value)
        value = self._map_value(4, value)
        value = self._map_value(5, value)
        return self._map_value(6, value)
    
    def _to_location_intervals(self,seed_range):
        interval = self._map_intervals(0, seed_range)
        interval = self._map_intervals(1, interval)
        interval = self._map_intervals(2, interval)
        interval = self._map_intervals(3, interval)
        interval = self._map_intervals(4, interval)
        interval = self._map_intervals(5, interval)
        return self._map_intervals(6, interval)
        

class AlmanacMap:
    def __init__(self, data: str) -> None:
        self.ranges = []
        for data_line in data.splitlines():
            self.ranges.append(list(map(int,data_line.split(" "))))
        self.ranges = sorted(self.ranges,key=lambda x: x[1])
            
    def map_value(self, value: int):
        for range in self.ranges:
            source_min = range[1]
            source_max = range[1]+range[2]
            if value < source_min or value >= source_max:
                continue
            delta = value-source_min
            dest_min = range[0]
            return dest_min+delta
        return value
    
    def map_intervals(self, intervals):
        computed_ranges = []
        for interval in intervals:
            (start,count)=interval
            source_start_val = start
            source_end_val = start+count
            current_source_start_val = source_start_val
            for current_range in self.ranges:
                current_range_source_start = current_range[1]
                current_range_dest_start = current_range[0] 
                current_range_count= current_range[2] 
                if current_source_start_val >= current_range_source_start+current_range_count:
                    continue
                if current_source_start_val < current_range_source_start:
                    computed_ranges.append((current_source_start_val,current_range_source_start-current_source_start_val))
                    current_source_start_val = current_range_source_start
                
                delta = current_source_start_val-current_range_source_start
                computed_range_start = current_range_dest_start+delta
                current_source_end_val = min(source_end_val,current_source_start_val+current_range_count)
                delta = current_source_end_val-current_range_source_start
                if delta < 0:
                    continue
                computed_range_end = current_range_dest_start+delta
                computed_ranges.append((computed_range_start,computed_range_end-computed_range_start))
                current_source_start_val = current_source_end_val
                if current_source_end_val >= source_end_val:
                    break
            if (current_source_start_val < start+count):
                computed_ranges.append((current_source_start_val,start+count-current_source_start_val))
        return computed_ranges



            
    
    
if __name__ == "__main__":
    f = open("/media/alexandre/DATA/Sources/aoc2023/tests/day5.txt", "r")
    txt = f.read()
    almanac = Almanac(txt)
    print(almanac.min_location())
    almanac = Almanac(txt,True)
    print(almanac.min_location())