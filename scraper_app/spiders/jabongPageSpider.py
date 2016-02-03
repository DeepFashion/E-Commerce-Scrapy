from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.loader import XPathItemLoader
from scrapy.contrib.loader.processor import Join, MapCompose
from jabongPageURLs import getURL
from scraper_app.items import JabongPageData
import urllib
from urlparse import urlparse
import json
import re
from lxml import etree
from io import StringIO, BytesIO

class JabongPageSpider(BaseSpider):

    name = "JabongPageBot"
    allowed_domains = ["jabong.com"]
    start_urls=getURL()
    custom_settings={"ITEM_PIPELINES" : ["scraper_app.pipelines.JabongPagePipeline"]}
    
    item_fields = {
        'brand': '//*[@itemprop="brand"]/text()',
        'product-title' : '//*[@class="product-title"]/text()',
        'desc1': '//*[@id="productInfo"]/section/ul/li',
        'desc2_1': '//div/text()',
        'desc2_2': '//div/p/text()',
        'desc2_3': '//div/ul/li/text()'

    }

    def parse(self, response):
        """
        Default callback used by Scrapy to process downloaded responses

        """
        obj=JabongPageData()
        selector = HtmlXPathSelector(text=response.body)
        str1=response.body
        pattern1='<h2 class="prod-disc" itemprop="description">'
        pattern2='</h2>'
        index1=str1.index(pattern1)
        index2=str1.index(pattern2)
        tempRes=str1[index1+45:index2]
        try:
            tempResponse="<div>"+tempRes+"</div>"
            parser = etree.HTMLParser()
            tree   = etree.parse(StringIO(unicode(tempResponse, "utf-8")), parser)
            data=list()
            x=tree.xpath(self.item_fields['desc2_1'])
            for element in x:
                element=element.strip()
                if element:
                    data.append(element)

            x=tree.xpath(self.item_fields['desc2_2'])
            for element in x:
                element=element.strip()
                if element:
                    data.append(element)
            x=tree.xpath(self.item_fields['desc2_3'])
            tdata=""
            for element in x:
                element=element.strip()
                if element:
                    tdata=tdata+element+","
            if tdata:
                tdata=tdata[:-1]
                data.append(tdata)
            obj['desc2']=json.dumps(data)
        except:
            print 'count not get h2 data'
            obj['desc2']=""


        x=selector.xpath(self.item_fields['brand'])
        obj['brand']=x[0].extract()
        x=selector.xpath(self.item_fields['product-title'])
        obj['productTitle']=x[0].extract()
        x=selector.xpath(self.item_fields['desc1'])
        data=dict()
        for element in x:
            key=element.xpath('label/text()').extract()[0]
            val=element.xpath('span/text()').extract()[0]
            data[key]=val
        obj['desc1']=json.dumps(data)
        obj['requestURL']=unicode(response.request.url, "utf-8")
        print obj
        yield obj
