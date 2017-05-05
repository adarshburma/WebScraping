import urllib
from bs4 import BeautifulSoup

htmlFile = urllib.urlopen("http://www.yellow.com/best-match/?search_term=cafe&city=US+US&state=&is_cat=1")
soup = BeautifulSoup(htmlFile, 'html')
#print soup.prettify()

#links = soup.find_all("a")

#for link in links:
#	print "<a href = '%s'> %s </a> " %(link.get("href"),link.text)

cafes = soup.find_all("div" , {"class" : "yb-results-container position-relative"})

#reviews = soup.find_all("p" , {"class" : "yb-results-list-spaced"})


for cafe in cafes:
	print "Cafe : " + cafe.find_all("h2")[0].text + " Address :" + cafe.find_all("p")[0].text + " Number of Stars :" + cafe.find_all("div" , {"class" : "listing-stars clearAfter yb-results-list-spaced"})[-1].find_all("div")[5].text

