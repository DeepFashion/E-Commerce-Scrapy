import json
import yaml
import urllib,requests
import ast
def PostQuery(url):
		myURL = url
		r = requests.get(myURL)
		return r.text

if __name__ == '__main__':
	url="http://www.jabong.com/women/clothing/tops-tees-shirts/?source=topnav_women&ax=1&page=44&limit=100&sortField=popularity&sortBy=desc"
	PostQuery(url)