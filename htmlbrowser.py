import urllib.request
import urllib.response

fhand = urllib.request.urlopen('http://127.0.0.1:8000/')
for line in fhand:
    print(line.decode().strip())

urllib.response.addclosehook
