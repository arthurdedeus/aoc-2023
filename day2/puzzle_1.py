LIMITS = {
    "red": 12,
    "green": 13,
    "blue": 14,
}


def extract_subsets(line):
    games = line.split(":")[1]
    games = [game.strip() for game in games.split(";")]
    subsets = [game.split(",") for game in games]
    return subsets


def get_game_id(line):
    name = line.split(":")[0]
    return int(name.split(" ")[-1])


def is_valid(subsets):
    for subset in subsets:
        for result in subset:
            result = result.strip()
            count, color = result.split(" ")
            count = int(count)
            if count > LIMITS.get(color):
                return False
    return True


lines = list(open("input.txt"))
possible_ids = []

for line in lines:
    game_id = get_game_id(line)
    subsets = extract_subsets(line)
    if is_valid(subsets):
        possible_ids.append(game_id)

print(sum(possible_ids))
# 2486
