def split_on_digits(some_number: int) -> tuple:
    return [int(d) for d in str(some_number)]


print(split_on_digits(1234112))
