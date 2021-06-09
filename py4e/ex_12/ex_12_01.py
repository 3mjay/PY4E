# # **Using BeautifulSoup
# import urllib.request, urllib.parse, urllib.error
# from bs4 import BeautifulSoup
# import ssl
#
# # Ignore SSL certification error
# ctx = ssl.create_default_context()
# ctx.check_hostname = False
# ctx.verify_mode = ssl.CERT_NONE
#
# url = input('Enter - ')
# html = urllib.request.urlopen(url, context=ctx).read()
# soup = BeautifulSoup(html, 'html.parser')
#
# # Retrieve all of the anchor tags
# tags = soup('a')
# for tag in tags:
#     print(tag.get('href', None))

# Exercise 1: Change the socket program socket1.py to prompt the user for the URL
# so it can read any web page. You can use split('/') to break the URL into its
# component parts so you can extract the host name for the socket connect call.
# Add error checking using try and except to handle the condition where the user
# enters an improperly formatted or non-existent URL.

import socket

url = input("Enter URL: ")

try:
    host = url.split("/")[2]
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect((host, 80))
    cmd = 'GET '+ url +' HTTP/1.0\r\n\r\n'
    cmd = cmd.encode()
    mysock.send(cmd)

    while True:
        data = mysock.recv(512)
        if len(data) < 1:
            break
        print(data.decode(),end='')

    mysock.close()
except:
    print("improperly formatted or non-existent URL.")
    quit()
