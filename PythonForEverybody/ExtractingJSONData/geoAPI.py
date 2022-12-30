import urllib.request, urllib.parse, urllib.error
import json

api = 'http://py4e-data.dr-chuck.net/json?'
loc = input('Enter location: ')
link = api + urllib.parse.urlencode({'address':loc, 'key':42})
print('Retrieving', link)

html = urllib.request.urlopen(link).read().decode()
print('Retrieved', len(html), 'characters')

try:
    js = json.loads(html)
    print('Place id', js['results'][0]['place_id'])
except:
    js = None
    print('No Address...')