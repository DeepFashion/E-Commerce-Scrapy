from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.loader import XPathItemLoader
from scrapy.contrib.loader.processor import Join, MapCompose

from scraper_app.items import LivingSocialDeal

class LivingSocialSpider(BaseSpider):
    """Spider for regularly updated livingsocial.com site, San Francisco Page"""
    name = "livingsocial"
    allowed_domains = ["flipkart.com"]
    start_urls=list()
    for i in range(120):
        tempUrl="http://www.flipkart.com/lc/pr/pv1/spotList1/spot1/productList?sid=2oq%2Cs9b%2Cmg4%2Cvg6&pincode=208016&filterNone=true&start="+str(15*i+1)+"&q=shirts&ajax=true&_=1453307533668"
        start_urls.append(tempUrl)
    deals_list_xpath = '//div[@class="lifestyle-grid"]/div[@class="browse-grid-row"]/div[@class="unit size1of3"]/div'
    item_fields = {
        'images': 'div[1]/a[1]/@data-images',
        'mainImage':  'div[1]/a[1]/img[1]/@data-src',
        'apparelURL': 'div[1]/a[1]/@href',
        'title': 'div[2]/div[1]/a/@title',
        'rating': 'div[2]/div[2]/div[1]/+@title',
        'finalPrice': 'div[2]/div[3]/div[1]/span/text()', 
        'initialPrice': 'div[2]/div[3]/div[2]/span[1]/text()',
        'discount': 'div[2]/div[3]/div[2]/span[2]/text()'
    }

    def parse(self, response):
        """
        Default callback used by Scrapy to process downloaded responses

        Testing contracts:
        @url http://www.livingsocial.com/cities/15-san-francisco
        @returns items 1
        @scrapes title link

        """
        selector = HtmlXPathSelector(response)

        # iterate over deals
        for deal in selector.select(self.deals_list_xpath):
            loader = XPathItemLoader(LivingSocialDeal(), selector=deal)

            # define processors
            loader.default_input_processor = MapCompose(unicode.strip)
            loader.default_output_processor = Join()

            # iterate over fields and add xpaths to the loader
            for field, xpath in self.item_fields.iteritems():
                loader.add_xpath(field, xpath)
            yield loader.load_item()