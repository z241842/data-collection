import scrapy
class work3_Item(scrapy.Item):
    name = scrapy.Field()
    price1 = scrapy.Field()
    price2 = scrapy.Field()
    price3 = scrapy.Field()
    price4 = scrapy.Field()
    price5 = scrapy.Field()
    date = scrapy.Field()

class forexSpider(scrapy.Spider):
    name = 'forexSpider'
    # allowed_domains = ['www.boc.cn']
    start_urls = ['https://www.boc.cn/sourcedb/whpj/']

    def parse(self, response):
        data = response.body.decode()
        selector=scrapy.Selector(text=data)
        data_lists = selector.xpath('//table[@align="left"]/tr')
        for data_list in data_lists:
            datas = data_list.xpath('.//td')
            if datas != []:
                item = work3_Item()
                keys = ['name','price1','price2','price3','price4','price5','date']
                str_lists = datas.extract()
                for i in range(len(str_lists)-1):
                    item[keys[i]] = str_lists[i].strip('<td class="pjrq"></td>').strip()
                yield item

