import urllib
from bs4 import BeautifulSoup

def test():
    url=urllib.urlopen("http://www.nyu.edu/life/travel-and-transportation/university-transportation/routes-and-schedules/route-a.html")
    result = BeautifulSoup(url)
    return result

print(test())
