ball = int(input("Введите количество баллов: "))
if ball < 50:
    print("Неудовлетворительно")
elif ball <= 69:
    print("Удовлетворительно")
elif ball <= 89:
    print("Хорошо")
else:
    print("Отлично")