#  Задайте список случайных чисел от 1 до 10, выведите все элементы больше 5. Используйте для решения лямбда-функцию.
#
# 2, 3, 4, 6, 7, 8 -> 6, 7, 8

import random
numbers = [random.randint(0 , 10) for _ in range(10)]
print(numbers)
new_numb = list(filter(lambda x: x > 5, numbers))
print(f'{new_numb} найдено чисел больше 5 -> {len(numbers) - len(new_numb)}')
