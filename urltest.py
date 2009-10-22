import urllib
from BeautifulSoup import *

class ComputerLab():
	def __init__(self, room, num, time):
		self.room = room
		self.num = num
		self.time = time

	def __repr__(self):
		str = "Room: %s\nNum: %s\nTime: %s\n" % (self.room, self.num, self.time)
		return str

url = "https://tomcat.itap.purdue.edu:8445/ICSWeb/AvailableStations"
page = urllib.urlopen(url)
soup = BeautifulSoup(page.read())
xp = []
mac = []
sun = []
labs = [xp, mac, sun]

i=0
j=0
for tbl in soup.findAll('table'):
	if (i==0):
		i=1
		continue	
	for tr in tbl.findAll('tr'):
		if (len(tr.contents) > 2):
			a = ComputerLab(None, None, None)
			a.room = tr.contents[0].find('font').contents[0]
			a.num = tr.contents[1].find('font').contents[0]
			a.time = tr.contents[2].find('font').contents[0]
			labs[j].append(a)
	j+=1

for labos in labs:
	for lab in labos:
		print lab
	print



