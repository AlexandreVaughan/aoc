
NOOP = 0
ADD = 1

class Screen():
    def __init__(self) -> None:
        self.erase()

    def erase(self):
        self.pixels = []
        for _ in range(6):
            self.pixels.append([False]*40)

    def pixel_lit(self,line,column):
        return self.pixels[line][column]

    def pixel_at_cycle(self,cycle):
        return ((cycle-1)//40,(cycle-1)%40)


    def light_pixel(self,cycle,sprite_position):
        potential_pos = []
        if sprite_position > 0:
            potential_pos.append(sprite_position-1)
        potential_pos.append(sprite_position)
        if sprite_position < 39:
            potential_pos.append(sprite_position+1)

        current_pos = (cycle-1)%40
        if not current_pos in potential_pos:
            return
        
        line,column = self.pixel_at_cycle(cycle)
        self.pixels[line][column] = True

    def to_string(self):
        result = ""
        for line in self.pixels:
            for column in line:
                result += "#" if column else "."
            result += '\n'
        return result



class CPU:
    def __init__(self) -> None:
        self._program = []
        self.screen = Screen()
        self._reset_state()
        self.instruction_map = {
            NOOP : (self._noop,1),
            ADD : (self._add,2)
        }
        

    def _reset_state(self):
        self._X = 1
        self.screen.erase()

    def X(self):
        return self._X
    


    def load(self, program : str):
        self._program = []
        for line in program.splitlines():
            inst_array = line.split()
            if inst_array[0] == "noop":
                self._program.append((NOOP, 0))
            elif inst_array[0] == "addx":
                self._program.append((ADD,int(inst_array[1])))

    def run(self,max_cycles : int):
        self._reset_state()
        cycle_count = 0
        for instruction, value in self._program:
            cycle_length = self.instruction_map[instruction][1]
            for _ in range(cycle_length):
                cycle_count += 1
                if max_cycles > 0 and cycle_count >= max_cycles:
                    return self._X * max_cycles
                self.screen.light_pixel(cycle_count,self._X)
            
            self.instruction_map[instruction][0](value)
        return self._X * max_cycles

    def _noop(self,_):
        pass

    def _add(self,value):
        self._X += value

with open('day10.txt') as file:
    program = file.read().strip()
    cpu = CPU()
    cpu.load(program)
    interesting_cycles = [20,60,100,140,180,220]
    sum = 0
    for cycle in interesting_cycles:
        sum += cpu.run(cycle)
    print(sum)
    cpu.run(-1)
    print(cpu.screen.to_string())