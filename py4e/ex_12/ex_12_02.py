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


# Exercise 2: Change your socket program so that it counts the number of characters
# it has received and stops displaying any text after it has shown 3000 characters.
# The program should retrieve the entire document and count the total number of
# characters and display the count of the number of characters at the end of the document.

# http://data.pr4e.org/romeo.txt

import socket

url = input("Enter URL: ")

try:
    host = url.split("/")[2]
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect((host, 80))
    cmd = 'GET '+ url +' HTTP/1.0\r\n\r\n'
    cmd = cmd.encode()
    mysock.send(cmd)

    received = b""

    while True:
        data = mysock.recv(512)
        if len(data) < 1:
            break
        received += data

    received = received.decode()
    print(received[:3000])
    print(len(received))

    mysock.close()
except:
    print("improperly formatted or non-existent URL.")
    quit()
