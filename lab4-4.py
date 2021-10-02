"""
МНОЖЕСТВО в Python -  это структура данных, содержащая не повторяющиеся элементы в случайном порядке.
"""

a = set()  # Создание пустого множества

a.add(1)  # Добавление элемента в множество

a.add(2)

a.add(1)

print(a)  # Объясните результат
#Выведется два элемента которые мы добавили в множество, так как мы добавили два раза единицу а множество
#это структура данных, содержащая не повторяющиеся элементы в случайном порядке



b = set('hello')  # Преобразование строки в множество


print(b)  # Объясните результат
#В случайном порядке выведутся  буквы этого слова без повторение
"""
Множества удобно использовать для удаления повторяющихся элементов из списка
"""

a = ['aa', 'ab', 'aa', 'ba']


print(set(a))

"""
Множества поддерживают стандартные операции других структур данных - len, in, clear и т.п. 
"""

# Вставьте пропущенную строку, чтобы оператор print выводил True

b = ['aa', 'ab', 'aa', 'ba']

b = set(b)

print(len(b) == 3)

"""
Помимо базовых операций, множества в Python поддерживают операции математических множеств (объединение(union), пересечение(intersection))
"""

a = set({1, 2, 3, 4})  # Создание множества

b = set({3, 4, 5, 6})


c = a.union(b)  # Объединение множества

print(c)

# Вставьте пропущенное действие, чтобы в консоль вывелось пересечение множеств a и b

d = a.intersection(b)


print(d)