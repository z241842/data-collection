import urllib.request
from bs4 import BeautifulSoup
import re
import urllib.parse

headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.81"}
url="https://search.jd.com/Search?keyword=%E4%B9%A6%E5%8C%85&enc=utf-8&wq=shu&pvid=ea9bef8ed6114b1a9106f35315b8bf24"

req=urllib.request.Request(url,headers=headers)  # Request可以加url
html=urllib.request.urlopen(req)
html=html.read()
html=html.decode()

def bagcrawl():
    soup = BeautifulSoup(html, "html.parser")
    i=0
    lis=soup.find_all("li",{"data-sku": re.compile("\d+")})
    print("序号        商品名称                        价格")
    for li in lis:
        price1=li.find("div",attrs={"class":"p-price"}).find("strong").find("i")
        price = price1.text
        name1=li.find("div",attrs={"class":"p-name"}).find("a").find("em")
        name=name1.text.strip()
        i=i+1
        t='\t'
        print(i,t,name,t,price)


if __name__ == '__main__':
    bagcrawl()





