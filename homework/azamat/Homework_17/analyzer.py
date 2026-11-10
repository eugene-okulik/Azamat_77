import os
import argparse
import re


parser = argparse.ArgumentParser()
parser.add_argument("path", help="Укажите путь к папке, где лежат логи. Пример C:\\user\\data\\logs")
parser.add_argument('--text', required=True, help = "Указать в кавычках текст ошибки.")

args = parser.parse_args()  # Записываем данные в переменную

# # Проверка, что мы указали файл или путь
# if os.path.isdir(args.path):  # Если у нас папка
#     print('Это папка')
#     for f in os.listdir(args.path):  # Перебираются файлы внутри папки
#         with open(os.path.join(args.path, f), 'r') as file: # Через .join соединяем полный путь и файл
#             for num, text in enumerate(file, start=1):
#                 # Сравниваем что текст, который передали соответствует тексту файла
#                 if args.text.lower() in text.lower():
#                     x = (f'Файл {f}.\n'
#                          f'Строка {num}. {text.strip()}')
#                     print(x)
# elif os.path.isfile(args.path): # Если это файл
#     print('Это файл')
#     with open((args.path), 'r') as file:
#         # Читаем построчно и добавляем нумерации строк начиная с 1
#         for num, text in enumerate(file, start=1):
#             # Сравниваем что текст, который передали соответствует тексту файла
#             if args.text.lower() in text.lower():
#                 x = (f'Файла {os.path.basename(args.path)}\n'
#                      f'Строка {num}.'
#                      f'Содержание{text.strip()}')
#                 print(x)
# else:
#     print('Путь не найден')
# blocks = {}
# timestamp = None
# current_block = []
# for num, text in enumerate(file, start=1):
#     x = re.match(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}', text)
#     if x is not None:
#         if timestamp is not None:
#             blocks[timestamp] = current_block
#             current_block = []
#         timestamp = x.group()
#     current_block.append(text)

# Проверка, что мы указали файл или путь


if os.path.isdir(args.path):  # Если у нас папка
    files = [os.path.join(args.path, f)  # Объединение в один путь
            for f in os.listdir(args.path)  # Перебираются файлы внутри папки
            if os.path.isfile(os.path.join(args.path, f))
        ]
    print('Это папка')

elif os.path.isfile(args.path): # Если это файл
    file = [args.path]
    print('Это файл')

else:
    print('Путь не найден')

for file_path in files:
    with open(file_path) as file:  # Открываем файл
        blocks = {}
        timestamp = None
        current_block = []
        for num, text in enumerate(file, start=1):  # Чиатем построчно с добавлением нумерации
            x = re.match(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}', text)
            if x is not None:
                if timestamp is not None:  #Ищем timestamp в начале строки.
                    # Если встретили новую дату и предыдущий блок существует — сохраняем предыдущий блок.
                    blocks[timestamp] = current_block
                    # Создаём новый список.
                    current_block = []
                # сохраняем найденное время в переменную
                timestamp = x.group()
            if timestamp is not None:
                # Добавляем текущую строку вместе с её номером.
                current_block.append((num,text))
        if timestamp is not None: # После завершения файла сохраняем последний блок.
            blocks[timestamp] = current_block
            for timestamp, lines in blocks.items():  # Перебираем содержимое в блоках
                for num, text in lines:  # Берем нужное содержимое и перебираем снова
                    if args.text.lower() in text.lower(): # Сравниваем полученный текс с текстом в 'логах'
                        print(f"Имя: {file},\n"
                              f"Время: {timestamp},\n"
                              f"Строка: {num},\n"
                              f"Текст: {text}")
