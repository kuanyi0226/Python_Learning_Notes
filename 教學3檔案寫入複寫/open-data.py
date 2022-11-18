#網路連線
"""import urllib.request as request #縮寫
src="https://www.ntu.edu.tw/" #台大網址
with request.urlopen(src) as response: #嘗試連到台大網站
     data=response.read().decode("utf-8") #讀取網站原始碼(HTML、CSS、JS) #讓亂碼變中文字
print(data) """

#串接、擷取公開資料:尋找open data的"API"
import urllib.request as request
import json #因為open data是json格式
src="https://data.taipei/api/v1/dataset/296acfa2-5d93-4706-ad58-e83cc951863c?scope=resourceAquire"
with request.urlopen(src) as response:
    data=json.load(response) #利用json模組處理json資料格式
print(data)

#將公司名稱列表出來到檔案中(擷取)
clist=data["result"]["results"]
with open("data2.txt","w",encoding="utf-8") as file:
    for company in clist: #迴圈在with內，把資料一個一個抓出來
        file.write(company["公司名稱"]+"\n") #以上為字典列表，公司名稱是key，xxx公司是value

