import json
import yaml
import urllib,requests
import ast
def PostQuery(operator='plus',operand1='2',operand2='3'):
		myURL = "http://www.jabong.com/women/clothing/tops-tees-shirts/?source=topnav_women&ax=1&page=44&limit=100&sortField=popularity&sortBy=desc"
		r = requests.get(myURL)
		response=r.text
		f = open('out.html','w')
		f.write(response.encode('ascii', 'ignore'))
		f.close()
		return response

if __name__ == '__main__':
	PostQuery()