from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.loader import XPathItemLoader
from scrapy.contrib.loader.processor import Join, MapCompose
import getResponse
from scrapy.item import Item, Field
from  scrapy.http import *
from flip import *
import json

class testData(Item):
    keyFeatures = Field()
    specs = Field() 
    rating = Field()
    descriptionText=Field()

def test():
    responseText=responseTextflipkart
    item_fields = {
        'keyFeatures': '//*[@id="fk-mainbody-id"]/div/div/div/div[@class="keyFeatures specSection"]/ul ',
        'specs':  '//*[@id="fk-mainbody-id"]/div/div/div/div[@class="productSpecs specSection"]/table[@class="specTable"]',
        'rating': '//*[@id="fk-mainbody-id"]/div/div/div/div/div/div/div/div/ul[@class="ratingsDistribution"]/li',
        'descriptionText': '//*[@id="fk-mainbody-id"]/div/div/div/div[@class="description specSection"]/div[@class="description-text"]/text()'
    }

    selector = HtmlXPathSelector(text=responseText)
    x=selector.select(item_fields['keyFeatures'])
    y=x.select('li/text()')
    keyFeaturesList=list()
    tablesExtracted=dict()
    ratingExtracted=dict()
    descriptionText=list()
    for element in y:
        keyFeaturesList.append(element.extract())

    x=selector.select(item_fields['specs'])
    tables=x.select('tbody')
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



    x=selector.select(item_fields['rating'])
    for element in x:
        ratingExtracted[element.select('a/span/text()').extract()[0]]=element.select('a/div/div/text()').extract()[0]
    
    x=selector.select(item_fields['descriptionText'])
    for element in x:
        descriptionText.append(element.extract())

    obj=testData()
    obj['keyFeatures']=json.dumps(keyFeaturesList)
    obj['specs']=json.dumps(tablesExtracted)
    obj['rating']=json.dumps(ratingExtracted)
    obj['descriptionText']=json.dumps(descriptionText)
    
    print obj


    # load to dict:

    # my_dict = json.loads(input)







    
    # print y[0].select('text()').extract()
    # y=x.select('li/text()')
    # print "keyFeatures"
    # for element in y:
    #     print element.extract()

    # print selector.data
    # print selector.select(item_fields['keyFeatures']).extract()
    # for deal in selector.select(self.deals_list_xpath):
    #     loader = XPathItemLoader(testData(), selector=deal)

    #     # define processors
    #     # loader.default_input_processor = MapCompose(unicode.strip)
    #     # loader.default_output_processor = Join()

    #     # iterate over fields and add xpaths to the loader
    #     for field, xpath in self.item_fields.iteritems():
    #         loader.add_xpath(field, xpath)

    #     print loader.load_item()

test()
