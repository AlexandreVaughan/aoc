
def split_rucksack(rucksack):
    mid_idx = int(len(rucksack)/2)
    return rucksack[:mid_idx],rucksack[mid_idx:]

def rucksack_common_elem(rucksack):
    comp1, comp2 = split_rucksack(rucksack)
    for item in comp1:
        if item in comp2:
            return item
    return ""

def rucksack_score_common_elem(rucksack):
    common_item :str  = rucksack_common_elem(rucksack)
    return compute_item_score(common_item)

def compute_item_score(item):
    if item.isupper():
        return ord(item[0])-ord('A')+27
    else:
        return ord(item[0])-ord('a')+1

def find_badge(group):
    badge_item_counter = {}
    for sack in group:
        sack_item_counter = {}
        for item in sack:
            sack_item_counter[item] = 1
        for item in sack_item_counter:
            if item in badge_item_counter: 
                badge_item_counter[item] +=1
            else:
                badge_item_counter[item] = 1
    
    for item,count in badge_item_counter.items():
        if count == len(group):
            return item
    return ""



with open('day3.txt') as file:
    current_elf = 0
    total_score = 0
    badge_score = 0
    current_group = []
    for line in file:
        rucksack = line.strip()
        total_score += rucksack_score_common_elem(rucksack)
        current_group.append(rucksack)
        if len(current_group) == 3:
            badge = find_badge(current_group)
            badge_score += compute_item_score(badge)
            current_group = []

    print(total_score)
    print(badge_score)