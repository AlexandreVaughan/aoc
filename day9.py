RIGHT = 1
LEFT = -1
DOWN = -1
UP = 1


class Rope:
    def __init__(self) -> None:
        self._head = (0,0)
        self._tail = (0,0)
        self._tail_visited_positions = set()
        self._tail_visited_positions.add(self._tail)

    def head(self):
        return self._head
    
    def tail(self):
        return self._tail

    def tail_visited_positions(self):
        return self._tail_visited_positions
    
    def move_h(self,direction,length):
        for _ in range(1,length+1):
            self._move_h(direction)

    def _move_h(self,direction):
        self._head = (self._head[0]+direction, self._head[1])
        if self._head[0]-self._tail[0]>1:
            self._tail = (self._head[0]-1, self._head[1])
            self._tail_visited_positions.add(self._tail)
        elif self._head[0]-self._tail[0] < -1:
            self._tail = (self._head[0]+1, self._head[1])
            self._tail_visited_positions.add(self._tail)

    def move_v(self,direction,length):
        for _ in range(1,length+1):
            self._move_v(direction)

    def _move_v(self,direction):
        self._head = (self._head[0], self._head[1]+direction)
        if self._head[1]-self._tail[1]>1:
            self._tail = (self._head[0],self._head[1]-1)
            self._tail_visited_positions.add(self._tail)
        elif self._head[1]-self._tail[1] < -1:
            self._tail = (self._head[0], self._head[1]+1)
            self._tail_visited_positions.add(self._tail)
    
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
    commands = file.read()
    rope = Rope()
    rope.exec_moves(commands)
    print(len(rope.tail_visited_positions()))
