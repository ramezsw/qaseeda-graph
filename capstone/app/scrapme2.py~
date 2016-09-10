from bs4 import BeautifulSoup
import urllib.request
import re

#cp all of the content from webpage.
webpage = urllib.request.urlopen('http://www.huffingtonpost.com/weird-news/').read()

#grab everything that lies between the tite tags using a regex
patFinderTitle = re.compile(b'')

#grab the link of the original article using regex.
patFinderLink = re.compile(b'')

#store all titles and links found in 2 lists.
findPatTitle = re.findall(patFinderTitle, webpage)

findPatLink = re.findall(patFinderLink, webpage)

listIterator = []

listIterator[:] = range(2,16)

soup2 = BeautifulSoup(webpage)

titleSoup = soup2.findAll("title")
linkSoup = soup2.findAll("link")

for i in listIterator:
    #print(titleSoup[i])
    print(linkSoup[i])
    print("\n")
