from scrapy.item import Item, Field
class flipkartData(Item):
    """flipkartData container (dictionary-like object) for scraped data"""
    images = Field()
    mainImage = Field() 
    apparelURL = Field()
    title = Field()
    rating = Field()
    finalPrice = Field()
    initialPrice = Field()
    discount = Field()
    requestURL = Field()

class JabongData(Item):
    product_link= Field()
    image_320 =Field()
    image_500 =Field()
    image_768 =Field()
    image_1024 =Field()
    image_1280 =Field()
    name =Field()
    brand=Field()
    previous_price =Field()
    standard_price =Field()
    discount =Field()
    requestURL = Field()

class PolyvoreData(Item):
    name= Field()
    numlikes=Field()
    requestURL = Field()
    
