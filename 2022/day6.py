
STANDARD_MARKER_SIZE = 4
MESSAGE_MARKER_SIZE= 14

def find_marker_end(stream,marker_size=STANDARD_MARKER_SIZE):
    if len(stream) < marker_size:
        return 0
    for idx_start in range(len(stream)-marker_size+1):
        idx_end = idx_start+marker_size
        potential_marker = stream[idx_start:idx_end]
        marker_found = is_marker(potential_marker)
        if marker_found:
            return idx_end
    return 0

def is_marker(potential_marker):
    elem_set = set()
    for elem in potential_marker:
        if elem in elem_set:
            return False
        elem_set.add(elem)
    return True

with open('day6.txt') as file:
    stream = file.readline()
    print(find_marker_end(stream))
    print(find_marker_end(stream,MESSAGE_MARKER_SIZE))