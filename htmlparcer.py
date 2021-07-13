#exresice following links in python, how iwant to write it
#this one is extracting possible link from a home URL (first one), position is how much links to extract, and count is how many times each link willbe extracted
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
if len(url) < 1:
    url = "http://py4e-data.dr-chuck.net/known_by_Fikret.html"
count=input('Enter count:')
if len(count)<1:
    count=4
count=int(count)+1
position=input('Enter position:')
if len(position)<1:
    position=3
position=int(position)
while count>0:
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    positioncount=0
    count=count-1
    if count==0:break
    for tag in tags:
        url=tag.get('href', None)
        positioncount=positioncount+1
        print(positioncount,count, url)
        name=tag.contents[0]
        if positioncount==position:
            break
print(name)
