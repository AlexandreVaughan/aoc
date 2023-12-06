class Race:
    def __init__(self, time, record_distance) -> None:
        self.race_time = time
        self.record_distance = record_distance

    def travel_distance(self,time_press):
        speed = time_press
        remaining_time = max(0,self.race_time-time_press)
        return speed*remaining_time
    
    def  count_win_possibilities(self):
        time_press = 1
        win_count = 0
        while True:
            distance = self.travel_distance(time_press)
            if distance <= 0:
                return win_count
            if distance > self.record_distance:
                win_count+=1
            time_press+=1
    
def load_races(races: str, remove_spaces=False):
    times = []
    dists = []
    for line in races.splitlines():
        if line.startswith("Time:"):
            def_time = line[5:]
            if remove_spaces:
                def_time = def_time.replace(" ", "")
            for time_str in def_time.split():
                times.append(int(time_str))
        elif line.startswith("Distance:"):
            def_dist = line[9:]
            if remove_spaces:
                def_dist = def_dist.replace(" ", "")
            for dist_str in def_dist.split():
                dists.append(int(dist_str))

    races_array = []
    for idx in range(len(times)):
        races_array.append(Race(times[idx],dists[idx]))

    return races_array

def multiply_win_possibilities(races):
    mult_result = 1
    for race in races:
        mult_result *= race.count_win_possibilities()
    return mult_result

if __name__ == "__main__":
    f = open("D:\\Sources\\sample_projects\\aoc2023\\tests\\day6.txt", "r")
    txt = f.read()
    races = load_races(txt)
    print(multiply_win_possibilities(races))
    races = load_races(txt,True)
    print(multiply_win_possibilities(races))
