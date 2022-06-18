# Персонажи книги Гарри Поттер
# Опишем словарем, списком и множеством

# Составим список персонажей, можно обращатсья по индексу элемента начиная с 0 и при необходимости перебирать и изменять список
hogwarts_students = ['Harry Potter', 'Hermione Granger', 'Ron Weasly']

# Поиск элемента возможен по индексу:
print(hogwarts_students[0]) 
# Вывод: Harry Potter

# Изменение списка (удаление элемента)
hogwarts_students.remove("Harry Potter")
print(hogwarts_students) 
# Вывод: ['Hermione Granger', 'Ron Weasly']


# То же самое можно описать множеством.
hogwarts_students = {'Harry Potter', 'Hermione Granger', 'Ron Weasly'}
# Обращаться по номеру уже нельзя, но можно убрать дубли, если они вдруг есть:
hogwarts_students = {'Harry Potter', 'Hermione Granger', 'Ron Weasly', 'Ron Weasly'}
print(hogwarts_students) 
# Вывод: {'Harry Potter', 'Ron Weasly', 'Hermione Granger'}
# Также можно найти пересечения между двумя множествами и сразу убрать дубли например:
# Первое множество, ученики Хогвартса
hogwarts_students = {'Harry Potter', 'Hermione Granger', 'Ron Weasly'}
# Второе множество - члены семьи Гарри
harrys_family = {'Harry Potter', 'Dudley Dursley', 'Vernon Dursley', 'Petunia Dursley'}
# Вычислим, кто из семьи Гарри попал в Хогвартс через пересечение множеств
who_is_in_hogwarts = hogwarts_students & harrys_family
print(who_is_in_hogwarts)
# Вывод: {'Harry Potter'}

# Применим словари:
# Ученики по факультетам, для примера уникальные ключи - имена учеников
faculty = {'Harry Potter': 'Gryffindor', 'Hermione Granger': 'Gryffindor', 'Ron Weasly': 'Gryffindor', 'Drako Malfoy': 'Slytherin'}

# Можно искать по ключу, например найдем факультет на котором учится Гарри
print(faculty['Harry Potter'])
# Вывод: Gryffindor

# Можем добавить в словарь новую запись, нужно чтоб ключ был уникальным, иначе перезапишется значение у текущего ключа:
faculty['Vincent Crabbe'] = 'Slytherin'

print(faculty)
# Вывод:
# {'Harry Potter': 'Gryffindor', 'Hermione Granger': 'Gryffindor', 'Ron Weasly': 'Gryffindor', 'Drako Malfoy': 'Slytherin', 'Vincent Crabbe': 'Slytherin'}