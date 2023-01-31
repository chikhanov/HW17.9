numbers = input('Введите целые числа через пробел: ')
user_number = int(input('Введите любое число: '))
# Функция для определения цифр в строке
def is_int(str):
    str = str.replace(' ', '')
    try:
        int(str)
        return True
    except ValueError:
        return False
# Проверка соответствия указанному в условии ввода данных.
if " " not in numbers:
    print("\nВ ВВОДЕ ОТСУТСТВУЮТ ПРОБЕЛЫ (введите числа, согласно условиям ввода.)")
    numbers = input('Введите целые числа через пробел: ')
if not is_int(numbers):
    print('\nВ ВВОДЕ СОДЕРЖАТСЯ НЕ ЦИФРЫ ЛИБО НЕ ЦЕЛЫЕ ЧИСЛА (введите числа, согласно условиям ввода.)\n')
    print(error)
else:
    numbers = numbers.split()
# Меняем список строк на список чисел
list_numbers = [int(item) for item in numbers]
# Сортировка списка
def merge_sort(L):
    if len(L) < 2:
        return L[:]
    else:
        middle = len(L) // 2
        left = merge_sort(L[:middle])
        right = merge_sort(L[middle:])
        return merge(left, right)

def merge(left, right):
    result = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1
    return result

list_numbers = merge_sort(list_numbers)
# Установка позиции элемента
def binary_search(array, element, left, right):
    try:
        if left > right:
            return False
        middle = (right + left) // 2
        if array[middle] == element:
            return middle
        elif element < array[middle]:
            return binary_search(array, element, left, middle - 1)
        else:
            return binary_search(array, element, middle + 1, right)
    except IndexError:
        return 'Число выходит за диапазон списка, введите меньшее число.'
# Устанавливается номер позиции элемента, который меньше
# введенного пользователем числа, а следующий за ним больше или равен этому числу.
print(f'Упорядоченный по возрастанию список: {list_numbers}')

if not binary_search(list_numbers, user_number, 0, len(list_numbers)):
    rI = min(list_numbers, key=lambda x: (abs(x - user_number), x))
    ind = list_numbers.index(rI)
    max_ind = ind + 1
    min_ind = ind - 1
    if rI < user_number:
        print(f'''В списке нет введенного числа 
Ближайшее меньшее число: {rI}, его индекс: {ind}
Ближайшее большее число: {list_numbers[max_ind]} его индекс: {max_ind}''')
    elif min_ind < 0:
        print(f'''В списке нет введенного числа
Ближайшее большее число: {rI}, его индекс: {list_numbers.index(rI)}
В списке нет меньшего числа''')
    elif rI > user_number:
        print(f'''В списке нет введенного числа
Ближайшее большее число: {rI}, его индекс: {list_numbers.index(rI)}
Ближайшее меньшее число: {list_numbers[min_ind]} его индекс: {min_ind}''')
    elif list_numbers.index(rI) == 0:
        print(f'Индекс введенного числа: {list_numbers.index(rI)}')
else:
    print(f'Индекс введенного числа: {binary_search(list_numbers, user_number, 0, len(list_sequence_numbers))}')
