def convert_written_numbers_to_int(value):
    value = value.replace("one", "o1e")
    value = value.replace("two", "t2o")
    value = value.replace("three", "t3ee")
    value = value.replace("four", "f4ur")
    value = value.replace("five", "fi5ve")
    value = value.replace("six", "s6x")
    value = value.replace("seven", "sev7en")
    value = value.replace("eight", "ei8ght")
    value = value.replace("nine", "ni9e")
    return value


def filter_digits(value):
    return "".join(filter(str.isdigit, value))


def join_first_and_last_digit(value):
    return int(f"{value[0]}{value[-1]}")


def process_value(value):
    value = convert_written_numbers_to_int(value)
    value = filter_digits(value)
    value = join_first_and_last_digit(value)
    return value


values = list(open("input.txt"))
sums = sum([process_value(value.lower()) for value in values])
print(sums)
# 54087
