'''
Домашнее задание:
    
    1) При помощи класса описать сравнение строк
       любым методом
       
    2) Объект - экземпляр класса должен
       принимать 2 аргумента - строки для сравнения
       
    3) Метод сравнения должен возвращать
       степень похожести (как в примерах)
       
    4) Создать в __name__ == '__main__'
       экземпляр класса и вызвать его
       метод сравнения для строк из списка
       (как в сегодняшнем примере).
'''
from pymorphy2 import MorphAnalyzer

class Comparator:
    # Аргументы класса - две искомые строки 
    def __init__(self, s1, s2):
        self.s1 = s1
        self.s2 = s2
    # Метод класса - сравнение способом триграм
    def compare(self, s1, s2):
        ngrams = [s1[i:i+3] for i in range(len(s1))]
        count = 0
        for ngram in ngrams:
            count += s2.count(ngram)
        return count / max (len(s1), len(s2))
    
    def normalize_strings(self, s1, s2):
        ma = MorphAnalyzer()
        nf_s1 = ma.parse(s1)[0].normal_form
        nf_s2 = ma.parse(s2)[0].normal_form
        # Возвращаем кортеж нормализованных значений слов
        return nf_s1, nf_s2

    def normalized_compare(self, s1, s2):
        return self.compare(*self.normalize_strings(s1, s2))


if __name__ == '__main__':
    s1 = 'арбузов'
    s2 = 'арбуза'
    # Создаем экземпляр класса Comparator
    melons = Comparator(s1,s2)
    # Выводим результат полученный методом класса
    print(melons.normalized_compare(s1,s2))

