from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.loader import XPathItemLoader
from scrapy.contrib.loader.processor import Join, MapCompose
from polyvoreURLs import getURL
from scraper_app.items import PolyvoreData


class PolyvoreSpider(BaseSpider):
    """Spider for Polyvore Website; Ladies collection: shirts, tees, etc"""
    name = "PolyvoreBot"
    allowed_domains = ["polyvore.com"]
    start_urls=getURL()

    products_list_xpath = '//*[@id="body"]'
    item_fields = {
        'name' : '//*[@id="set_editor"]/h1/text()',
        'numlikes': '//*[@id="right"]/ul[1]/li/span/span/span/text()'
    }

    def parse(self, response):
        """
        Default callback used by Scrapy to process downloaded responses

        """

        selector = HtmlXPathSelector(response)

        # iterate over deals
        for deal in selector.select(self.products_list_xpath):
            loader = XPathItemLoader(PolyvoreData(), selector=deal)

            # define processors
            loader.default_input_processor = MapCompose(unicode.strip)
            loader.default_output_processor = Join()

            # iterate over fields and add xpaths to the loader
            for field, xpath in self.item_fields.iteritems():
                loader.add_xpath(field, xpath)
            yield loader.load_item()
