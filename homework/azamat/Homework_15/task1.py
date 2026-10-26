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

cursor.execute(f"update students set group_id = {group_id} where id =  {student_id}")

query = f"insert into books (title, taken_by_student_id) values (%s, %s)"
values = [
    ('Qa SQL', student_id),
    ('Qa Python', student_id),
]
cursor.executemany(query, values)

cursor.execute("insert into subjects (title) values ('course AQA by EO')")
subject_id_1 = cursor.lastrowid

cursor.execute("insert into subjects (title) values ('course Azamat')")
subject_id_2 = cursor.lastrowid

cursor.execute(f"insert into lessons (title, subject_id) values ('SQL AQA', {subject_id_1})")
lesson_ID_1 = cursor.lastrowid

cursor.execute(f"insert into lessons (title, subject_id) values ('Python', {subject_id_1})")
lesson_ID_1_1 = cursor.lastrowid

cursor.execute(f"insert into lessons (title, subject_id) values ('API', {subject_id_2})")
lesson_ID_2 = cursor.lastrowid

cursor.execute(f"insert into lessons (title, subject_id) values ('Pytest', {subject_id_2})")
lesson_ID_2_2 = cursor.lastrowid

query = f"insert into marks (value, lesson_id, student_id) values (%s, %s, %s)"
values = [
    ('5', lesson_ID_1, student_id),
    ('5', lesson_ID_1_1, student_id),
    ('5', lesson_ID_2, student_id),
    ('5', lesson_ID_2_2, student_id),
]
cursor.executemany(query, values)

select_1 = f'''
SELECT * FROM marks m
WHERE m.student_id = {student_id}
'''
cursor.execute(select_1)
print(cursor.fetchall())

select_2 = f'''
SELECT * FROM books b
WHERE b.taken_by_student_id  = {student_id}
'''
cursor.execute(select_2)
print(cursor.fetchall())

select_3 = f'''
SELECT g.title, b.title, m.value, l.title, s.title FROM students st
JOIN `groups` g ON g.id = st.group_id
JOIN marks m ON m.student_id = st.id
JOIN books b ON b.taken_by_student_id = st.id
JOIN lessons l ON l.id = m.lesson_id
JOIN subjects s ON s.id = l.subject_id
WHERE st.id = {student_id}
'''
cursor.execute(select_3)
print(cursor.fetchall())

db.commit()
db.close()
