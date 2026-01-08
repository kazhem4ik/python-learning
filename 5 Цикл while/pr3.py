summ = 0
while True:
    number = int(input("Введите число: "))
    if number < 0:
        continue
    elif number == 0:
        break
    else:
        summ += number

print (summ)