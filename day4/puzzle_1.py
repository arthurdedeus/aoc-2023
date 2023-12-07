def clean(numbers):
  return [int(item) for item in numbers.split(" ") if item]

def calculate_points(winning_numbers, owned_numbers):
  winners = []
  for number in owned_numbers:
    if number in winning_numbers:
      winners.append(number)

  if not winners:
    return 0

  return 2 ** (len(winners) - 1)

def extract_numbers(line):
  winning_numbers, owned_numbers = line.split(":")[1].split("|")
  winning_numbers = clean(winning_numbers)
  owned_numbers = clean(owned_numbers)
  return winning_numbers, owned_numbers

lines = list(open("input.txt"))
points = []

for line in lines:
  winning_numbers, owned_numbers = extract_numbers(line)
  points.append(calculate_points(winning_numbers, owned_numbers))

print(sum(points))
# 18619
