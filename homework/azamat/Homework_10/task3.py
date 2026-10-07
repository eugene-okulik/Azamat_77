def func_calc(func):
    def wrapper(a, b):
        if a < 0 or b < 0:
            operation = '*'
        elif a == b:
            operation = '+'
        elif a > b:
            operation = '-'
        else:
            operation = '/'
        return func(a, b, operation)
    return wrapper

@func_calc
def calc(a, b, operation):
    if operation == '+':
        return a + b
    elif operation == '-':
        return a - b
    elif operation == '*':
        return a * b
    else:
        return a / b


x = (int(input('Первое число: ')))
y = (int(input('Второе число: ')))

print(calc(x, y))
