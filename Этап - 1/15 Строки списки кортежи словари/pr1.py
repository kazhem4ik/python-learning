''' Задание A1 — базовое разрезание
text = "apple banana orange"
Разрежь строку на слова
Выведи список
Выведи каждое слово отдельно через for
📌 Цель:
почувствовать, что split() → list '''

text = "apple banana orange"
text1= text.split()
for i in text1:
    print(i)