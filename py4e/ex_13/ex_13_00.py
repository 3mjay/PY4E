import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

all_link_list = list()
linkpos = 3
process_repeat = 4
## Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

link = input('Enter URL: ')
cont = int(input("Enter count: "))
line = int(input("Enter position: "))

print('Retrieving: ', link)
for i in range(0, cont):
    html = urllib.request.urlopen(link, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    ## Retrieve all of the anchor tags
    tags = soup('a')
    cn = 0
    ps = 0
    for tag in tags:
        ps += 1
        if ps == line:
            print("Retrieving:", str(tag.get('href', None)))
            link = str(tag.get('href', None))
            ps = 0
            break
