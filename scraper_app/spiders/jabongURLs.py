def getURL():
	category="tunics"
	start_urls=list()
	for i in range(1,26):
	    tempUrl="http://www.jabong.com/women/clothing/tunics/?source=topnav_women&ax=1&page="+str(i)+"&limit=100&sortField=popularity&sortBy=desc"
	    start_urls.append(tempUrl)
	return start_urls,category
