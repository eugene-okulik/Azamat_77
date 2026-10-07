def add_text(func):
    def wrapper(*args, count=1, **kwargs):
        result = None
        for i in range(count):
            result = func(*args, **kwargs)
        return result
    return wrapper


@add_text
def desc(x):
    print(x)

desc('hello', count = 2)
