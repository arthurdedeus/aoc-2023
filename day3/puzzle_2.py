import re, math


board = list(open('input.txt'))
length = len(board)
width = len(board[0]) - 1

symbols = {
  (row, column): []
  for row in range(length)
  for column in range(width)
  if board[row][column] not in '01234566789.'
  }

for idx, line in enumerate(board):
  for number in re.finditer(r"\d+", line):
    edges = {
      (row, column)
      for row in (idx - 1, idx, idx + 1)
      for column in range(number.start() - 1, number.end() + 1)
    }

    for hit in edges & symbols.keys():
      symbols[hit].append(int(number.group()))

print(sum(math.prod(part_number) for part_number in symbols.values() if len(part_number) == 2))
# 79026871
