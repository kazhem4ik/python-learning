# Функции input() и print()


# input() - функция для ввода данных
name = input("Ваше имя: ")
print(name)


# print() - функция для вывода данных
# Синтаксис функции print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)

products = ["Молоко", "Сыр", "Мясо"]

print(*products)
print(*products, sep=', ')
print(*products, sep=', ', end='!')
print(*products, sep=', ')
print(*products, sep=' + ', end=' = ')
print("100")