import xml.etree.ElementTree as ET
from urllib.request import urlopen
import json

tags, res = ('pubDate', 'title'), []
data = urlopen('https://lenta.ru/rss').read().decode('utf8')
items = ET.fromstring(data).find('channel').findall('item')
for item in items:
    data = {}
    for tag in tags:
        data.update({tag: item.find(tag).text})
    res.append(data)
with open('news1.json', 'w', encoding='utf8') as file:
    json.dump(res, file, indent=1)
