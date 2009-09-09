from mechanize import Browser
from BeautifulSoup import BeautifulSoup

mech = Browser()
mech.addheaders = [ ('User-agent', 'Mozilla/5.0 (compatible)') ]
mech.set_handle_robots(False)
url = "http://www.google.com/search?hl=en&safe=off&client=firefox-a&channel=s&rls=org.mozilla%3Aen-US%3Aofficial&q=cheese&aq=f&oq=&aqi=g10"
page = mech.open(url)
html = page.read()
soup = BeautifulSoup(html)

#print soup.prettify()
#table = soup.find("li", class="g")
#print table
i=1
print "oh snap! heres some links!"
while (i < 50):
    for result in soup.findAll("li", "g"):
        link = result.find("a")
        print 'Link %d: ' % i,
        print link['href']
        i += 1
    navtbl = soup.find("table", id="nav")
    arrows = navtbl.findAll("td", "b")
    nexturl = arrows[1].find("a");
    page = mech.open(nexturl['href'])
    html = page.read()    
    soup = BeautifulSoup(html)
