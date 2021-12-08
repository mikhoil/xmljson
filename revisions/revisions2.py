from urllib.request import urlopen
from json import loads
from itertools import groupby
from datetime import datetime


def get_date(revision):
    return datetime.strptime(revision['timestamp'], '%Y-%m-%dT%H:%M:%SZ').date()


url = 'https://ru.wikipedia.org/w/api.php?action=query&format=json&prop=revisions&rvlimit=500&titles=' \
      '%D0%91%D0%B5%D0%BB%D1%8C%D0%BC%D0%BE%D0%BD%D0%B4%D0%BE,' \
      '_%D0%96%D0%B0%D0%BD-%D0%9F%D0%BE%D0%BB%D1%8C'
data = loads(urlopen(url).read().decode('utf8'))
groups = groupby(data['query']['pages']['192203']['revisions'], get_date)
max_count, date_death = 0, datetime.now()
for date, revisions in groups:
    count = len(list(revisions))
    if count > max_count:
        max_count, date_death = count, date
print(date_death)
# 2021-09-06 - день смерти Жан-Поля Бельмондо.
# Такой метрикой пользоваться можно, но всегда есть риск,
# что о каком-либо человеке упоминаний было больше при его жизни