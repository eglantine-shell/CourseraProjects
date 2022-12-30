import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

link = input('Enter URL: ')
count = int(input('Enter count: '))
pos = int(input('Enter position: '))

print('Retrieving:', link)
for i in range(0, count):
    html = urllib.request.urlopen(link, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    
    tags = soup('a')
    ps = 0
    for tag in tags:
        ps += 1
        if ps == pos:
            print('Retrieving:', str(tag.get('href', None)))
            link = str(tag.get('href', None))
            ps = 0
            break