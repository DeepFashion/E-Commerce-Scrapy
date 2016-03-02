import urllib
import urllib
import unicodedata
import optparse
from urlparse import urlparse
import os.path
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)))
from models import db_connect


def process_item():
		engine=db_connect()
		database="jabongdata"
		stepSize=25000
		offset=50000
		query="select \"id\",\"image_320\",\"image_500\",\"image_768\",\"image_1024\",\"image_1280\" from "+database+" order by id limit "+str(stepSize)+" offset "+str(offset)
		queryRes=engine.execute(query)
		result=list()
		for element in queryRes.fetchall():
			for i in range(1,6):
				if element[i]:
					result.append(element[i])
		
		print len(result)
		res1=list(set(result))
		print len(res1)
		return res1



def getURLSimple():
	return process_item()

def getURL():
	return getURLSimple()

if __name__ == '__main__':
	pass
	process_item()
	