labels = ["J", "2", "3", "4", "5", "6", "7", "8", "9", "T", "Q", "K", "A"]
lines = [line.strip().split(" ") for line in list(open('input.txt'))]
FIVE_OF_KIND = 6
FOUR_OF_KIND = 5
FULL_HOUSE = 4
THREE_OF_KIND = 3
TWO_PAIRS = 2
ONE_PAIR = 1
HIGH_CARD = 0
def jokers(counts):
  return counts["J"]

def get_type_no_joker(hand):
  counts = {label: 0 for label in labels}
  for card in hand:
    counts[card] += 1

  if any([count == 5 for count in counts.values()]):
    return FIVE_OF_KIND
  if any([count == 4 for count in counts.values()]):
    return FOUR_OF_KIND
  if any([count == 3 for count in counts.values()]):
    if any([count == 2 for count in counts.values()]):
      return FULL_HOUSE
    return THREE_OF_KIND

  num_pairs = sum([count == 2 for count in counts.values()])
  if num_pairs == 2:
    return TWO_PAIRS
  if num_pairs == 1:
    return ONE_PAIR
  return HIGH_CARD

def get_type(hand):
  counts = {label: 0 for label in labels}
  for card in hand:
    counts[card] += 1

  if any([count in [5, 4] for count in counts.values()]):
    return FIVE_OF_KIND

  if jokers(counts) == 3:
    if any([count == 2 for count in counts.values()]):
      return FIVE_OF_KIND
    return FOUR_OF_KIND

  if jokers(counts) == 2:
    if any([count == 3 for count in counts.values()]):
      return FIVE_OF_KIND
    if sum([count == 2 for count in counts.values()]) == 2:
      return FOUR_OF_KIND
    return THREE_OF_KIND

  if any([count == 4 for count in counts.values()]):
    return FIVE_OF_KIND
  if any([count == 3 for count in counts.values()]):
    return FOUR_OF_KIND

  num_pairs = sum([count == 2 for count in counts.values()])
  if num_pairs == 2:
    return FULL_HOUSE
  if num_pairs == 1:
    return THREE_OF_KIND
  return ONE_PAIR

def sort_bids_per_type(hands_per_type):
  sorted_bids = []
  for _, hands in hands_per_type.items():
    if not hands:
      continue
    sorted_bids.extend([hand[-1] for hand in sorted(hands, key=lambda hand: hand[0], reverse=True)])
  return sorted_bids

labels = ["J", "2", "3", "4", "5", "6", "7", "8", "9", "T", "Q", "K", "A"]
lines = [line.strip().split(" ") for line in list(open('input.txt'))]
hands_per_type = {
  6: [],
  5: [],
  4: [],
  3: [],
  2: [],
  1: [],
  0: [],
}
for hand, bid in lines:
  if "J" not in hand:
    _type = get_type_no_joker(hand)
  else:
    _type = get_type(hand)

  key = [labels.index(card) for card in hand]
  hands_per_type[_type].append([key, hand, bid])

bids = sort_bids_per_type(hands_per_type)

result = 0
for mult, bid in enumerate(reversed(bids), 1):
  result += int(bid) * mult
print(result)

# 249356515 - correct
