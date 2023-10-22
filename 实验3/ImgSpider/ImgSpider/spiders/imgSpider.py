import scrapy
import re
class ImgSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    # title_ = scrapy.Field()
    image_url = scrapy.Field()
    pass
class imgSpider(scrapy.Spider):
    name = "imgSpider"

    start_url = "http://www.weather.com.cn"
    total = 0

    def start_requests(self):
        yield scrapy.Request(self.start_url, callback=self.parse)

    # def picParse(self, response):
    def parse(self, response):
        imgList = re.findall(r'<img.*?src="(.*?)"', response.text, re.S)
        # print(imgList)
        for k in imgList:
            # print(self.total)
            print(k)
            if self.total > 102:
                return
            item = ImgSpiderItem()
            item['image_url'] = k
            item['name'] = self.total
            self.total += 1
            yield item
