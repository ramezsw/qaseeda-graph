from bs4 import BeautifulSoup
import urllib.request

pageFile = urllib.request.urlopen("http://www.reddit.com")

pageHtml = pageFile.read()
pageFile.close()

soup = BeautifulSoup("".join(str(pageHtml)))

sAll = soup.findAll("a")

for href in sAll:
    print(href)

#need to check the final scrapping excersice and read the other tutorials, then check out adab.com source and first try on one poem, then try to do it for many poems at once!! enjoy <:-)
