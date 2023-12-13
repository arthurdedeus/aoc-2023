EXTRA = {}


def clean(numbers):
    return [int(item) for item in numbers.split(" ") if item]


def extract_numbers(line):
    winning_numbers, owned_numbers = line.split(":")[1].split("|")
    winning_numbers = clean(winning_numbers)
    owned_numbers = clean(owned_numbers)
    return winning_numbers, owned_numbers


def calculate_winners(line):
    winning_numbers, owned_numbers = extract_numbers(line)
    winners = []
    for number in owned_numbers:
        if number in winning_numbers:
            winners.append(number)

    return len(winners)


def get_card_id(line):
    return int(line.split(":")[0].split(" ")[-1])


def increment_count(extra_id):
    EXTRA[extra_id] = EXTRA.get(extra_id, 0) + 1


lines = list(open("input.txt"))
for line in lines:
    num_lines = len(lines)
    card_id = get_card_id(line)
    increment_count(card_id)
    winners = calculate_winners(line)

    for point in range(1, winners + 1):
        extra_id = card_id + point
        if extra_id > num_lines:
            continue

        EXTRA[extra_id] = EXTRA.get(extra_id, 0) + 1 * EXTRA.get(card_id, 1)

total_cards = sum(EXTRA.values())
print(total_cards)
# 8063216
