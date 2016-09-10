from bs4 import BeautifulSoup
import urllib.request

url = "http://adab.com/modules.php?name=Sh3er&doWhat=shqas&qid=23028&r=&rc=0"

page = urllib.request.urlopen(url)
soup = BeautifulSoup(page.read())

fw = open("write.txt","w")

table = soup.findAll('table')
asr = table[3].findAll('a')[1].text

fw.write(asr)
fw.close()
