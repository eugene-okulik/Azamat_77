import random


salary = int(input("Enter your salary: "))
bonus = bool(random.getrandbits(1))

if bonus:
    bonus = True
    print(salary, ',', bonus, '-', '$', salary + random.randint(1, 100))

else:
    print(salary, ',', bonus, '-', '$', salary)
