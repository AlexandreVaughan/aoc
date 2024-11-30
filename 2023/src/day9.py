class Sequence:
    def __init__(self, definition: str) -> None:
        self.initial_sequence = list(map(int,definition.split(" ")))

    def delta_sequence(self):
        return _delta_sequence(self.initial_sequence)

    def all_delta_sequences(self):
        sequences = []
        current_sequence = self.initial_sequence
        while True:
            current_sequence = _delta_sequence(current_sequence)
            if _all_zero(current_sequence):
                return sequences
            sequences.append(current_sequence)

    def next_value(self):
        delta_sequences = self.all_delta_sequences()
        sum = 0
        for delta_seq in delta_sequences:
            sum+=delta_seq[-1]
        return self.initial_sequence[-1]+sum
    
    def prev_value(self):
        delta_sequences = self.all_delta_sequences()
        diff = 0
        for delta_seq in reversed(delta_sequences):
            diff=delta_seq[0]-diff
        return self.initial_sequence[0]-diff

    
def _delta_sequence(sequence):
    return_seq = []
    previous_val = None
    for val in sequence:
        if previous_val is None:
            previous_val = val
            continue
        delta = val-previous_val
        return_seq.append(delta)
        previous_val = val
    return return_seq

def _all_zero(sequence):
    for v in sequence:
        if v != 0:
            return False
    return True

if __name__ == "__main__":
    f = open("D:\\Sources\\sample_projects\\aoc2023\\tests\\day9.txt", "r")
    txt = f.read()
    sum_next = 0
    sum_prev = 0
    for seq_def in txt.splitlines():
        seq = Sequence(seq_def)
        sum_next+= seq.next_value()
        sum_prev+= seq.prev_value()
    print(sum_next)
    print(sum_prev)