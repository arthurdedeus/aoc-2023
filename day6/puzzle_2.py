import math

races = [
    (45, 295),
    (98, 1734),
    (83, 1278),
    (73, 1210),
]


def calculation(time, distance):
    r1 = math.ceil((time + math.sqrt(time**2 - 4 * distance)) / 2)
    r2 = math.ceil((time - math.sqrt(time**2 - 4 * distance)) / 2)
    print(r1)
    print(r2)
    return max(r1, r2) - min(r1, r2)


print(calculation(45988373, 295173412781210))
