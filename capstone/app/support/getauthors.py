from bs4 import BeautifulSoup
import urllib.request
import json
import os

root_url = 'http://adab.com/'

def scrape_for_poem(url):
    webpage = urllib.request.urlopen(url)
    soup = BeautifulSoup(webpage.read())

    title = soup.findAll('title')
    table = soup.findAll('table')
    poemTableRows = table[5].findAll('tr')
    ID = table[4].findAll('td')[0].text[14:-1]
    era = table[3].findAll('a')[1].text

    authorAndTitle = title[0].text
    authorAndTitle = authorAndTitle.split(':')

    author = authorAndTitle[0].strip()
    name = authorAndTitle[1].strip()
    author = author[8:]

    poet = {"name": author}

    poem = {"title":name, "author":author, "era":era, "id":ID, "abyat":[]}

    for row in poemTableRows:
        col = row.findAll('td')
        sudr = col[0].text
        ajz = col[-1].text
        poem["abyat"].append({"sadr":sudr, "ajez":ajz, "bayt":sudr+ ajz})
        #fw.write(sudr +"        "+ ajz + "\n")

    filename = '%s.json' %ID
    path = '/home/ramez/python/capstone/app/jahili_json'
    fullpath = os.path.join(path,filename)

    with open(fullpath,"w") as outfile:
        json.dump(poem, outfile, ensure_ascii=False)


with open("jahili_poet_urls.txt") as f:
    #get the complete list that contains lists of poet poems. json was used because the list of lists has valid json syntax even tho its not json.
    all_poems = json.load(f)
    #accessing each poet individually
for poet_collection in all_poems:
    #access each poem individually get url
    for poet_poem in poet_collection:
        index_url = poet_poem
        poem_url = root_url + index_url
        print(poem_url)
        poem_json = scrape_for_poem(poem_url)
