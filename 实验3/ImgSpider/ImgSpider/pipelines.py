from itemadapter import ItemAdapter
from scrapy.pipelines.images import ImagesPipeline
import scrapy

images_store = "C:\\Users\\zmk\\PycharmProjects\\pythonProject\\ImgSpider\\images\\"
class ImgSpiderPipeline(ImagesPipeline):

    def file_path(self, request, response=None, info=None, *, item=None):
        file_name = item['image_url'].split('/')[-1]
        print(file_name)
        return images_store + '/' + file_name

    def get_media_requests(self, item, info):
        url = item['image_url']
        print(url)
        yield scrapy.Request(url)

    def item_completed(self, results, item, info):
        return item
