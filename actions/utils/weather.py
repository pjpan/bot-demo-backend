#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/7/12 1:23 下午
# @Author  : ppj
# @File    : weather.py
# @Software: PyCharm

import requests
import json
import power_data_toolkit as pdt

def weather(city_name):
    # api_address='http://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q='

    weather = pdt.weather.WeatherCrawler()
    json_data = weather.get_7d_weather(city_name=city_name)
    # url = api_address + city
    # json_data = requests.get(url).json()
    # format_add = json_data['main']
    # print(format_add)
    return json.dumps(json_data, ensure_ascii=False, sort_keys=True, indent=4, separators=(', ', ': '))


if __name__ == '__main__':
    print(weather("上海"))
    # print(json.dumps(pdt.weather.WeatherCrawler().get_real_time_weather('上海'),
    #                  ensure_ascii=False, sort_keys=True, indent=4, separators=(', ', ': ')))