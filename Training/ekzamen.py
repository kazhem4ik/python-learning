''' ⚫ УРОВЕНЬ 4 — очень тяжёлый (экзамен)
Задание 8
Числа записаны в файле numbers.txt, по одному в строке.
Нужно:
Прочитать файл
Пройтись for
Пропустить пустые строки
Найти:
сумму
количество
минимальное
максимальное
📌 Нельзя использовать min, max, sum, len '''

file = open("numbers.txt", "r")
numbers = file.read()
lines = numbers.split("\n")     # - убрали перенос строки
summ = 0
count = 0
maximum = None
minimum = None
for i in lines:
    if not i: continue
    i_int = int(i)              # - сделали i int вместо str
    summ += i_int
    count += 1
    if maximum is None: maximum = i_int
    if minimum is None: minimum = i_int
    if maximum < i_int: maximum = i_int
    if minimum > i_int: minimum = i_int
    
print("Сумма: " + str(summ))
print("Количество чисел: " + str(count))
print("Минимальное число: " + str(minimum))
print("Максимальное число: " + str(maximum))