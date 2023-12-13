maze = [row.strip() for row in list(open("input.txt"))]
height = len(maze)
width = len(maze[0])

directions = {
    ".": [],
    "S": [(-1, 0), (0, -1), (0, 1), (1, 0)],
    "|": [(-1, 0), (1, 0)],
    "-": [(0, -1), (0, 1)],
    "L": [(-1, 0), (0, 1)],
    "J": [(-1, 0), (0, -1)],
    "7": [(1, 0), (0, -1)],
    "F": [(1, 0), (0, 1)],
}


def find_start(maze):
    for row in range(height):
        for column in range(width):
            if maze[row][column] == "S":
                return (row, column)


def adjacent(row, column):
    for row_step, column_step in directions[maze[row][column]]:
        next_row = row + row_step
        next_column = column + column_step

        if next_row < 0 or next_row >= height:
            continue
        if next_column < 0 or next_column >= width:
            continue
        if maze[next_row][next_column] == ".":
            continue
        yield (next_row, next_column)


def move(current, previous):
    for next in adjacent(current[0], current[1]):
        if next == previous:
            continue
        return next


def count_crossings(maze, row):
    for column in reversed(range(width)):
        crossings = 0
        if (row, column) in maze_walls:
            print(f"Skipping {row}, {column}")
            print("-------")
            continue
        print(f"Checking {row}, {column}")
        for point in range(column):
            print(row, point, maze[row][point])
            if (row, point) in maze_walls and maze[row][point] in ["F", "7", "|", "S"]:
                crossings += 1
                print(f"Crossing at {row}, {point}")
        print(f"Found {crossings} crossings")
        print("-------")
        crossing_list.append(crossings)


start = curr = prev = find_start(maze)
maze_walls = [start]
while curr == prev or curr != start:
    next = move(curr, prev)
    print(curr, prev, next)
    maze_walls.append(next)
    prev = curr
    curr = next

crossing_list = []
for row, line in enumerate(maze):
    count_crossings(maze, row)

print(len([crossing for crossing in crossing_list if crossing % 2 != 0]))
# 411 
