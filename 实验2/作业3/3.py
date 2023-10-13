import requests
import pandas as pd
import re

url = "https://www.shanghairanking.cn/_nuxt/static/1695811954/rankings/bcur/2021/payload.js"

resquest = requests.get(url=url)
#获取学校名称
name_grep = ',univNameCn:"(.*?)",'
name = re.findall(name_grep,resquest.text)
#获取学校总分
score_grep = ',score:(.*?),'
score = re.findall(score_grep,resquest.text)
#获取学校类型
category_grep = ',univCategory:(.*?),'
category = re.findall(category_grep,resquest.text)
#获取学校所在省份
province_grep = ',province:(.*?),'
province = re.findall(province_grep,resquest.text)

code_name_grep = 'function(.*?){'
code_name = re.findall(code_name_grep,resquest.text)
start_code = code_name[0].find('a')
end_code = code_name[0].find('pE')
code_name = code_name[0][start_code:end_code].split(',')#将function中的参数取出并存在code_name列表中

value_name_grep ='mutations:(.*?);'
value_name = re.findall(value_name_grep,resquest.text)
start_value = value_name[0].find('(')
end_value = value_name[0].find(')')
value_name = value_name[0][start_value+1:end_value].split(",") #将参数所对应的含义取出存在value_name列表中

df = pd.DataFrame(columns=["排名","学校","省份","类型","总分"])
for i in range(len(name)):
    province_name = value_name[code_name.index(province[i])][1:-1]
    category_name = value_name[code_name.index(category[i])][1:-1]
    df.loc[i] = [i+1,name[i],province_name,category_name,score[i]]
print(df)
df.to_excel("./rank.xlsx")