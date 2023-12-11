GALAXY='#'
EMPTY_SPACE = '.'

class ImageField:
    def __init__(self,definition) -> None:
        self.image = []
        for line in definition.splitlines():
            self.image.append([*line])

    def expand(self):
        (max_x,max_y) = self.size()
        for x in reversed(range(max_x)):
            if not self._is_empty_column(x):
                continue
            self._add_column_after(x)
        for y in reversed(range(max_y)):
            if not self._is_empty_line(y):
                continue
            self._add_line_after(y)


    def has_galaxy(self,x,y):
        return self.image[y][x] == GALAXY

    def size(self):
        return (len(self.image[0]),len(self.image))
    
    def _is_empty_line(self,y):
        (max_x,_) = self.size()
        for x in range(max_x):
            if self.has_galaxy(x,y):
                return False
        return True
    
    def _is_empty_column(self,x):
        (_,max_y) = self.size()
        for y in range(max_y):
            if self.has_galaxy(x,y):
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
        (max_x,max_y) = self.size()
        galaxies = []
        for y in range(max_y):
            for x in range(max_x):
                if not self.has_galaxy(x,y):
                    continue
                galaxies.append((x,y))
        return galaxies
    
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