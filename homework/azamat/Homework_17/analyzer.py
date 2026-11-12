import os
import argparse
import re


parser = argparse.ArgumentParser()
parser.add_argument("path", help="Укажите путь к папке, где лежат логи. Пример C:\\user\\data\\logs")
parser.add_argument('--text', required=True, help="Указать в кавычках текст ошибки.")

args = parser.parse_args()  # Записываем данные в переменную


if os.path.isdir(args.path):  # Если у нас папка
    files = [os.path.join(args.path, f)  # Объединение в один путь
            for f in os.listdir(args.path)  # Перебираются файлы внутри папки
            if os.path.isfile(os.path.join(args.path, f))
        ]
    print('Это папка')

elif os.path.isfile(args.path):  # Если это файл
    files = [args.path]
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
                if timestamp is not None:  # Ищем timestamp в начале строки.
                    # Если встретили новую дату и предыдущий блок существует — сохраняем предыдущий блок.
                    blocks[timestamp] = current_block
                    # Создаём новый список.
                    current_block = []
                # сохраняем найденное время в переменную
                timestamp = x.group()
            if timestamp is not None:
                # Добавляем текущую строку вместе с её номером.
                current_block.append((num, text))
        if timestamp is not None:  # После завершения файла сохраняем последний блок.
            blocks[timestamp] = current_block
        for timestamp, lines in blocks.items():  # Перебираем содержимое в блоках
            args_text = args.text.lower().split()
            for num, text in lines:  # Берем нужное содержимое и перебираем снова
                # Разделенеи на отдельные слова для удобного поиска
                text_log = text.lower().split()
                for i in range(len(text_log)):  # Перебираем всче слова в тексте лога
                    # Проверяем, совпадает ли последовательность слов из лога с поисковым запросом
                    if text_log[i:i + len(args_text)] == args_text:
                        index = i
                        start = max(0, i - 5)
                        end = min(len(text_log), i + len(args_text) + 5)
                        before = text_log[start:i]
                        after = text_log[i + len(args_text):end]
                        context = ' '.join(before + args_text + after)

                        print(f"Имя файла: {os.path.basename(file_path)},\n"
                              f"Время: {timestamp},\n"
                              f"Строка: {num},\n"
                              f"Текст: {context}")
