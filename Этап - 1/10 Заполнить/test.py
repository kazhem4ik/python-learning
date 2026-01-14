file_name = input("Введите название файла: ")
file_text = input("Введите содержимое файла: ")

test_file = open(file_name, "w")
test_file.write(file_text)
test_file.close()