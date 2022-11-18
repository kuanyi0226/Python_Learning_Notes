#抓取Medium.com的文章資料
import urllib.request as req
url="https://medium.com/_/graphql"
request=req.Request(url, headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36"
}) 
with req.urlopen(request) as response:
    data=response.read().decode("utf-8") #根據觀察，取得的資料為JSON格式(不用美味湯)

#解析JSON格式的資料，取得每篇標題
import json
data=json.loads(data) #把原始資料解析成字典/列表的表示形式
print(data)



