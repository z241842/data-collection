import urllib.request
import re
import json
import pandas as pd
import pathlib
import openpyxl

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                 '(KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.47'
}

def getdata(data_ls,count_ls):
    count = 1
    for i in range(1,6):
        page_num = i
        url = ('http://25.push2.eastmoney.com/api/qt/clist/get?cb=jQuery11240213'
               '13927342030325_1696658971596&pn=%d&pz=20&po=1&np=1&ut=bd1d9ddb040'
               '89700cf9c27f6f7426281&fltt=2&invt=2&wbp2u=|0|0|0|web&fid=f3&fs=m:0'
               '+t:6,m:0+t:80,m:1+t:2,m:1+t:23,m:0+t:81+s:2048&fields=f2,f3,f4,f5,f6,f7,f12,f14,f15,f16,f17,f18&_=1696658971636')
        url = url % page_num

        req = urllib.request.Request(url=url,headers=headers)

        data = urllib.request.urlopen(req).read().decode()

        data = re.compile('"diff":\[(.*?)\]',re.S).findall(data)

        for one_data in re.compile('\{(.*?)\}',re.S).findall(data[0]):
            data_dic = json.loads('{' + one_data + '}')
            data_ls.append(data_dic)
            count_ls.append(count)
            count += 1

    return data_ls, count_ls


if __name__ == "__main__":
    columns={'f2':'最新价','f3':'涨跌幅(%)','f4':'涨跌额','f5':'成交量','f6':'成交额','f7':'振幅(%)','f12':'代码','f14':'名称',
             'f15':'最高','f16':'最低','f17':'今开','f18':'昨收'}
    data_ls=[]
    count_ls=[]
    getdata(data_ls, count_ls)
    num = pd.DataFrame(count_ls)
    # print(num)
    df = pd.DataFrame(data_ls)
    df.rename(columns=columns,inplace=True)
    df.insert(0,column='序号',value=num)
    df.to_excel('./stock.xlsx',index=False)

