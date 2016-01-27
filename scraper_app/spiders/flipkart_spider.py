from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.loader import XPathItemLoader
from scrapy.contrib.loader.processor import Join, MapCompose
from flipkartURLs import getURL
from scraper_app.items import flipkartData

class FlipkartSpider(BaseSpider):

    name = "FlipkartBot"
    allowed_domains = ["flipkart.com"]
    start_urls=getURL()
    
    deals_list_xpath = '//div[@class="lifestyle-grid"]/div[@class="browse-grid-row"]/div[@class="unit size1of3"]/div'
    item_fields = {
        'images': 'div[1]/a[1]/@data-images',
        'mainImage':  'div[1]/a[1]/img[1]/@data-src',
        'apparelURL': 'div[1]/a[1]/@href',
        'title': 'div[2]/div[1]/a/@title',
        'rating': 'div[2]/div[2]/div[1]/@title',
        'finalPrice': 'div[2]/div[3]/div[1]/span/text()', 
        'initialPrice': 'div[2]/div[3]/div[2]/span[1]/text()',
        'discount': 'div[2]/div[3]/div[2]/span[2]/text()'
    }

    def parse(self, response):
        """
        Default callback used by Scrapy to process downloaded responses

        """
        selector = HtmlXPathSelector(response)

        # iterate over deals
        for deal in selector.select(self.deals_list_xpath):
            loader = XPathItemLoader(flipkartData(), selector=deal)

            # define processors
            loader.default_input_processor = MapCompose(unicode.strip)
            loader.default_output_processor = Join()

            # iterate over fields and add xpaths to the loader
            for field, xpath in self.item_fields.iteritems():
                loader.add_xpath(field, xpath)
            yield loader.load_item()