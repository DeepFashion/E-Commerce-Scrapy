import urllib

def getURLBrands():
	brandnames=list()
	with open('flipkartBrandList') as f:
		brandnames=f.readlines()
	for i in range(len(brandnames)):
		brandnames[i]=brandnames[i].strip()

	start_urls=list()
	for j in range(len(brandnames)):	
		for i in range(99):
			tempUrl="http://www.flipkart.com/lc/pr/pv1/spotList1/spot1/productList?p%5B%5D=facets.brand%255B%255D%3D"+urllib.quote(brandnames[j])+"&sid=2oq%2Cc1r%2Cha6%2Ccck&pincode=560034&filterNone=true&start="+str(15*i+1)+"&ajax=true&_=1453926601673"
			start_urls.append(tempUrl)
	return start_urls
	
def getURLSimple():
	start_urls=list()	
	for i in range(120):
		tempUrl="http://www.flipkart.com/lc/pr/pv1/spotList1/spot1/productList?sid=2oq%2Cs9b%2Cmg4%2Cvg6&pincode=208016&filterNone=true&start="+str(15*i+1)+"&q=shirts&ajax=true&_=1453307533668"
		start_urls.append(tempUrl)
	return start_urls

def getURL():
	category="shirts-tops-tunics"
	return getURLBrands(),category

if __name__ == '__main__':
	print getURL()

