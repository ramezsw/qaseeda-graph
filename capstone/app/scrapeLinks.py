import urllib.request
from bs4 import BeautifulSoup

root_url = "http://adab.com/"
jahili_url = root_url + 'modules.php?name=Sh3er&doWhat=lstsh&catid=17&r=n_asc&start=0'
#islami_url = root_url + 'modules.php?name=Sh3er&doWhat=lstsh&catid=19&r=n_asc&start=0'
#abbasi_url = root_url + 'modules.php?name=Sh3er&doWhat=lstsh&catid=15&r=n_asc&start=0'
#andalsi_url = root_url + 'modules.php?name=Sh3er&doWhat=lstsh&catid=20&r=n_asc&start=0'
#index url here is 1 or the 4 main eras were working with, change this manually when scrapping for links.

fw = open("ja_poet_urls.txt","w")
#do not scrape url of eras, the code below opens the URL of the specific era that I manually provide, fetches all the links of author names, and thats it; it now fetches all the names of authors in different pages(1,2,3...) then access these links using different method. put param in this method that takes URL(1 of the 4 era urls) this same method can be applied on the URLs containing author names to access their poems.
def scrape_for_links(url):
    webpage = urllib.request.urlopen(url)
    soup = BeautifulSoup(webpage.read())
    table = soup.findAll("table")
    tablerows = table[5].findAll("a")[2:]
    links = []
    for link in tablerows:
        links.append(link.get('href'))
    next= soup.findAll('a',{'class':'tiny'})
    #print(next[:-1])
    for ea in next[:-1]:#ea is the URL of page
        url = root_url+ea.get('href')
        #print(url)
        page = urllib.request.urlopen(url)
        soup = BeautifulSoup(page.read())
        table = soup.findAll("table")
        tablerows = table[5].findAll("a")[2:]
        for link in tablerows:
            links.append(link.get('href'))
        #print(ea['href']+", "+ea.string)
    print(len(links))
    return links
#different methods because the webpage is ugly and retarded.
def scrape_for_poem_links(url):
    webpage = urllib.request.urlopen(url)
    soup = BeautifulSoup(webpage.read())
    table = soup.findAll("table")
    tablerows = table[4].findAll("a")
    links = []
    for link in tablerows:
        links.append(link.get('href'))
    next= soup.findAll('a',{'class':'tiny'})
    #print(next[:-1])
    for ea in next[:-1]:
        url = root_url+ea.get('href')
        #print(url)
        page = urllib.request.urlopen(url)
        soup = BeautifulSoup(page.read())
        table = soup.findAll("table")
        tablerows = table[4].findAll("a")
        for link in tablerows:
            links.append(link.get('href'))
        #print(ea['href']+", "+ea.string)
    print(len(links))
    return links


URL = scrape_for_links(jahili_url)#should give me alist called URL containing all links for jah
#print(len(URL))
for each in URL:
    lin = root_url+each
    fw.write(str(scrape_for_poem_links(lin)))
fw.close()
    #print(lin)
    #poet = scrape_for_poem_links(lin)
    #print(poet)
#fw.close()

#the above method is simply first getting the links on page 1 of given 3aser, then iterating to page2;get its links, jump onto page3; get its links, then go to altali link and get its links

#fw.write(str(scrape_for_links(andalsi_url)))
#fw.close()
