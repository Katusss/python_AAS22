'''
Индивидуальный проект:
Будем использовать модуль requests для запроса и отображения кратких данных 
о погоде в выбранном городе из открытых источников.
Будем также использовать вспомогательные модули для более удобного отображения
информации и для введения искусственной задержки.
'''

import requests
import time
from tabulate import tabulate

def get_weather(city_name, lang='ru', units='metric'):
    '''Функция принимает на вход название города на любом языке. 
    Для запроса погоды используется модуль requests и API сервиса openweathermap.org
    Функция возвращает текущую погоду в формате json
    '''
    # Используем бесплатный тариф и генерируем API ключ
    api_key = 'c7e636033cb0e8a941b06951023b7cde'
    # Адрес запроса текущей погоды
    api_url = f'https://api.openweathermap.org/data/2.5/weather'
    r = requests.get(url=api_url, params=dict(q=city_name, appid=api_key, lang=lang, units=units))
    return r.json()

def parse_weather_output(data):
    '''Функция принимает на вход словарь c ответом от погодного сервиса 
    и возвращает словарь с ключами:
    Город, Текущая температура, Ощущаемая температура, Погодные условия, Ветер (м/с)
    '''
    # Проверка, что сервис вернул корректные данные
    if data['cod'] == 200:
        d_keys = ['Город', 'Текущая температура', 'Ощущаемая температура', 'Погодные условия', 'Ветер (м/с)']
        d_values = [data['name'], data['main']['temp'], data['main']['feels_like'], data['weather'][0]['description'], data['wind']['speed']]
        result = dict(zip(d_keys, d_values))
    else:
        result = False
    return result

def parse_user_input():
    '''Функция принимает на вход перечень городов через запятую и возвращает
    cписок словарей с данными о погоде в каждом городе. 
    Перечень ключей каждого словаря:
    Город, Текущая температура, Ощущаемая температура, Погодные условия, Ветер (м/с)
    '''
    user_data = input('Введите город или города в формате Город_1, Город_2, Город_3: ')
    result = []
    # Базовая проверка, что введены какие-то буквы
    if user_data.isalpha:
        # Получаем список городов, отсекая лишние пробелы
        cities = [city.strip() for city in user_data.split(',')]
    else:
        print('Ошибочный ввод')
    for city in cities:
        weather_data = parse_weather_output(get_weather(city))
        if weather_data:
            result.append(weather_data)
        else:
            print(f'Сервис не может отобразить данные по городу: {city}')
        # Вводим искусственную задержку для взаимодействия с сервисом, т.к. используем бесплатный тариф
        time.sleep(1)
    return result
        
def print_user_data(data, headers='keys', tablefmt='grid', stralign='left'):
    '''Функция ожидает на вход список словарей и делает вывод на экран в формате
    таблицы с заголовками - ключами словарей. Формат таблицы кастомизируется ключами.
    '''
    print(tabulate(data, headers=headers, tablefmt=tablefmt, stralign=stralign))




if __name__ == '__main__':
    print_user_data(parse_user_input())
