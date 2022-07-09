'''
Индивидуальный проект:
Будем использовать модуль requests для запроса данных о погодев выбранном городе из открытых источников.
Будем также использовать вспомогательные модули для более удобного отображения информации и для введения
искусственной задержки
'''
import requests

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

if __name__ == '__main__':
    print(get_weather('Perm'))
