from scrapy.item import Item, Field
class LivingSocialDeal(Item):
    """Livingsocial container (dictionary-like object) for scraped data"""
    images = Field()
    mainImage = Field() 
    apparelURL = Field()
    title = Field()
    rating = Field()
    finalPrice = Field()
    initialPrice = Field()
    discount = Field()