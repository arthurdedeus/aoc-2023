def filter_digits(value):
    return "".join(filter(str.isdigit, value))


def sum_firt_and_last_digit(value):
    return int(f"{value[0]}{value[-1]}")


def process_value(value):
    value = filter_digits(value)
    value = sum_firt_and_last_digit(value)
    return value


values = list(open("input.txt"))
sums = sum([process_value(value.lower()) for value in values])

print(sums)
# 54708
