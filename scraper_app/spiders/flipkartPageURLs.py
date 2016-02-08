import urllib
import urllib
import unicodedata
import optparse
from urlparse import urlparse
import os.path
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)))
from models import db_connect


def process_item(start=0,numEntries=10):
		engine=db_connect()
		database="flipkartdata"
		offset=start;stepSize=numEntries
		query="select \"id\",\"apparelURL\" from "+database+" limit "+str(stepSize)+" offset "+str(offset)
		queryRes=engine.execute(query)
		result=list()
		for element in queryRes.fetchall():
			result.append("http://www.flipkart.com"+element[1])
		return result


def getURLSimple():
	# start_urls=list()	
	# # start_urls.append('http://www.flipkart.com/wrangler-women-s-solid-casual-shirt/p/itme8q4gjgqg42xc?pid=SHTE8Q4G5XQGF9SQ&al=ThsGnZDjLFHQALPQjf3S7MldugMWZuE7eGHgUTGjVrq34siOYkRdcylI1wIgMoStWjqoPwBrylw%3D&ref=L%3A145924790153660934&srno=b_8')
	# # start_urls.append('http://www.flipkart.com/hbhwear-solid-women-s-polo-neck-t-shirt/p/itme4g769excshzj?pid=TSHE4G76CXHXU456&al=ThsGnZDjLFEZTQtAEV05F8ldugMWZuE7wkNiXfq8GiR%2FMBq1PENgcSTIaBkyV9pqxSpxi8SNpDQ%3D&ref=L%3A145924790153660934&srno=b_14')
	# # start_urls.append('http://www.flipkart.com/hbhwear-solid-women-s-polo-neck-t-shirt/p/itme4g76ystz3jjh?pid=TSHE4G76ZFNBKZ6C&icmpid=reco_pp_personalhistoryFooter_womenclothing_na_5')
	# start_urls.append('http://www.flipkart.com/vero-moda-casual-women-s-top/p/itme8fmfnx7ukhsv?pid=TOPE8FMFGT5PFZHS&al=oTeXb3%2BdcWfgcf7QcZVhIsldugMWZuE7wkNiXfq8GiTNzsLCzdMSnQxbkyR58oGhUMkqngEt3uU%3D&ref=L%3A3444917640624687878&srno=b_107')
	# return start_urls
	return process_item()

def getURL():
	return getURLSimple()

if __name__ == '__main__':
	# pass
	# print getURL()
	process_item(4,1)

