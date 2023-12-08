class DesertMap:
    def __init__(self, definition: str) -> None:
        self.node_map = {}
        for line in definition.splitlines():
            (node_name,_,node_def) = line.partition(" = ")
            (left, _, right) = node_def.replace("(","").replace(")","").partition(", ")
            self.node_map[node_name] = (left,right)

    def left(self, node:str):
        return self.node_map[node][0]
    
    def right(self, node:str):
        return self.node_map[node][1]
    
    def follow_instructions(self,instructions):
        node = "AAA"
        return self._follow_instructions(instructions, node)

    def _follow_instructions(self, instructions, node):
        function_map = {
            'L' : DesertMap.left,
            'R' : DesertMap.right
        }
        for instruction in instructions:
            node = function_map[instruction](self,node)
        return node

    def find_destination(self,instructions):
        steps_count = 0
        node = 'AAA'
        while True:
            for instruction in instructions:
                node = self._follow_instructions(instruction,node)
                steps_count+=1
                if node == 'ZZZ':
                    return steps_count
                
    def find_ghost_destination(self,instructions):
        steps_count = 0
        nodes = self.ghost_starting_points()
        while True:
            for instruction in instructions:
                found_all_destinations = True
                steps_count+=1
                new_nodes = set()
                for node in nodes:
                    node = self._follow_instructions(instruction,node)
                    new_nodes.add(node)
                    if not is_ghost_ending_point(node):
                        found_all_destinations = False
                nodes = new_nodes
            if found_all_destinations:
                return steps_count
                    
    
    def ghost_starting_points(self):
        start_points = set()
        for node in self.node_map.keys():
            if node.endswith('A'):
                start_points.add(node)
        return start_points
                

def is_ghost_ending_point(node: str):
    return node.endswith('Z')

if __name__ == "__main__":
    f = open("D:\\Sources\\sample_projects\\aoc2023\\tests\\day8.txt", "r")
    txt = f.read()
    instructions = txt.splitlines()[0]
    definition = txt.replace(instructions,"").strip()
    desert_map = DesertMap(definition)
    print(desert_map.find_destination(instructions))
    print(desert_map.find_ghost_destination(instructions))