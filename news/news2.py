import xml.etree.ElementTree as ET
from urllib.request import urlopen
import json

res = []
data = urlopen('https://lenta.ru/rss').read().decode('utf8')
items = ET.fromstring(data).find('channel').findall('item')
for item in items:
    data = {}
    for child in item:
        data.update({child.tag: child.text})
    res.append(data)
with open('news2.json', 'w', encoding='utf8') as file:
    json.dump(res, file, indent=1, sort_keys=True)