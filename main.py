import json
import xml.etree.ElementTree as ET
from collections import Counter

# Задача №1
with open('newsafr.json', encoding='utf-8') as json_file:
    news_json = json.load(json_file)['rss']['channel']['items']
    word_count_json = Counter()
    for description in news_json:
        for word in description['description'].split(' '):
            if len(word) > 6:
                # print(word)
                word_count_json[word] += 1

    sorted_tuple = sorted(word_count_json.items(), key=lambda x: x[1])
    word_count_json = dict(reversed(sorted_tuple))

    print('Топ 10 самых часто встречающихся в новостях слов длиннее 6 символов в json файле:')
    for word, count in list(word_count_json.items())[:10]:
        print(f'Слово "{word}" встречается {count} раз')

print()
print('*************************')
print()
# Задача №2
news_xml = ET.parse('newsafr.xml').getroot()
description_list = news_xml.findall("channel/item/description")
word_count_xml = Counter()
for description in description_list:
    for word in description.text.split(' '):
        if len(word) > 6:
            word_count_xml[word] += 1

sorted_tuple = sorted(word_count_xml.items(), key=lambda x: x[1])
word_count_xml = dict(reversed(sorted_tuple))

print('Топ 10 самых часто встречающихся в новостях слов длиннее 6 символов в xml файле:')
for word, count in list(word_count_xml.items())[:10]:
    print(f'Слово "{word}" встречается {count} раз')
