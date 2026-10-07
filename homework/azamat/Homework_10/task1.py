def add_text(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        print("finished")
        return
    return wrapper


@add_text
def desc(text):
    print(text)

desc('hello')
