import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/comments_42.xml'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/xml?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# while True:
#     address = input('Enter location: ')
#     if len(address) < 1: break
#address = input("Enter URL: ")
count = 0
parms = dict()
parms['count'] = count
if api_key is not False: parms['key'] = api_key
url = serviceurl + urllib.parse.urlencode(parms)
print('Retrieving', url)

uh = urllib.request.urlopen(url, context=ctx)
data = uh.read()
print('Retrieved', len(data), 'characters')
#print(data.decode())
tree = ET.fromstring(data)

# XPath selector string to look through the entire tree of XML for any tag named 'count' with the following line of code:
# ** counts = tree.findall('.//count') **
#
# You could also work from the top of the XML down to the comments node and then loop through the child nodes of the comments node.

results = tree.findall('commentinfo')
# print(results)
# counts = tree.findall('.//count')
# print(counts.decode())
num = results[0].find('comments').find('comment').find('count').text
print(num)
