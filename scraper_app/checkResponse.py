import json
import yaml
import urllib,requests
import ast
def PostQuery(operator='plus',operand1='2',operand2='3'):
		myURL = "http://www.flipkart.com/shaurya-enterprise-embroidered-kurta-churidar/p/itmeak7ewkjwqq9z?pid=SWDEAK7ERRCRSYTY&icmpid=reco_pp_personalhistoryFooter_womenclothing_na_1"
		r = requests.get(myURL)
		response=r.text
		f = open('out.html','w')
		f.write(response.encode('ascii', 'ignore'))
		f.close()
		return response

if __name__ == '__main__':
	PostQuery()