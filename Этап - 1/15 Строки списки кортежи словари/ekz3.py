''' 🧪 ЭКЗАМЕН A — СПИСКИ + СЛОВАРИ (ФИЛЬТРАЦИЯ)
📥 Дано
users = {
    "alex": {"age": 31, "city": "Moscow"},
    "john": {"age": 25, "city": "Berlin"},
    "maria": {"age": 28, "city": "Madrid"},
    "kate": {"age": 19, "city": "London"}
}
🎯 Задача
Создать пустой список adults
Пройтись по словарю users
Добавить в список adults имена пользователей,
у которых возраст >= 25
Вывести список adults
🚫 Ограничения
❌ без функций
❌ без filter
❌ без list comprehension
❌ без .get()
❌ без try/except
✅ можно:
for
if
append
доступ через [] '''

adults = []
users = {
    "alex": {"age": 31, "city": "Moscow"},
    "john": {"age": 25, "city": "Berlin"},
    "maria": {"age": 28, "city": "Madrid"},
    "kate": {"age": 19, "city": "London"}
}
for i in users:
    if users[i]["age"] >= 25:
        adults.append(i)
print(adults)
count = 0
for i in adults:
    count += 1
print(f'Пользователей старше 25: {count}')

new_adults = ""
for i in range(len(adults)):
    new_adults += adults[i]
    if i != len(adults) - 1:
        new_adults = new_adults + ", "
print(new_adults)
print(range(len(adults)))
