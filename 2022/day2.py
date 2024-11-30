
ROCK = "A"
PAPER = "B"
SCISSORS = "C"

LOSE = "X"
DRAW = "Y"
WIN = "Z"



lose_rules = {
    ROCK     : SCISSORS,
    PAPER    : ROCK,
    SCISSORS : PAPER
}

win_rules = {
    SCISSORS : ROCK,
    ROCK     : PAPER,
    PAPER    : SCISSORS,
}

item_points = {
    ROCK : 1,
    PAPER : 2,
    SCISSORS : 3
}



with open('day2.txt') as file:
    current_elf = 0
    total_score = 0
    for line in file:
        stripped_line = line.strip()
        play_turn = stripped_line.split(" ")
        p1_play = play_turn[0]
        p2_play = ""
        score = 0
        if play_turn[1] == LOSE:
            p2_play = lose_rules[p1_play]
        elif play_turn[1] == DRAW:
            p2_play = p1_play
            score += 3
        elif play_turn[1] == WIN:
            p2_play = win_rules[p1_play]
            score += 6
        score += item_points[p2_play]
        total_score += score
    print(total_score)

        

