from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.loader import XPathItemLoader
from scrapy.contrib.loader.processor import Join, MapCompose

from scraper_app.items import JabongData


class JabongSpider(BaseSpider):
    """Spider for Jabong Website; Ladies collection: shirts, tees, etc"""
    name = "jabongSpiderLadiesShirtsTees"
    allowed_domains = ["jabong.com"]
    start_urls=list()
    for i in range(1,120):
        tempUrl="http://www.jabong.com/women/clothing/tops-tees-shirts/?source=topnav_women&ax=1&page="+str(i)+"&limit=100&sortField=popularity&sortBy=desc"
        start_urls.append(tempUrl)

    products_list_xpath = '//*[@id="catalog-product"]/section[2]/div'
    item_fields = {
        'product_link': 'a/@href',
        'image_320' : 'a/figure/img/@data-src-320',
        'image_500' : 'a/figure/img/@data-src-500',
        'image_768' : 'a/figure/img/@data-src-768',
        'image_1024' : 'a/figure/img/@data-src-1024',
        'image_1280' : 'a/figure/img/@data-src-1280',
        'brand' : 'a/div/div[1]/text()',
        'name': 'a/div/div[1]/span[1]/text()',
        'previous_price': 'a/div/div[2]/span[1]/span/text()',
        'standard_price': 'a/div/div[2]/span[2]/text()',
        'discount': 'a/div/div[2]/span[3]/text()'
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
        for deal in selector.select(self.products_list_xpath):
            loader = XPathItemLoader(JabongData(), selector=deal)

            # define processors
            loader.default_input_processor = MapCompose(unicode.strip)
            loader.default_output_processor = Join()

            # iterate over fields and add xpaths to the loader
            for field, xpath in self.item_fields.iteritems():
                loader.add_xpath(field, xpath)
            yield loader.load_item()
