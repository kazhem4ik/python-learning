# Нужно сделать так, что бы количество знаков с двух сторон было одинаковое
input_str = "Jessy"
length = 10
if (len(input_str) % 2):
    length += 1
print(("{0:*^"+str(length)+"}").format(input_str))