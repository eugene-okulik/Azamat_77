my_dict = {
    "tuple": (1, 2, 3, 'test', False, 'xiaomi'),
    "list": [1, 'test', 3, 4, False, 'apple', 'flow'],
    "dict": {"name": 'Azamat', "family": 'Tatlok', "city": 'KR', "age": 27, "learning": 'Python', "operating system": 'mac'},
    "set": {1, 2, 3, None, False, 'samsung'}
}

print(my_dict["tuple"][-1])  # Вывести на экран последний эллемент
my_dict["list"].append(5)  # Добавлнеие в список число 5
my_dict["list"].pop(1)  # Удаление эллемент 2 в списке
my_dict["i am a tuple"] = 2  # Добавление нового эллемента ключа со значением
my_dict["dict"].pop('operating system')  # Удаление эллемента с ключа словаря
my_dict["set"].add(77)  # Добавление нового элемента множества
my_dict["set"].remove(None)  # Удаление нового элемента множества

print(my_dict)
