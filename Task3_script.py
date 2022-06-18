from Task3_module import normalized_compare

values = ['арбуз', 'арбузов', 'гора', 'архитектор', 'буровая', 'арбузный']
const = 'арбуз'

# Перебираем элементы в списке слов, сравниваем со словом константой, если коэффициент совпадения больше 0.5, то печатаем слово.
for elem in values:
    if normalized_compare(const, elem) > 0.5:
        print(elem)