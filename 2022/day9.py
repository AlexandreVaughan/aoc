RIGHT = 1
LEFT = -1
DOWN = -1
UP = 1


class Rope:
    def __init__(self, size=2) -> None:
        self._rope = [(0,0)]*size
        self._tail_visited_positions = set()
        self._tail_visited_positions.add(self._rope[-1])

    def head(self):
        return self._rope[0]
    
    def tail(self):
        return self._rope[-1]

    def tail_visited_positions(self):
        return self._tail_visited_positions
    
    def move_h(self,direction,length):
        for _ in range(1,length+1):
            self._move_h(direction)

    def _move_h(self,direction):
        self._rope[0] = (self._rope[0][0]+direction, self._rope[0][1])
        self._move_rope()
    
    def move_v(self,direction,length):
        for _ in range(1,length+1):
            self._move_v(direction)

    def _move_v(self,direction):
        self._rope[0] = (self._rope[0][0], self._rope[0][1]+direction)
        self._move_rope()
        

    def _move_rope(self):
        for idx in range(0,len(self._rope)-1):
            offset_hz = self._rope[idx][0]-self._rope[idx+1][0]
            offset_vert = self._rope[idx][1]-self._rope[idx+1][1]
            if offset_vert > 1:
                self._rope[idx+1] = (self._rope[idx][0] if abs(offset_hz) <= 1 else self._rope[idx+1][0] ,self._rope[idx][1]-1)
            if offset_vert < -1:
                self._rope[idx+1] = (self._rope[idx][0] if abs(offset_hz) <= 1 else self._rope[idx+1][0], self._rope[idx][1]+1)
            if offset_hz > 1:
                self._rope[idx+1] = (self._rope[idx][0]-1, self._rope[idx][1] if abs(offset_vert) <= 1 else self._rope[idx+1][1])
            if offset_hz < -1:
                self._rope[idx+1] = (self._rope[idx][0]+1, self._rope[idx][1] if abs(offset_vert) <= 1 else self._rope[idx+1][1])
        self._tail_visited_positions.add(self.tail())

    def exec_moves(self, moves_string : str):
        commands = {
            "U" : (self.move_v,UP),
            "D" : (self.move_v,DOWN),
            "R" : (self.move_h,RIGHT),
            "L" : (self.move_h,LEFT)
        }
        for line in moves_string.splitlines():
            command_steps = line.split()
            length = int(command_steps[1])
            command = command_steps[0]
            move_func = commands[command][0]
            direction = commands[command][1]
            move_func(direction,length)

with open('day9.txt') as file:
    commands = file.read().strip()
    rope = Rope(size=10)
    rope.exec_moves(commands)
    print(len(rope.tail_visited_positions()))
