import csv
import os
import dotenv
import mysql.connector as mysql

dotenv.load_dotenv(override=True)

# Подключение к БД через env файл
db = mysql.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSW"),
    database=os.getenv("DB_NAME"),
    port=os.getenv("DB_PORT")
)

# Создание курсора для управления бд и делаем запрос для переменной DATA
cursor = db.cursor()
cursor.execute('''
SELECT
    st.name,
    st.second_name,
    g.title,
    b.title,
    s.title,
    l.title, 
    m.value
FROM students st
    JOIN `groups` g ON g.id = st.group_id
    JOIN marks m ON m.student_id = st.id
    JOIN books b ON b.taken_by_student_id = st.id
    JOIN lessons l ON l.id = m.lesson_id
    JOIN subjects s ON s.id = l.subject_id;
''')

# Получение в переменной результат запроса
data = cursor.fetchall()

# Тут мы делаем преобразование последнего столбца в строку, путем среза целого числа и добавления в виде строки
data2 = []
for x in data:
    data2.append(tuple(x[:-1]) + (str(x[-1]),))

# Находим корень файла
homework_csv = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
data_csv = os.path.join(homework_csv, "eugene_okulik", "Lesson_16", "hw_data", 'data.csv')

# Читаем полученный файл
with open(data_csv, newline='') as csv_file:
    file_data = csv.DictReader(csv_file)
    # Создание переменной для добавления содержимое CSV файла
    data1 = []
    for a in file_data:
        # Добавляем ввиде кортежей именно ЗНАЧЕНИЕ для сравнения в будущем, т.к. с бд приходят не словари, а кортежи
        data1.append(tuple(a.values()))

# Проверка содержимого БД и файла CSV для сравнения, и вывод тех строк, которые не сходятся с БД
for a in data1:
    if a not in data2:
        print(a)



db.commit()
db.close()
