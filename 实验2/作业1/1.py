from bs4 import BeautifulSoup
from bs4.dammit import UnicodeDammit
import urllib.request
import sqlite3


# 天气数据库
class WeatherDB:
    def __init__(self):
        self.cursor = None
        self.con = None

    def openDB(self):
        self.con = sqlite3.connect("weathers.db")
        self.cursor = self.con.cursor()
        try:
            self.cursor.execute(
                "create table weathers (wCity varchar(16),"
                "wDate varchar(16),"
                "wWeather varchar(64),"
                "wTemp varchar(32),"
                "constraint pk_weather primary key (wCity,wDate))")
        except Exception as err:
            print(err)
            self.cursor.execute("delete from weathers")

    def closeDB(self):
        self.con.commit()
        self.con.close()

    def insert(self, city, date, weather, temp):
        try:
            self.cursor.execute("insert into weathers (wCity,wDate,wWeather,wTemp) values (?,?,?,?)",
                                (city, date, weather, temp))
        except Exception as err:
            print(err)

    def show(self):
        self.cursor.execute("select * from weathers")
        rows = self.cursor.fetchall()
        print("%-16s%-16s%-32s%-16s" % ("city", "date", "weather", "temp"))
        for row in rows:
            print("%-16s%-16s%-32s%-16s" % (row[0], row[1], row[2], row[3]))


# 天气预报
class WeatherForecast:
    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 6.0 x64; en-US; rv:1.9pre) "
                          "Gecko/2008072421 Minefield/3.0.2pre"}
        self.cityCode = {"北京": "101010100", "上海": "101020100", "广州": "101280101", "深圳": "101280601"}

    def forecastCity(self, city):
        if city not in self.cityCode.keys():
            print(city + " 找不到代码")
            return
        url = "http://www.weather.com.cn/weather/" + self.cityCode[city] + ".shtml"
        try:
            req = urllib.request.Request(url, headers=self.headers)
            data = urllib.request.urlopen(req)
            data = data.read()
            dammit = UnicodeDammit(data, ["utf-8", "gbk"])
            data = dammit.unicode_markup
            soup = BeautifulSoup(data, "lxml")
            lis = soup.select("ul[class='t clearfix'] li")
            x = 0
            row = 1
            for li in lis:
                try:
                    date = li.select('h1')[0].text
                    weather = li.select('p[class="wea"]')[0].text
                    if x == 0:  # 为今天只有一个温度做判断 <i>14℃</i>
                        x += 1
                        temp = li.select('p[class="tem"] i')[0].text
                    else:
                        temp = li.select('p[class="tem"] span')[0].text + "/" + li.select('p[class="tem"] i')[0].text
                    print("{:<5}\t{:<4}\t{:<9}\t{:<12}\t{:<6}\t".format(row, city, date, weather, temp))
                    row = row+1
                    self.db.insert(city, date, weather, temp)
                except Exception as err:
                    print(err)
        except Exception as err:
            print(err)

    def process(self, cities):
        self.db = WeatherDB()
        self.db.openDB()

        for city in cities:
            self.forecastCity(city)

        # self.db.show()
        self.db.closeDB()


ws = WeatherForecast()
ws.process(["北京", "上海", "广州", "深圳"])