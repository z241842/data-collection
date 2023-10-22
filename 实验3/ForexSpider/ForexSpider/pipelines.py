class ForexSpiderPipeline:
    count = 0

class ForexSpiderPipeline:

    def open_spider(self, spider):
        print('%-10s%-10s%-10s%-10s%-10s%-10s%-10s' % (
        '货币名称', '现汇买入价', '现钞买入价', '现汇卖出价', '现钞卖出价', '中行折算价', '发布日期'))

    def process_item(self, item, spider):
        print('%-10s%-10s%-10s%-10s%-10s%-10s%-10s' % (
        item['name'], item['price1'], item['price2'], item['price3'], item['price4'], item['price5'], item['date']))
        return item