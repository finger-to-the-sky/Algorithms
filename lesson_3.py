# Практическое задание № 1
# 1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.




result = {}

for i in range(2, 10):
    result[i] = []
    for x in range(2, 100):
        if x % i == 0:
            result[i].append(x)
    print(f'Для числа {i} кратны {len(result[i])}. Кратные числа: {result[i]}')



# Практическое задание № 2
# 2. Во втором массиве сохранить индексы четных элементов первого массива. Например, если дан массив со значениями
# 8, 3, 15, 6, 4, 2, то во второй массив надо заполнить значениями 1, 4, 5, 6 (или 0, 3, 4, 5 - если индексация начинается
# с нуля), т.к. именно в этих позициях первого массива стоят четные числа.


ls = [2, 5, 8, 12, 31, 41, 77, 22]

result = [ls.index(i) for i in ls if i % 2 == 0]

print(f'Индексы четных чисел: {result}')


# Практическое задание № 3
# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.



res = [2, 5, 123, 45, 13, 87, 55, 20, 11, 3]
print(f'Наш массив - {res}')
num_min = min(res)
num_max = max(res)

id_1 = res.index(num_min)
id_2 = res.index(num_max)

res[id_1] = num_max
res[id_2] = num_min

print(f'Элементы {num_min} и {num_max} поменялись местами.\nНаш массив - {res}')

# Практическое задание № 4
# 4. Определить, какое число в массиве встречается чаще всего.


list_1 = [1, 2, 3, 3, 3, 4, 5, 5, 5, 5, 5]
list_2 = []

for i in range(0, len(list_1)):
    count = list_1.count(list_1[i])
    list_2.append(count)

print(f'Самое частое число: {max(list_2)}.')


# Практическое задание № 5
# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.

import random

list_3 = [random.randint(-20, 0) for _ in range(20)]
print(list_3)
print(f'Минимальное число: {min(list_3)}. Его позиция: №{list_3.index(min(list_3)) + 1} в списке.')

# Практическое задание № 6
# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

list_4 = [random.randint(1, 20) for _ in range(15)]

print(f'Наш список чисел - {list_4}')

idx_1 = list_4.index(min(list_4))
idx_2 = list_4.index(max(list_4))

if idx_1 < idx_2:
    result = list_4[idx_1+1:idx_2]

else:
    result = list_4[idx_2+1:idx_1]

print(f'Индекс мин. числа: {idx_1},\nИндекс макс. числа: {idx_2}.'
      f'\nСумма чисел между мин и макс элементами: {sum(result)}')


# Практическое задание № 7
# 7. В одномерном массиве целых чисел определить два наименьших элемента. Они могут быть как равны между собой
# (оба являться минимальными), так и различаться.

list_5 = [1, 3, 5, 6, 7, 10, 15]
res_list = list_5[:]
# Cоздав копию списка мы не будем менять структуру основного и вычислим второе минимальное число путем удаления одного.
minimum_1 = min(list_5)
res_list.remove(minimum_1)

minimum_2 = min(res_list)

if minimum_1 == minimum_2:
    print(f'Минимальные числа в массиве {minimum_1} и {minimum_2}')
else:
    print(f'Минимальные числа в массиве {minimum_1} и {minimum_2}')




# Практическое задание № 8
# 8. Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк. Программа должна вычислять сумму
# введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
# В конце следует вывести полученную матрицу.

matrixx = []
def matrix():
    count = 0

    while count != 20:
        number = int(input("Введите число: "))
        matrixx.append(number)
        count = count + 1
        if count == 5:
            row1 = (f'{matrixx[0]}\t{matrixx[1]}\t{matrixx[2]}\t{matrixx[3]}\t{matrixx[4]}\n')
        if count == 10:
            row2 = (f'{matrixx[5]}\t{matrixx[6]}\t{matrixx[7]}\t{matrixx[8]}\t{matrixx[9]}\n')
        if count == 15:
            row3 = (f'{matrixx[10]}\t{matrixx[11]}\t{matrixx[12]}\t{matrixx[13]}\t{matrixx[14]}\n')
        if count == 20:
            row4 = (f'{matrixx[15]}\t{matrixx[16]}\t{matrixx[17]}\t{matrixx[18]}\t{sum(matrixx)}\n')

    return row1 + row2 + row3 + row4
print(matrix())

# Практическое задание № 9
# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.

print(matrixx)


column_1 = min([matrixx[0], matrixx[5], matrixx[10], matrixx[15]])
column_2 = min([matrixx[1], matrixx[6], matrixx[11], matrixx[16]])
column_3 = min([matrixx[2], matrixx[7], matrixx[12], matrixx[17]])
column_4 = min([matrixx[3], matrixx[8], matrixx[13], matrixx[18]])
column_5 = min([matrixx[4], matrixx[9], matrixx[14], matrixx[19]])

result_column = max(column_1, column_2, column_3, column_4, column_5)
print(f'Максимальный элемент среди минимальных стобцов: {result_column}')