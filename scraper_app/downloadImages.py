import urllib
imgURL="http://img5a.flixcart.com/image/kurta/v/n/p/716kurt09m-indigo-fusion-beats-3xl-400x400-imaef5hmq2nhqxk2.jpeg"
destURL="00000001.jpg"
urllib.urlretrieve(imgURL,destURL)

class DownloadIamges(object):
	def __init__(self):
		engine = db_connect()
        self.Session = sessionmaker(bind=engine)

        def getURL():
        	