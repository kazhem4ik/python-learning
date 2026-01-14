''' Задание B2 — tuple из строки
text = "John 25 Berlin"
Разрежь строку
Преобразуй результат в tuple
Достань имя и город
📌 Цель:
tuple как “запись”, а не контейнер для изменений '''

text = "John 25 Berlin"

# 1️⃣ Разбиваем строку на список
parts = text.split()  # ['John', '25', 'Berlin']

# 2️⃣ Превращаем список в tuple
person = tuple(parts)  # ('John', '25', 'Berlin')

# 3️⃣ Достаём элементы по индексу
name = person[0]
city = person[2]

# 4️⃣ Выводим результат
print("Имя:", name)
print("Город:", city)