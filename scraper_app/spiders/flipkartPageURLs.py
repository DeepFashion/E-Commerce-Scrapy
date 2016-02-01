import urllib

def getURLSimple():
	start_urls=list()	
	start_urls.append('http://www.flipkart.com/wrangler-women-s-solid-casual-shirt/p/itme8q4gjgqg42xc?pid=SHTE8Q4G5XQGF9SQ&al=ThsGnZDjLFHQALPQjf3S7MldugMWZuE7eGHgUTGjVrq34siOYkRdcylI1wIgMoStWjqoPwBrylw%3D&ref=L%3A145924790153660934&srno=b_8')
	start_urls.append('http://www.flipkart.com/hbhwear-solid-women-s-polo-neck-t-shirt/p/itme4g769excshzj?pid=TSHE4G76CXHXU456&al=ThsGnZDjLFEZTQtAEV05F8ldugMWZuE7wkNiXfq8GiR%2FMBq1PENgcSTIaBkyV9pqxSpxi8SNpDQ%3D&ref=L%3A145924790153660934&srno=b_14')
	start_urls.append('http://www.flipkart.com/hbhwear-solid-women-s-polo-neck-t-shirt/p/itme4g76ystz3jjh?pid=TSHE4G76ZFNBKZ6C&icmpid=reco_pp_personalhistoryFooter_womenclothing_na_5')
	return start_urls

def getURL():
	return getURLSimple()

if __name__ == '__main__':
	print getURL()

