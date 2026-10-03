a = 6
while True:
    user_input = float(input('Сегодня какое число?'))
    if user_input == a:
        print('Поздравляю! Вы угадали!')
        break
    else:
        print('Попробуйте снова')
