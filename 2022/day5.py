class Ship:
    def __init__(self, stack_count) -> None:
        self.stacks = []
        self._init_stacks(stack_count)

    def _init_stacks(self, stack_count):
        for i in range(stack_count):
            self.stacks.append([])

    def load_desc(self,desc):
        self.stacks = []
        for line in reversed(desc.splitlines()):
            if line.strip() == "":
                continue
            if self.stacks == []:
                stack_count = int(line.split()[-1])
                self._init_stacks(stack_count)
                continue
            line = line.replace("    ", " [§] ")
            crates = line.split()
            stack = 1
            for crate in crates:
                item = crate[1]
                if item != "§":
                    self.put_crate(stack,item)
                stack += 1



    def put_crate(self, stack, crate):
        self.stack(stack).append(crate)

    def stack(self,stack):
        return self.stacks[stack-1]

    def move_9000(self,crate_count,source_stack,dest_stack):
        for _ in range(crate_count):
            item = self.stack(source_stack).pop()
            self.stack(dest_stack).append(item)
    
    def move_9001(self,crate_count,source_stack,dest_stack):
        source_stack_list = self.stack(source_stack)
        items =  source_stack_list[-crate_count:]
        self.stacks[source_stack-1]= source_stack_list[:-crate_count]
        self.stack(dest_stack).extend(items)

    def move_order(self,order, crane_type = "9000"):
        order =order.replace("move","")
        order =order.replace("from","")
        order =order.replace("to","")
        numbers = list(map(int,order.split()))
        if len(numbers) != 3:
            return
        if crane_type == "9000":
            self.move_9000(numbers[0],numbers[1],numbers[2])
        else:
            self.move_9001(numbers[0],numbers[1],numbers[2])


    def top(self):
        top_string = ""
        for stack in self.stacks:
            if stack == []:
                continue
            top_string += stack[-1]
        return top_string

with open('day5.txt') as file:
    ship_desc=""
    ship = Ship(0)
    for line in file:
        if ship.stacks == []:
            ship_desc += line
            if line.strip() == "":
                ship.load_desc(ship_desc)
            continue
        ship.move_order(line,"9001")


    print(ship.top())