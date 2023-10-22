import pymysql

class StockSpiderPipeline:
    count = 0
    def open_spider(self, spider):
        print("opened")
        try:
            self.con = pymysql.connect(host="127.0.0.1", port=3308, user="root",passwd = "", db = "stock", charset = "utf8")
            self.cursor = self.con.cursor(pymysql.cursors.DictCursor)
            self.cursor.execute("delete from stocks")
            self.opened = True
            self.count = 0
        except Exception as err:
            print(err)
            self.opened = False

    def close_spider(self, spider):
        if self.opened:
            self.con.commit()
            self.con.close()
            self.opened = False
        print("closed")
        print("总共爬取", self.count, "条股票信息")

    def process_item(self, item, spider):
        try:
            self.count = self.count + 1
            print("{:^2}{:>10}{:>10}{:>10}{:>10}{:>12}{:>13}{:>15}{:>12}{:>12}{:>12}{:>12}{:>12}".format(self.count, item['code'], item['name'],
                                                                                 item['new_price'], item['price_limit'],
                                                                                 item['change_amount'],
                                                                                 item['turnover'],
                                                                                 item['volume'], item['rise'],item['highest'],item['lowest'],item['today_open'],item['yesterday_receive']))
            if self.opened:
                self.cursor.execute("insert into stocks (id,bStockNo,bName,bNewPrice,bPriceLimit,bChangeAmount,bTurnover,bVolume,bRise,bHighest,bLowest,bTodayOpen,bYesterdayReceive)values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.count, item['code'], item['name'],item['new_price'], item['price_limit'],item['change_amount'],item['turnover'],item['volume'], item['rise'],item['highest'],item['lowest'],item['today_open'],item['yesterday_receive']))

        except Exception as err:
            print(err)
        return item
