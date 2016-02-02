from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.loader import XPathItemLoader
from scrapy.contrib.loader.processor import Join, MapCompose
from jabongPageURLs import getURL
from scraper_app.items import JabongPageData
import urllib
from urlparse import urlparse
import json

class JabongPageSpider(BaseSpider):

    name = "JabongPageBot"
    allowed_domains = ["jabong.com"]
    start_urls=getURL()
    custom_settings={"ITEM_PIPELINES" : ["scraper_app.pipelines.JabongPagePipeline"]}
    
    item_fields = {
        'brand': '//*[@itemprop="brand"]/text()',
        'product-title' : '//*[@class="product-title"]/text()',
        'desc1': '//*[@id="productInfo"]/section/ul/li',
        'desc2': '//*[@class="prod-disc"]/p/text()'
    }

    def parse(self, response):
        """
        Default callback used by Scrapy to process downloaded responses

        """
        with open('f1','w+') as f:
            f.write(response.body)
        obj=JabongPageData()
        
        selector = HtmlXPathSelector(text=response.body)
        x=selector.select(self.item_fields['brand'])
        obj['brand']=x[0].extract()
        x=selector.select(self.item_fields['product-title'])
        obj['productTitle']=x[0].extract()
        x=selector.select(self.item_fields['desc1'])
        data=dict()
        for element in x:
            key=element.select('label/text()').extract()[0]
            val=element.select('span/text()').extract()[0]
            data[key]=val

        x=selector.select(self.item_fields['desc2'])
        print "####################"
        print x
        print x.extract()
        print "####################"

        # for element in x:
        #     res1=element.select('text()')
        #     for res in res1:
        #         print res

        #     res1=element.select('p/text()')
        #     for res in res1:
        #         print "####################"
        #         print res
        #         print "####################"

        #     y=element.select('ul/li/text()')
        #     for listElement in y:
        #         print listElement.extract()


        
        obj['desc1']=json.dumps(data)
        if len(x.extract()) > 0:
            obj['desc2']= x.extract()[0]
        else:
            obj['desc2']=""

        obj['requestURL']=unicode(response.request.url, "utf-8")

        print obj
        # =json.dumps(keyFeaturesList)
        # obj['specs']=json.dumps(tablesExtracted)
        # obj['rating']=json.dumps(ratingExtracted)
        # obj['descriptionText']=json.dumps(descriptionText)
        # obj["requestURL"]=unicode(response.request.url, "utf-8")
        # print obj
        yield obj
