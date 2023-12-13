from concurrent.futures import ThreadPoolExecutor, as_completed


def clean_value(value):
    return int(value.strip())


def get_pairs(lines):
    seeds = [int(seed) for seed in lines[0].strip().split(":")[1].strip().split(" ")]
    return zip(seeds[::2], seeds[1::2])


def clean_value(value):
    return int(value.strip())


def map_value(title, value, lines):
    start = lines.index(f"{title}\n") + 1
    end = lines[start:].index("\n") + start

    for idx in range(start, end):
        dst, src, length = lines[idx].split(" ")
        src = clean_value(src)
        dst = clean_value(dst)
        length = clean_value(length)

        if value in range(src, src + length):
            diff = value - src
            return dst + diff

    return value


def reverse_map_value(title, value, lines):
    start = lines.index(f"{title}\n") + 1
    end = lines[start:].index("\n") + start

    for idx in range(start, end):
        dst, src, length = lines[idx].split(" ")
        src = clean_value(src)
        dst = clean_value(dst)
        length = clean_value(length)
        if value in range(dst, dst + length):
            diff = value - dst
            return src + diff

    return value


def calculate_location(seed):
    soil = map_value("seed-to-soil map:", seed, lines)
    fertilizer = map_value("soil-to-fertilizer map:", soil, lines)
    water = map_value("fertilizer-to-water map:", fertilizer, lines)
    light = map_value("water-to-light map:", water, lines)
    temperature = map_value("light-to-temperature map:", light, lines)
    humidity = map_value("temperature-to-humidity map:", temperature, lines)
    location = map_value("humidity-to-location map:", humidity, lines)
    return location


def calculate_seed(location):
    humidity = reverse_map_value("humidity-to-location map:", location, lines)
    temperature = reverse_map_value("temperature-to-humidity map:", humidity, lines)
    light = reverse_map_value("light-to-temperature map:", temperature, lines)
    water = reverse_map_value("water-to-light map:", light, lines)
    fertilizer = reverse_map_value("fertilizer-to-water map:", water, lines)
    soil = reverse_map_value("soil-to-fertilizer map:", fertilizer, lines)
    seed = reverse_map_value("seed-to-soil map:", soil, lines)
    return seed


def process_pair(pair):
    start, length = pair
    seeds = range(start, start + length)

    for location in range(9999999999999):
        seed = calculate_seed(location)
        if seed in seeds:
            return seed


with open("input.txt") as file:
    lines = file.readlines()
    smallest_seeds = []
    pairs = get_pairs(lines)

    with ThreadPoolExecutor(max_workers=10) as executor:
        future_to_pair = future_to_pair = {
            executor.submit(process_pair, pair): pair for pair in pairs
        }

        for future in as_completed(future_to_pair):
            pair = future_to_pair[future]
            try:
                result = future.result()
                with open("res.txt", "a") as f:
                    f.write(f"{result}\n")
                smallest_seeds.append(result)

            except Exception as exc:
                print(f"Pair {pair} generated an exception: {exc}")
            else:
                print(f"Pair {pair} processed with result: {result}")

    print(min(smallest_seeds))
    # 3763992295 corresponds to the seed that leads to the smallest location
    location = calculate_location(3763992295)
    print(location)
    # 47909639
