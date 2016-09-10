#!/usr/bin/env python3.2
from bs4 import BeautifulSoup
import urllib.request

url = urllib.request.urlopen("http://www.python.org")

content = url.read()

soup = BeautifulSoup(content)

links = soup.findAll("a")

print(links)
