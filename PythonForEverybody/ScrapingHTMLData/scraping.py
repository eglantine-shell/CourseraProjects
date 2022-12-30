import urllib.request, urllib.parse, urllib.error
import bs4
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

link = input('Enter - ')
html = urllib.request.urlopen(link, context = ctx).read()
soup = BeautifulSoup(html, 'html.parser')

tags = soup('span')
sum = 0
count = 0
for tag in tags:
    count += 1
    sum += int(tag.contents[0])

print('Count', count)
print('Sum', sum)