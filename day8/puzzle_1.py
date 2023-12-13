lines = list(open("input.txt"))
directions = lines[0].strip().replace("L", "0").replace("R", "1")
maps = {
    line.strip()
    .split(" = ")[0]: line.strip()
    .split(" = ")[1]
    .replace("(", "")
    .replace(")", "")
    .split(", ")
    for line in lines[2:]
}

key = "AAA"
steps = 0
while key != "ZZZ":
    for direction in directions:
        key = maps[key][int(direction)]
        steps += 1
        print(key)
print(steps)
# 19631
