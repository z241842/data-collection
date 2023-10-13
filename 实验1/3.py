import requests
from bs4 import BeautifulSoup as bs
import re

url = "https://xcb.fzu.edu.cn/info/1071/4504.htm"


def GetHtml(url):
    session = requests.session()
    response = session.get(url)
    return response

def GetImages():
    baseUrl = "https://xcb.fzu.edu.cn"
    Dir = "C:\\Users\\zmk\\PycharmProjects\\pythonProject\\数据采集\\实验1\\images\\"
    with open("3.html", "r", encoding="utf-8") as file:
        soup = bs(file, "lxml")
    cores = soup.select("p.vsbcontent_img > img")
    for i in range(0, len(cores)):
        core = cores[i]
        url = baseUrl + core['src']
        image = GetHtml(url)
        fileName = Dir + "{}.jpeg".format(i+1)
        with open(fileName, 'wb') as fi:
            fi.write(image.content)
            print("{}.jpeg 爬取成功！".format(i+1))

if __name__ == "__main__":
    html = GetHtml(url).text
    GetImages()



