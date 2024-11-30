class Engine:
    def __init__(self) -> None:
        self.symbol_map = {}
        self.serial_map = {}
        self.col_count = 1000000
        self.line_count = 1000000
    
    def add_serial(self,coords,value):
        self.serial_map[coords] = value

    def add_symbol(self,coords,value):
        self.symbol_map[coords] = value

    def symbol(self,column,line):
        if not (column,line) in self.symbol_map:
            return ""
        return self.symbol_map[(column,line)]
    
    def serial(self,column,line):
        if not (column,line) in self.serial_map:
            return ""
        return self.serial_map[(column,line)]
    
    def is_valid_serial(self,column,line):
        (_,_,symbol) = self._serial_adjacent_symbol(column,line)
        return symbol != ''

    
    def _serial_adjacent_symbol(self,column,line):
        serial = self.serial(column,line)
        if  serial == '':
            return (0,0,"")
        for col_idx in range(column,column+len(serial)):
            adjacent_list = [
                (col_idx-1,line-1),
                (col_idx  ,line-1),
                (col_idx+1,line-1),
                (col_idx-1,line  ),
                (col_idx+1,line  ),
                (col_idx-1,line+1),
                (col_idx  ,line+1),
                (col_idx+1,line+1),
            ]
            for (col_adj,line_adj) in adjacent_list:
                if (col_adj < 0 or line_adj < 0):
                    continue
                if (col_adj >= self.line_count or line_adj >= self.line_count):
                    continue
                symbol = self.symbol(col_adj,line_adj)
                if symbol != "":
                    return (col_adj,line_adj,symbol)
        return (0,0,"")   
    
    def serial_sum(self):
        sum=0
        for (column,line),serial in self.serial_map.items():
            if not self.is_valid_serial(column,line):
                continue
            sum+=int(serial)
        return sum
    
    def sum_gear_ratios(self):
        sum = 0
        for (column,line) in self.symbol_map.keys():
            (serial1,serial2) = self.gear(column,line)
            sum += serial1*serial2
        return sum

    def gear(self,column,line):
        symbol = self.symbol(column,line)
        if symbol != '*':
            return(0,0)
        serial_1 = 0
        serial_2 = 0
        for (col_serial,line_serial),serial in self.serial_map.items():
            (col_adj,line_adj,_) = self._serial_adjacent_symbol(col_serial,line_serial)
            if (col_adj == column and line_adj == line):
                if serial_1 == 0:
                    serial_1 = serial
                else:
                    serial_2 = serial
                    break
        return (int(serial_1),int(serial_2))

        
    
    def load_schematic(self,schematic: str):
        line_idx = 0
        for line in schematic.splitlines():
            if line == "":
                continue
            column_idx = 0
            current_number = ""
            current_number_idx = 0
            for char in line:
                if char == '.':
                    if current_number != "":
                        self.add_serial((current_number_idx,line_idx),current_number)
                        current_number_idx = 0
                        current_number = ""
                elif char.isdigit():
                    if current_number == "":
                        current_number_idx = column_idx
                        current_number = char
                    else:
                        current_number += char
                else:
                    if current_number != "":
                        self.add_serial((current_number_idx,line_idx),current_number)
                        current_number_idx = 0
                        current_number = ""
                    self.add_symbol((column_idx,line_idx),char)
                column_idx+=1
            if current_number != "":
                self.add_serial((current_number_idx,line_idx),current_number)
            self.col_count = column_idx+1
            line_idx +=1
        self.line_count = line_idx+1
    
if __name__ == "__main__":
    f = open("D:\\Sources\\sample_projects\\aoc2023\\tests\\day3.txt", "r")
    txt = f.read()
    engine = Engine()
    engine.load_schematic(txt)
    print(engine.serial_sum())
    print(engine.sum_gear_ratios())