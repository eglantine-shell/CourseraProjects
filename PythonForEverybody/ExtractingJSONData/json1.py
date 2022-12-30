import urllib.request, urllib.parse, urllib.error
import json

link = input('Enter location: ')
print('Retrieving', link)

html = urllib.request.urlopen(link).read().decode()
print('Retrieved', len(html), 'characters')

try:
    js = json.loads(html)
except:
    js = None

c = 0
s = 0
for item in js['comments']:
    c += 1
    s += int(item['count'])

print('Count:', c)
print('Sum:', s)