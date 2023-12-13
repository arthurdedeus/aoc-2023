def get_seeds(lines):
    seeds = lines[0].strip().split(":")[1].strip().split(" ")
    return [int(seed) for seed in seeds]


def clean_value(value):
    return int(value.strip())


def map_value(title, seed, lines):
    start = lines.index(f"{title}\n") + 1
    end = lines[start:].index("\n") + start

    for idx in range(start, end):
        dst, src, length = lines[idx].split(" ")
        src = clean_value(src)
        dst = clean_value(dst)
        length = clean_value(length)

        if seed in range(src, src + length):
            diff = seed - src
            return dst + diff

    return seed


with open("test_input.txt") as file:
    lines = file.readlines()
    seeds = get_seeds(lines)
    locations = []

    for seed in seeds:
        soil = map_value("seed-to-soil map:", seed, lines)
        fertilizer = map_value("soil-to-fertilizer map:", soil, lines)
        water = map_value("fertilizer-to-water map:", fertilizer, lines)
        light = map_value("water-to-light map:", water, lines)
        temperature = map_value("light-to-temperature map:", light, lines)
        humidity = map_value("temperature-to-humidity map:", temperature, lines)
        location = map_value("humidity-to-location map:", humidity, lines)
        locations.append(location)

    print(min(locations))
    # 226172555
