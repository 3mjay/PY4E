import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl


ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

link = input("Enter URL: ")


uh = urllib.request.urlopen(link, context=ctx)
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
#num = results.find('comments').find('comment').find('count').text
