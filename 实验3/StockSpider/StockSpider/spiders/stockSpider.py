import json
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
class stockSpider(scrapy.Spider):
    name = 'stockSpider'
    page = 1
    start_urls = [
        'http://69.push2.eastmoney.com/api/qt/clist/get?cb=jQuery11240821834413285744_1602921989373&pn=' + str
        (page) + '&pz=20&po=1&np=1&ut=bd1d9ddb04089700cf9c27f6f7426281&fltt=2&invt=2&fid=f3&fs=m:0+t:6,m:0+t:13,'
                      'm:0+t:80,m:1+t:2,m:1+t:23&fields=f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f12,f13,f14,f15,f16,f17,f18,f20,'
                      'f21,f23,f24,f25,f22,f11,f62,f128,f136,f115,f152&_=1602921989374']

    def parse(self, response):
        try:
            data = response.body.decode('utf-8')
            data = data[41:-2]  # 将获取到的json文件字符串去掉前面的jQuery.....一大串东西，截取为标准的json格式，传入处理
            responseJson = json.loads(data)
            stocks = responseJson.get('data').get('diff')
            for stock in stocks:
                item = StockItem()
                item['code'] = stock.get('f12')
                item['name'] = stock.get('f14')
                item['new_price'] = stock.get('f2')
                item['price_limit'] = stock.get('f3')
                item['change_amount'] = stock.get('f4')
                item['turnover'] = stock.get('f5')
                item['volume'] = stock.get('f6')
                item['rise'] = stock.get('f7')
                item['highest'] = stock.get('f15')
                item['lowest'] = stock.get('f16')
                item['today_open'] = stock.get('f17')
                item['yesterday_receive'] = stock.get('f18')
                yield item

            url = response.url.replace("pn=" + str(self.page), "pn=" + str(self.page + 1))   # 实现翻页
            self.page = self.page + 1
            yield scrapy.Request(url=url, callback=self.parse)
        except Exception as err:
            print(err)

