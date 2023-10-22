import scrapy

class StockItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    code = scrapy.Field()
    name = scrapy.Field()
    new_price = scrapy.Field()
    price_limit = scrapy.Field()
    change_amount = scrapy.Field()
    turnover = scrapy.Field()
    volume = scrapy.Field()
    rise = scrapy.Field()
    highest = scrapy.Field()  # 最高
    lowest = scrapy.Field()  # 最低
    today_open = scrapy.Field()  # 今开
    yesterday_receive = scrapy.Field()  # 昨收
    pass
