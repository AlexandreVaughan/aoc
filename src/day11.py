GALAXY='#'
EMPTY_SPACE = '.'

class ImageField:
    def __init__(self,definition) -> None:
        self.galaxies = []
        self._size = (0,0)
        self._read_galaxies(definition)
    
    def _read_galaxies(self,definition):
        y = 0
        lines = definition.splitlines()
        self._size = (len(lines[0]),len(lines))
        for line in lines:
            x = 0
            for char in line:
                if char != GALAXY:
                    x+=1
                    continue
                self.galaxies.append((x,y))
                x+=1
            y+=1

    def expand(self,expansion_rate=2):
        expanded_galaxies = []
        for galaxy in self.galaxies:
            expanded_galaxies.append(self._expand_coordinates(galaxy,expansion_rate))
        self._size = self._expand_coordinates(self._size,expansion_rate)
        self.galaxies = expanded_galaxies

    def _expand_coordinates(self,coord, expansion_rate):
        (gx,gy) = coord
        (newx,newy) = (gx, gy)
        for x in range(gx):
            if self._is_empty_column(x):
                newx += expansion_rate-1
        for y in range(gy):
            if self._is_empty_line(y):
                newy += expansion_rate-1
        return (newx,newy)




    def has_galaxy(self,x,y):
        return (x,y) in self.galaxies

    def size(self):
        return self._size
    
    def _is_empty_line(self,y):
        for galaxy in self.galaxies:
            (_,gy) = galaxy
            if gy == y:
                return False
        return True

    
    def _is_empty_column(self,x):
        for galaxy in self.galaxies:
            (gx,_) = galaxy
            if gx == x:
                return False
        return True
    
    def _add_line_after(self,y):
        (max_x,_) = self.size()
        line = EMPTY_SPACE*max_x
        self.image.insert(y+1,line)

    def _add_column_after(self,x):
        for line in self.image:
            line.insert(x+1,EMPTY_SPACE)

    def find_galaxies(self):
        return self.galaxies
    
    def sum_distance(self):
        galaxies = self.find_galaxies()
        possible_pairs = [(a, b) for idx, a in enumerate(galaxies) for b in galaxies[idx + 1:]]
        sum = 0
        for (galaxy1,galaxy2) in possible_pairs:
            sum += distance(galaxy1,galaxy2)
        return sum


def distance(galaxy1,galaxy2):
    (x1,y1) = galaxy1
    (x2,y2) = galaxy2
    return abs(x2-x1)+abs(y2-y1)

if __name__ == "__main__":
    f = open("D:\\Sources\\sample_projects\\aoc2023\\tests\\day11.txt", "r")
    txt = f.read()
    image_field = ImageField(txt)
    image_field.expand()
    print(image_field.sum_distance())
    image_field = ImageField(txt)
    image_field.expand(1000000)
    print(image_field.sum_distance())