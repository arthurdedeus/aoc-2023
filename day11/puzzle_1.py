universe = [line.strip() for line in list(open("input.txt"))]


def get_empty_rows_and_columns(universe):
    empty_lines = set()
    empty_columns = set()

    for row, line in enumerate(universe):
        if all([char == "." for char in line]):
            empty_lines.add(row)
        for idx, column in enumerate(universe[0]):
            if all(universe[row][idx] == "." for row in range(len(universe))):
                empty_columns.add(idx)
    return empty_lines, empty_columns


def calculate_distance(src, dst):
    dist = abs(src[0] - dst[0]) + abs(src[1] - dst[1])
    for empty_row in empty_rows:
        if empty_row > src[0] and empty_row < dst[0]:
            dist += 1
        if empty_row < src[0] and empty_row > dst[0]:
            dist += 1
    for empty_column in empty_columns:
        if empty_column > src[1] and empty_column < dst[1]:
            dist += 1
        if empty_column < src[1] and empty_column > dst[1]:
            dist += 1
    return dist


empty_rows, empty_columns = get_empty_rows_and_columns(universe)
height = len(universe)
width = len(universe[0])

galaxies = []
for row in range(height):
    for column in range(width):
        if universe[row][column] == "#":
            galaxies.append((row, column))

distances = []
num_pairs = 0
seen = set()
for idx, galaxy in enumerate(galaxies):
    for other_galaxy in galaxies:
        if other_galaxy == galaxy:
            continue
        if (other_galaxy, galaxy) in seen:
            continue
        seen.add((galaxy, other_galaxy))
        num_pairs += 1
        distance = calculate_distance(galaxy, other_galaxy)
        distances.append(distance)

print(sum(distances))
# 10490062
