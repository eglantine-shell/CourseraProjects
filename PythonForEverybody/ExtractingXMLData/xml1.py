import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

link = input('Enter location: ')
html = urllib.request.urlopen(link).read().decode()
print('Retrieving', link)
print('Retrieved', len(html), 'characters')

count = 0
sum = 0
data = ET.fromstring(html)
tags = data.findall('comments/comment')

for tag in tags:
    count += 1
    sum += int(tag.find('count').text)

print('Count:', count)
print('Sum:', sum)
