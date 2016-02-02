from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.loader import XPathItemLoader
from scrapy.contrib.loader.processor import Join, MapCompose
from flipkartPageURLs import getURL
from scraper_app.items import FlipkartPageData
import urllib
from urlparse import urlparse
import json

class FlipkartPageSpider(BaseSpider):

    name = "FlipkartPageBot"
    allowed_domains = ["flipkart.com"]
    start_urls=getURL()
    custom_settings={"ITEM_PIPELINES" : ["scraper_app.pipelines.FlipkartPagePipeline"]}
    
    item_fields = {
        'keyFeatures': '//*[@class="keyFeatures specSection"]/ul',
        'specs' : '//*[@class="productSpecs specSection"]/table[@class="specTable"]',
        'rating': '//*[@class="ratingsDistribution"]/li',
        'descriptionText': '//*[@class="description specSection"]/div[@class="description-text"]/text()'
    }
# 'specs':  '//*[@id="fk-mainbody-id"]/div/div/div/div[@class="productSpecs specSection"]/table[@class="specTable"]',
    # //*[@id="fk-mainbody-id"]/div/div/div/div[@class="productSpecs specSection"]

    def parse(self, response):
        """
        Default callback used by Scrapy to process downloaded responses

        """
        # with open('f1','w+') as f:
        #     f.write(response.body)
        
        selector = HtmlXPathSelector(response)
        x=selector.select(self.item_fields['keyFeatures'])
        # print x.extract()
        y=x.select('li/text()')
        # print x.extract()
        # print y.extract()
        keyFeaturesList=list()
        tablesExtracted=dict()
        ratingExtracted=dict()
        descriptionText=list()
        for element in y:
            keyFeaturesList.append(element.extract())

        tables=selector.select(self.item_fields['specs'])
        for table in tables:
            entries=table.select('tr/th/text()')
            tableName=entries.extract()[0]
            tableEntry=dict()
            keys=table.select('tr/td[@class="specsKey"]/text()').extract()
            values=table.select('tr/td[@class="specsValue"]/text()').extract()
            for i in range(len(values)):
                try:
                    tableEntry[keys[i].strip()]=values[i].strip()
                except:
                    try:
                        tableEntry[i]=values[i].strip()
                    except:
                        break
            tablesExtracted[tableName]=tableEntry



        x=selector.select(self.item_fields['rating'])
        for element in x:
            ratingExtracted[element.select('a/span/text()').extract()[0]]=element.select('a/div/div/text()').extract()[0]
        
        x=selector.select(self.item_fields['descriptionText'])
        for element in x:
            descriptionText.append(element.extract())

        obj=FlipkartPageData()
        obj['keyFeatures']=json.dumps(keyFeaturesList)
        obj['specs']=json.dumps(tablesExtracted)
        obj['rating']=json.dumps(ratingExtracted)
        obj['descriptionText']=json.dumps(descriptionText)
        obj["requestURL"]=unicode(response.request.url, "utf-8")
        # print obj
        yield obj
