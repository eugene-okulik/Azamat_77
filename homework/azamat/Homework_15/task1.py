import mysql.connector as mysql

db = mysql.connect(
    host="db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com",
    port=25060,
    user="st-onl",
    passwd="AVNS_tegPDkI5BlB2lW5eASC",
    database="st-onl"
)

cursor = db.cursor()

cursor.execute("INSERT INTO students (name, second_name) VALUES('AZ', 'TA')")
student_id = cursor.lastrowid

cursor.execute("insert into `groups` (title, start_date, end_date) values ('AQA_test', '24 sep', '24 jan')")
group_id = cursor.lastrowid

update_students = "update students set group_id = (%s) where id = (%s)"
cursor.execute(update_students, (group_id, student_id))

query = "insert into books (title, taken_by_student_id) values (%s, %s)"
values = [
    ('Qa SQL', student_id),
    ('Qa Python', student_id),
]
cursor.executemany(query, values)

def subjects(name):
    insert_query = "insert into subjects (title) values (%s)"
    cursor.execute(insert_query, (name,))
    return cursor.lastrowid

subject_id_1 = subjects('course AQA by EO')
subject_id_2 = subjects('course Azamat')

def lesson(lesson_name, subject_id):
    insert_query = "INSERT INTO lessons (title, subject_id) VALUES (%s, %s)"
    cursor.execute(insert_query, (lesson_name, subject_id))
    return cursor.lastrowid

lesson_ID_1 = lesson('Qa SQL', subject_id_1)

lesson_ID_2 = lesson('Python',subject_id_1)

lesson_ID_3 = lesson('Api', subject_id_2)

lesson_ID_4 = lesson('Pytest', subject_id_2)


query = "insert into marks (value, lesson_id, student_id) values (%s, %s, %s)"
values = [
    ('5', lesson_ID_1, student_id),
    ('5', lesson_ID_2, student_id),
    ('5', lesson_ID_3, student_id),
    ('5', lesson_ID_4, student_id),
]
cursor.executemany(query, values)

select_1 = '''
SELECT * FROM marks m
WHERE m.student_id = (%s)
'''
cursor.execute(select_1, (student_id,))
print(cursor.fetchall())

select_2 = '''
SELECT * FROM books b
WHERE b.taken_by_student_id  = (%s)
'''
cursor.execute(select_2, (student_id,))
print(cursor.fetchall())

select_3 = '''
SELECT g.title, b.title, m.value, l.title, s.title FROM students st
JOIN `groups` g ON g.id = st.group_id
JOIN marks m ON m.student_id = st.id
JOIN books b ON b.taken_by_student_id = st.id
JOIN lessons l ON l.id = m.lesson_id
JOIN subjects s ON s.id = l.subject_id
WHERE st.id = (%s)
'''

cursor.execute(select_3, (student_id,))
print(cursor.fetchall())

db.commit()
db.close()
