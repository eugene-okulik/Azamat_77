students = ['Ivanov', 'Petrov', 'Sidorov']
subjects = ['math', 'biology', 'geography']

# students = ', '.join(students)  # Преобразование в читабельный текст(т.е. вывел список без кавычек и скобок)
# subjects = ', '.join(subjects)  # Преобразование в читабельный текст(т.е. вывел список без кавычек и скобок)

# print(students)  # Посмотреть что получилось
# print(subjects)  # Посмотреть что получилось

print(
    'Students', ', '.join(students),
    'study these subjects:', ', '.join(subjects)
)

