from bs4 import BeautifulSoup
import urllib.request

url = "http://www.utexas.edu/world/univ/alpha/"

#open page using urlopen and create BS object using the second line. Now we can manipulate page using soup object methods!
page = urllib.request.urlopen(url)
soup = BeautifulSoup(page.read())

#next we use findAll method that searches through the soup object to match for text. we know that uni name and url has a pettern (a tag and that tag has css class institution!))
unis = soup.findAll('a',{'class':'institution'})

#traverse thru list of unis. during loop, eachuni[href] will give the link to the university because of the initial pattern, name of uni is the string following the a tag and thats y eachuni.string is used.
for eachuni in unis:
    print(eachuni['href']+", "+eachuni.string)
