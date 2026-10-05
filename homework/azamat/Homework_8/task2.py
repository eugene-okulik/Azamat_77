import sys

sys.set_int_max_str_digits(30000)


def fibonacci():
    a = 0
    b = 1

    while True:
        yield a
        a, b = b, a + b


generator = fibonacci()

for i in range(100000):
    number = next(generator)

    if i + 1 in (5, 200, 1000, 100000):
        print(number)
