from bs4 import BeautifulSoup
import urllib.request

root_url = "http://adab.com"

webpage = urllib.request.urlopen(root_url)
soup = BeautifulSoup(webpage.read())

table = soup.findAll('table')
poemTableRows = table[5].findAll('tr')

print(poemTableRows)

fw = open("url.txt","w")
for row in poemTableRows:
    col = row.findAll('b')
    #sudr = col.text
    #ajz = col[-1].text
    #poem["abyat"].append({"sadr":sudr, "ajez":ajz})
    #fw.write(sudr +"        "+ ajz + "\n")
    fw.write(str(col)+ "\n")
fw.close()
