# Задание 1:
 
# Посчитать:
# 1) Сумму ряда 0 - 88888888
# 2) Среднее арифметическое ряда [3, 4, 56, 100, 2, 2, 3]
# 3) Заменить в строке "asdxfghyxyx" все буквы "х" на "у"
# 4) Сосчитать произведение чисел [3, 4, 56, 100, 15, 2, 20, 30], 
#    кратных и 3 и 5.
# 5) Заменить все буквы "х" на "у" в исходной строке 
#    без использования дополнительной строки.


# 1) Посчитать сумму ряда 0 - 88888888
# 88888888 не включено в расчет
result = sum(range(88888888))
print(result)
# 3950617160493828

# Если нужен расчет по 88888888 включительно, то:
result = sum(range(88888889))
print(result)
# 3950617249382716


# 2) Среднее арифметическое ряда [3, 4, 56, 100, 2, 2, 3]
values = [3, 4, 56, 100, 2, 2, 3]
result = sum(values)/len(values)
print(result)
# 24.285714285714285


# 3) Заменить в строке "asdxfghyxyx" все буквы "х" на "у"
test_string = "asdxfghyxyx"
result_string = test_string.replace('x', 'y')
print(result_string)
# asdyfghyyyy


# 4) Сосчитать произведение чисел [3, 4, 56, 100, 15, 2, 20, 30], кратных и 3 и 5.
values = [3, 4, 56, 100, 15, 2, 20, 30]

# Создадим пустой список кратных чисел
result_values = []
# Добавляем в новый список элементы если они кратны 3 или 5
for elem in values:
    if elem % 3 == 0 or elem % 5 == 0:
        result_values.append(elem)
print(result_values)
# [3, 100, 15, 20, 30]
# Если список не пустой, то делаем умножение элементов, для простоты присвоим начальное значение в 1
if result_values:
    result = 1
    for elem in result_values:
        result = result*elem
print(result)
# 2700000
    

# 5) Заменить все буквы "х" на "у" в исходной строке без использования дополнительной строки.
input_str = 'asdxfghyxyx'
print(input_str.replace('x', 'y'))
# asdyfghyyyy