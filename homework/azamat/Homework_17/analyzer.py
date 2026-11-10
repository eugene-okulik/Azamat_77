import os
import argparse
import re


parser = argparse.ArgumentParser()
parser.add_argument("path", help="Укажите путь к папке, где лежат логи. Пример C:\\user\\data\\logs")
parser.add_argument('--text', required=True, help = "Указать в кавычках текст ошибки или название типа лога. "
                                                    "Пример 'WARN','ERROR'")
args = parser.parse_args()  # Записываем данные в переменную

# Проверка, что мы указали файл или путь
if os.path.isdir(args.path):  # Если у нас папка
    for f in os.listdir(args.path):  # Перебираются файлы внутри папки
        with open(os.path.join(args.path, f), 'r') as file: # Через .join соединяем полный путь и файл
            for num, text in enumerate(file, start=1):
                # Сравниваем что текст, который передали соответствует тексту файла
                if args.text.lower() in text.lower():
                    x = (f'Файл {f}.\n'
                         f'Строка {num}. {text.strip()}')
                    print(x)
elif os.path.isfile(args.path): # Если это файл
    with open((args.path), 'r') as file:
        # Читаем построчно и добавляем нумерации строк начиная с 1
        for num, text in enumerate(file, start=1):
            # Сравниваем что текст, который передали соответствует тексту файла
            if args.text.lower() in text.lower():
                x = (f'Файла {os.path.basename(args.path)}\n'
                     f'Строка {num}. {text.strip()}')
                print(x)
else:
    print('Путь не найден')
blocks = {}
timestamp = None
current_block = []
for num, text in enumerate(file, start=1):
    x = re.match(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}', text)
    if x is not None:
        if timestamp is not None:
            blocks[timestamp] = current_block
            current_block = []
        timestamp = x.group()
    current_block.append(text)
