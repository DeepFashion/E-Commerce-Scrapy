from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.loader import XPathItemLoader
from scrapy.contrib.loader.processor import Join, MapCompose
import urllib
from flipkartgetURL import getURL
from urlparse import urlparse
import json

class ImageSpider(BaseSpider):

    name = "ImageFlipkartBot"
    allowed_domains = []
    start_urls=getURL()
    custom_settings={"ITEM_PIPELINES" : ["scraper_app.pipelines.ImagePipeline"]}
    item_fields = {}
    folderName='/home/siddhantmanocha/Projects/flipkartImages/'

    def parse(self, response):
        """
        Default callback used by Scrapy to process downloaded responses

        """
        with open(self.folderName+(response.url).replace('/','_'),'w+') as f:
            f.write(response.body)
        
        obj={}

        print "success"

        yield obj
