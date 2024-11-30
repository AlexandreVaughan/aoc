from queue import Queue

NORTH = 0
SOUTH = 1
EAST = 2
WEST = 3

class Pipe:
    def __init__(self,definition: str) -> None:
        self.allowed_directions = _allowed_directions(definition)
        self.distance = -1
        self.definition = definition

    def in_loop(self):
        return self.distance != -1
    
    def has_vertical_component(self):
        return self.definition in "|JL"

class PipeGrid:
    def __init__(self, definition:str) -> None:
        self.grid = []
        self.starting_point = (0,0)
        self._read_grid(definition)
        self._find_startingpoint_directions()

    def _read_grid(self,definition:str):
        line_idx=0
        for line in definition.splitlines():
            grid_line = []
            column_idx =0
            for cell in line:
                grid_line.append(Pipe(cell))
                if cell == "S":
                    self.starting_point = (column_idx,line_idx)
                column_idx+=1
            self.grid.append(grid_line)
            line_idx +=1

    def _find_startingpoint_directions(self):
        final_directions = []
        (xstart,ystart) = self.starting_point
        for direction in self.directions(xstart,ystart):
            new_point = _move(xstart,ystart,direction)
            if not _opposite_direction(direction) in self.directions(*new_point):
                continue
            final_directions.append(direction)
        self.grid[ystart][xstart].allowed_directions = final_directions
        
    def directions(self,x,y):
        pipe = self._pipe_at(x,y)
        if pipe is None:
            return []
        return pipe.allowed_directions
    
    def distance(self,x,y):
        pipe = self._pipe_at(x,y)
        if pipe is None:
            return -1
        return pipe.distance
    
    def _pipe_at(self,x,y) -> Pipe:
        if x < 0 or y < 0:
            return None
        if x >= len(self.grid[0]) or y >= len(self.grid):
            return None
        return self.grid[y][x]
    
    def find_distances(self):
        queue = Queue()
        queue.put((*self.starting_point,0))
        while not queue.empty():
            (x,y,distance) = queue.get()
            pipe = self._pipe_at(x,y)
            if pipe is None:
                continue
            if pipe.distance != -1:
                continue
            pipe.distance = distance
            for direction in self.directions(x,y):
                queue.put((*(_move(x,y,direction)),distance+1))
        
    def max_distance(self):
        max_dist = 0
        for line in self.grid:
            for pipe in line:
                max_dist = max(max_dist,pipe.distance)
        return max_dist
    
    def count_enclosed(self):
        count=0
        max_y = len(self.grid)
        max_x = len(self.grid[0])
        for y in range(max_y):
            enclosed = False
            for x in range(max_x):
                pipe = self._pipe_at(x,y)
                if pipe.in_loop():
                    if pipe.has_vertical_component():
                        enclosed = not enclosed
                    if (x,y) == self.starting_point and NORTH in pipe.allowed_directions:
                        enclosed = not enclosed
                else:
                    count += int(enclosed)
        return count


def _allowed_directions(pipe: str):
    DIRECTION_MAP = {
        ".": [],
        "|": [NORTH,SOUTH],
        "-": [EAST,WEST],
        "J": [NORTH,WEST],
        "7": [SOUTH,WEST],
        "L": [NORTH,EAST],
        "F": [SOUTH,EAST],
        "S": [NORTH,SOUTH,EAST,WEST],
    }
    return DIRECTION_MAP[pipe]

def _move(x,y,direction):
    move_map = {
        NORTH: (x,y-1),
        SOUTH: (x,y+1),
        WEST: (x-1,y),
        EAST: (x+1,y)
    }
    return move_map[direction]

def _opposite_direction(direction):
    direction_map = {
        NORTH: SOUTH,
        SOUTH: NORTH,
        WEST: EAST,
        EAST: WEST
    } 
    return direction_map[direction] 

if __name__ == "__main__":
    f = open("D:\\Sources\\sample_projects\\aoc2023\\tests\\day10.txt", "r")
    txt = f.read()
    pipe_grid = PipeGrid(txt)
    pipe_grid.find_distances()
    print(pipe_grid.max_distance())
    print(pipe_grid.count_enclosed())