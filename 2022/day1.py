
calories_array = []

with open('day1.txt') as file:
    current_elf = 0
    for line in file:
        stripped_line = line.strip()
        if stripped_line == "":
            calories_array.append(current_elf)
            current_elf = 0
            continue
        current_elf += int(stripped_line)
    if current_elf != 0:
        calories_array.append(current_elf)

calories_array = sorted(calories_array)
print(calories_array[0])
print(calories_array[-1])

sum = 0
for i in range(1,4):
    print(calories_array[-i])
    sum+= calories_array[-i]
print(sum)
        

