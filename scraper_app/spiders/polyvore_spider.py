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
    start_urls=getURL()[:1]

    custom_settings={"ITEM_PIPELINES" : ["scraper_app.pipelines.PolyvorePipeline"]}

    products_list_xpath = '//*[@id="body"]'
    item_fields = {
        'name' : '//*[@id="set_editor"]/h1/text()',
        'numlikes': '//*[@id="right"]/ul[1]/li/span/span/span/text()'
    }

    item_items = {
        'productName' : 'div/div[1]/a/img/@title',
        'productURL' : 'div/div[1]/a/@href',
        'productPrice' : 'div/div[2]/div[2]/span/text()',
        'productImage' : 'div/div[1]/a/img/@src',
        'productNumLikes' : 'div/div[2]/div[3]/ul/li/span/span/span/text()'
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

            # adding the request URL to the loader 
            loader.add_value("requestURL",unicode(response.request.url, "utf-8"))


            for item in deal.xpath('//*[@id="content"]/ul[1]/li'):
                ll = XPathItemLoader(PolyvoreData(), selector=item)
                # define processors
                ll.default_input_processor = MapCompose(unicode.strip)
                ll.default_output_processor = Join()

                for field, xpath in self.item_items.iteritems():
                    ll.add_xpath(field, xpath)

                ll.add_value("requestURL", loader.load_item()['requestURL'])
                ll.add_value("name", loader.load_item()['name'])
                ll.add_value("numlikes", loader.load_item()['numlikes'])
                yield ll.load_item()

            for item in deal.xpath('//*[@id="content"]/ul[2]/li'):
                ll = XPathItemLoader(PolyvoreData(), selector=item)
                # define processors
                ll.default_input_processor = MapCompose(unicode.strip)
                ll.default_output_processor = Join()

                for field, xpath in self.item_items.iteritems():
                    ll.add_xpath(field, xpath)

                ll.add_value("requestURL", loader.load_item()['requestURL'])
                ll.add_value("name", loader.load_item()['name'])
                ll.add_value("numlikes", loader.load_item()['numlikes'])
                yield ll.load_item()
