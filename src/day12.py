import functools
class Record:
    def __init__(self, definition: str, fold_factor=1) -> None:
        self.damaged_record = ""
        self.count_record = None
        (self.damaged_record,self.count_record) = ('?'.join([definition.split()[0]]*fold_factor), tuple(map(int, definition.split()[1].split(',')))*fold_factor)

    def count_arrangements(self):
        return self._count_arrangements(0, 0) 

    def _advance(self,i, j):
        if j >= len(self.count_record): return 0
        if len(self.damaged_record) - i < self.count_record[j]: return 0
        if '.' in self.damaged_record[i:i+self.count_record[j]]: return 0
        if len(self.damaged_record) - i == self.count_record[j]: return self._count_arrangements(len(self.damaged_record), j+1)
        return self._count_arrangements(i+self.count_record[j]+1, j+1) if self.damaged_record[i+self.count_record[j]] in '.?' else 0    
    
    @functools.cache
    def _count_arrangements(self, i, j):
        if i >= len(self.damaged_record): return j >= len(self.count_record)
        if self.damaged_record[i] == '.': return self._count_arrangements(i+1, j)
        if self.damaged_record[i] == '#': return self._advance(i, j)
        return self._count_arrangements(i+1, j) + self._advance(i, j)

class RecordSet:
    def __init__(self, definition: str, fold_factor=1) -> None:
        self.record_list = []
        for line in definition.splitlines():
            record = Record(line,fold_factor)
            self.record_list.append(record)
    
    def sum_arrangements(self):
        sum = 0
        for record in self.record_list:
            sum += record.count_arrangements()
        return sum

if __name__ == "__main__":
    f = open("D:\\Sources\\sample_projects\\aoc2023\\tests\\day12.txt", "r")
    txt = f.read()
    record_set = RecordSet(txt)
    print(record_set.sum_arrangements())
    record_set = RecordSet(txt,5)
    print(record_set.sum_arrangements())

