
def included_pairs(pair1,pair2):
    # 1---2----2---1
    if pair1[0] >= pair2[0] and pair1[1] <= pair2[1]:
        return True 
    # 2---1---1---2 
    if pair2[0] >= pair1[0] and pair2[1] <= pair1[1]:
        return True 
    return False

def in_pair(value,pair):
    return value >= pair[0] and value <= pair[1]

def overlapped_pairs(pair1,pair2):
    return (in_pair(pair1[0], pair2) or in_pair(pair1[1],pair2)
        or in_pair(pair2[0], pair1) or in_pair(pair2[1], pair1)
    )

with open('day4.txt') as file:
    total_included_pairs = 0
    total_overlapped_pairs = 0
    for line in file:
        pair_line = line.strip().split(",")
        if len(pair_line) != 2:
            continue
        pair1 = tuple(map(int,pair_line[0].split('-')))
        pair2 = tuple(map(int,pair_line[1].split('-')))
        if (included_pairs(pair1,pair2)):
            total_included_pairs+=1
        if (overlapped_pairs(pair1,pair2)):
            total_overlapped_pairs+=1

    print(total_included_pairs)
    print(total_overlapped_pairs)