#!/usr/bin/env python3
# author: 0.382
# environment: win64 python3.7
# ----------------------------

from urllib import request
import codecs
from bs4 import BeautifulSoup
import sys
import re

def youdao_translate(words):
    youdao_URL = 'http://dict.youdao.com/w/{0}/#keyfrom=dict2.top'.format(words)
    response = request.urlopen(youdao_URL)
    html = response.read().decode('utf-8')
    soup = BeautifulSoup(html, 'html5lib')
    
    translate = {}
    pronounce_search = soup.find_all('span', class_ = 'pronounce')
    try:
        pronounce = {}
        for p in pronounce_search:
            p_key, p_value = p.stripped_strings
            pronounce[p_key] = p_value
        if pronounce != {}:
            translate['pronounce'] = pronounce
    except Exception as error:
        pass
    
    mean_search = soup.find('div', class_='trans-container')
    if mean_search != None:
        original_mean_search = mean_search.find_all('li')
        additional_mean_search = mean_search.find('p')
        original = []
        for li in original_mean_search:
            original.append(li.contents[0])
        translate['original'] = original
    try:
        additional = additional_mean_search.contents[0]
        additional = re.sub(r'(\[\n +)|(\n +\])|(\n +)', '\n', additional)
        translate['additional'] = additional[1:-1]
    except Exception as error:
        pass
    
    return translate

def print_translate(translate):
    if 'pronounce' in translate.keys():
        print('pronounce:')
        for item in translate['pronounce'].items():
            print(item[0], item[1])
    if 'original' not in translate.keys():
        print('翻译失败')
        exit()
    print('mean:')
    for li in translate['original']:
        print(li)
    if 'additional' in translate.keys():
        print('other:')
        print(translate['additional'])
    
if __name__ == '__main__':
    try:
        words = ' '.join(sys.argv[1:])
        translate = youdao_translate(words)
        print_translate(translate)
    except Exception as error:
        print(error)
        print('无效输入')