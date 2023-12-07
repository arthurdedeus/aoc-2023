def extract_results(line):
  subsets = [game.strip().split(",") for game in line.split(":")[1].split(";")]
  results = []
  for subset in subsets:
    results.extend(subset)
    results = [result.strip() for result in results]
  return results

def get_power(results):
  max_cubes = {
    "red": 0,
    "green": 0,
    "blue": 0,
  }

  for result in results:
    count, color = result.split(" ")
    count = int(count)
    if count > max_cubes.get(color):
      max_cubes[color] = count

  return max_cubes["green"] * max_cubes["red"] * max_cubes["blue"]

lines = list(open("input.txt"))
powers = []

for line in lines:
  results = extract_results(line)
  powers.append(get_power(results))

print(sum(powers))
# 87984
