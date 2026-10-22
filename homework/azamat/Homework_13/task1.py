import os
import datetime
from calendar import day_abbr

homework_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
data_path = os.path.join(homework_path, "eugene_okulik", "hw_13", 'data.txt')

with open(data_path) as file:  # Открыввем файл и создаем переменную сразу
    file = file.readlines()  # Содержимое фала переводим с список
    date = []
    for line in file:  # Создаем цикл
        # Делим список на 2 части точной деления служит - и срезаем сразу нумерации в начале текста
        date_text = line[3:].split(' - ')[0]
        # Т.к. переменная до сих пор числиться как строка, мы его конвертируем в формат дата для ПИТОНА
        date_time = datetime.datetime.strptime(date_text, '%Y-%m-%d %H:%M:%S.%f')
        date.append(date_time)
    x = date[0] - datetime.timedelta(days=7)
    print(x)
    y = date[1].isoweekday()
    print(y)  # 6 это суббота
    z = (datetime.datetime.now() - date[2]).days
    print(z)
