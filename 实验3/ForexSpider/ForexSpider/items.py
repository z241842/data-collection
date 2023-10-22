import scrapy


class work3_Item(scrapy.Item):
    name = scrapy.Field()
    price1 = scrapy.Field()
    price2 = scrapy.Field()
    price3 = scrapy.Field()
    price4 = scrapy.Field()
    price5 = scrapy.Field()
    date = scrapy.Field()

