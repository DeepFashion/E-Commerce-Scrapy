import json
import yaml
import urllib,requests
import ast
def PostQuery(operator='plus',operand1='2',operand2='3'):
		myURL = "http://www.flipkart.com/lc/pr/pv1/spotList1/spot1/productList?sid=2oq%2Cs9b%2Cmg4%2Cvg6&pincode=208016&filterNone=true&start=76&q=shirts&ajax=true&_=1453307533668"
		r = requests.get(myURL)
		response=r.text
		# response=yaml.safe_load(r.text)
		return response

if __name__ == '__main__':
	print PostQuery()