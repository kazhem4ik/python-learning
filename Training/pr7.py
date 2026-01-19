''' Задание 7
Есть список строк:
words = ["cat", "", "dog", "", "elephant", ""]
Нужно:
удалить пустые строки
сохранить порядок
результат положить в новый список
❗ Без list comprehension. '''

words = ["cat", "", "dog", "", "elephant", ""]
new_words = []
for i in words:
    if i:
        new_words.append(i)
print(new_words)