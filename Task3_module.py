# Модуль для сравнения строк S1 и S2
# Импортируем морфоанализатор
from pymorphy2 import MorphAnalyzer

# Функция для возврата нормализованного значения
def normalize_strings(s1, s2):
    ma = MorphAnalyzer()
    nf_s1 = ma.parse(s1)[0].normal_form
    nf_s2 = ma.parse(s2)[0].normal_form
    # Возвращаем кортеж нормализованных значений слов
    return nf_s1, nf_s2

# Функция сравнения методом триграмм. Результат - коэффициент похожести
def compare(string_pair):
    s1, s2 = string_pair
    ngrams = [s1[i:i+3] for i in range(len(s1))]
    count = 0
    for ngram in ngrams:
        count += s2.count(ngram)
    return count / max (len(s1), len(s2))

# Функция проводит первичную нормализацию и сравнение методом триграмм двух строк
def normalized_compare(s1, s2):
    return compare(normalize_strings(s1, s2))
    


if __name__ == '__main__':
    s1 = 'арбузов'
    s2 = 'арбуза'
    result = normalized_compare(s1, s2)
    print(result)