import urllib
import unicodedata
from models import db_connect
import optparse
from urlparse import urlparse

folder=""

class DownloadImagesFlipkart(object):
	engine=None
	database="flipkartdata"
	def __init__(self,callback,dest):
		self.engine = db_connect()
		self.callback=callback
		self.dest=dest

	def getImage(self,Id,primaryUrl,urlList):
		print Id
		count=0
		for url in urlList:
			count+=1
			url=unicodedata.normalize('NFKD',url).encode('ascii','ignore')
			self.callback(url,self.dest(url,Id,self.database,count))
		

	def process_item(self):
		engine = self.engine
		offset=0;stepSize=10
		count=engine.execute("select count(*) from "+self.database);
		numImages=count.fetchall()[0][0]
		while offset < numImages:
			query="select \"id\",\"mainImage\",\"images\" from "+self.database+" limit "+str(stepSize)+" offset "+str(offset)
			queryRes=engine.execute(query)
			for element in queryRes.fetchall():
				l=element[2].split('|')
				self.getImage(element[0],element[1],l)
			offset+=10
		



class DownloadImagesJabong(object):
	engine=None
	database="jabongdata"
	def __init__(self,callback,dest):
		self.engine = db_connect()
		self.callback=callback
		self.dest=dest


	def getImage(self,Id,var):
		print Id
		for key,val in var.iteritems():
			self.callback(val,self.dest(val,Id,self.database,key))


	def process_item(self):
		engine = self.engine
		offset=0;stepSize=10
		count=engine.execute("select count(*) from "+self.database);
		numImages=count.fetchall()[0][0]
		while offset < numImages:
			query="select \"id\",\"image_320\",\"image_500\",\"image_768\",\"image_1024\",\"image_1280\" from "+self.database+" limit "+str(stepSize)+" offset "+str(offset)
			queryRes=engine.execute(query)
			
			for element in queryRes.fetchall():
				var=dict()
				var['image_320']=element[1]
				var['image_500']=element[2]
				var['image_768']=element[3]
				var['image_1024']=element[4]
				var['image_1280']=element[5]
				self.getImage(element[0],var)
			offset+=10


class DownloadImagesPolyvore(object):
	engine=None
	database="polyvoredata"

	def __init__(self,callback,dest):
		self.engine = db_connect()
		self.callback=callback
		self.dest=dest

	def getImage(self,Id,imgURL):
		print Id
		self.callback(imgURL,self.dest(imgURL,Id,self.database,""))

	def process_item(self):
		engine = self.engine
		offset=0;stepSize=10
		count=engine.execute("select count(*) from "+self.database);
		numImages=count.fetchall()[0][0]
		while offset < numImages:
			query="select \"id\",\"productImage\" from "+self.database+" limit "+str(stepSize)+" offset "+str(offset)
			queryRes=engine.execute(query)
			for element in queryRes.fetchall():
				self.getImage(element[0],element[1])
			offset+=10


def downloadImage(imgURL,destURL):
	global folder
	urllib.urlretrieve(imgURL,folder+destURL)

def getDest(imgURL,Id,database,others):
	extension=imgURL.split('.')[-1]
	return str(database)+"_"+str(others)+"_"+str(Id)+"."+str(extension)

def getDestPolyvore(imgURL,Id,database,others):
	details=urlparse(imgURL)
	queryStr={x.split('=')[0]:(x.split('=')[1]) for x in details.query.split("&")}
	extension=queryStr['.out']
	return str(database)+"_"+str(others)+"_"+str(Id)+"."+str(extension)


def parse_args():

	usage="""
		use flag --loc with arguement [location of folder] terminated by /
		use flag --db with arguement [Database Name]

	"""
	parser = optparse.OptionParser(usage)

	help = "Specify the folder to dump files terminated by /"
	parser.add_option('--loc',help=help)

	help = "specify the name of database eg: [flipkart/jabong/polyvore]"
	parser.add_option('--db', help=help)

	options, args = parser.parse_args()

	if not options.db or not options.loc:
		parser.error('Both the arguments are compulsary')

	return options

if __name__ == '__main__':
	options=parse_args()	
	global folder
	folder=options.loc
	db=options.db
	if db=="flipkart":
		DownloadImagesFlipkart(downloadImage,getDest).process_item()
	elif db=="jabong":
		DownloadImagesJabong(downloadImage,getDest).process_item()
	elif db=="polyvore":
		DownloadImagesPolyvore(downloadImage,getDestPolyvore).process_item()
	else:
		print "Unknown Db"


