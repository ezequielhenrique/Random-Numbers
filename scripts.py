def is_integer(value):
    integer = True
    try:
        value = int(value)
    except ValueError:
        integer = False
    return integer


def generate_numbers(num_numbers, from_number, to_number):
    from random import randint

    numbers = list()

    while len(numbers) < num_numbers:
        n = randint(from_number, to_number)
        if n not in numbers:
            numbers.append(n)
        else:
            pass
    numbers.sort()
    return numbers
