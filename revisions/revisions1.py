from urllib.request import urlopen
from json import loads
from itertools import groupby
from datetime import datetime


def get_date(revision):
    return datetime.strptime(revision['timestamp'], '%Y-%m-%dT%H:%M:%SZ').date()


url = 'https://ru.wikipedia.org/w/api.php?action=query&format=json&prop=revisions&rvlimit=500&titles=' \
      '%D0%93%D1%80%D0%B0%D0%B4%D1%81%D0%BA%D0%B8%D0%B9,' \
      '_%D0%90%D0%BB%D0%B5%D0%BA%D1%81%D0%B0%D0%BD%D0%B4%D1%80_%D0%91%D0%BE%D1%80%D0%B8%D1%81%D0%BE%D0%B2%D0%B8%D1%87'
data = loads(urlopen(url).read().decode('utf8'))
groups = groupby(sorted(data['query']['pages']['183903']['revisions'], key=get_date, reverse=True), get_date)
statistics = {}
for date, revisions in groups:
    statistics.update({date: len(list(revisions))})
with open('revisions1.txt', 'w', encoding='utf8') as file:
    for date in statistics:
        print(date, statistics[date], file=file)


