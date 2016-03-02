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
		database="flipkartdata"
		stepSize=30000
		offset=50000
		query="select \"id\",\"mainImage\",\"images\" from "+database+" order by id limit "+str(stepSize)+" offset "+str(offset)
		queryRes=engine.execute(query)
		result=list()

		for element in queryRes.fetchall():
			if element[1]:
				result.append(element[1])
			if element[2]:
				l=element[2].split('|')
				for t in l:
					if t:
						result.append(t)

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
	