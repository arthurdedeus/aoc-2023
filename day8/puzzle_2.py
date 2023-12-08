import math


lines = list(open("input.txt"))
directions = lines[0].strip().replace("L", "0").replace("R", "1")
maps = {line.strip().split(" = ")[0]:line.strip().split(" = ")[1].replace('(','').replace(')','').split(", ") for line in lines[2:]}

steps = 0
step_list = []
start_map = {key:key for key in maps.keys() if key[-1] == "A"}
print(start_map)

for start, key in start_map.items():
    while not key[-1] == "Z":
        for direction in directions:
            key = maps[key][int(direction)]
            steps += 1
    step_list.append(steps)
    steps = 0

print(step_list)
print(math.lcm(*step_list))
            

# while not all([value[-1] == "Z" for value in start_map.values()]): 
#     for direction in directions:
#         print(f"step {steps}")
#         for start, key in start_map.items():
#             print(f"start: {start}, key: {key}")
#             start_map[start] = maps[key][int(direction)]
#         steps += 1
#     if all([value[-1] == "Z" for value in start_map.values()]):
#         print("Hooray!")
# print(steps)

