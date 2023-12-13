lines = [line.strip().split(" ") for line in list(open("input.txt"))]
lines = [[int(item) for item in line] for line in lines]


def get_diffs(lines, idx, diff_map):
    prev = lines[0]
    diffs = []
    for item in lines[1:]:
        diffs.append(item - prev)
        prev = item
    if any(diffs):
        diff_map[idx].append(diffs)
        get_diffs(diffs, idx, diff_map)
    else:
        return


def extrapolate(diff_map):
    extrapolated_vals = []
    for idx, diffs in diff_map.items():
        aux = diffs[-1][0]
        for diff in reversed(diffs[:-1]):
            aux = diff[0] - aux
        extrapolated_vals.append(aux)
    return extrapolated_vals


diff_map = {}
for idx, line in enumerate(lines):
    diff_map[idx] = [line]
    get_diffs(line, idx, diff_map)

extrapolated_vals = extrapolate(diff_map)
print(sum(extrapolated_vals))
# 1097
