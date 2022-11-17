#儲存(寫入)檔案:
#把檔案物件放在file變數中，mode為寫入(儲存)/r:閱讀/r+:閱讀加寫入) 
"""file=open("data.txt", mode="w", encoding="utf-8") #開啟 要寫入中文必須打encoding=utf8，英文不用
file.write("hello file\n你好壓") #操作:產生一個檔案 #\n換行
file.close() #關閉 """

#最佳寫法:(不需要寫close，會自動安全關閉檔案)
with open("data.txt", mode="w", encoding="utf-8") as file:
    file.write("5\n3")

#讀取檔案:(讀取已經存在的檔案)
with open("data.txt", mode="r", encoding="utf-8") as file: #改成r
    data=file.read()
print(data)

#把檔案中的數字資料，一行一行的讀取出來，計算總合
sum=0
with open("data.txt", mode="r", encoding="utf-8") as file: #改成r
    for line in file:
        sum+=int(line)
print(sum) 

#使用JSON格式讀取檔案
import json
with open("config.json", mode="r") as file:
    data=json.load(file) #data是個字典資料
print("name: ", data["name"])
print("version: ", data["version"])

#從檔案中讀取JSON資料，修改後放入data裡面
with open("config.json", mode="r") as file:
    data=json.load(file)
print(data)
data["name"]="new name"#修改變數中的資料

with open("config.json", mode="w") as file: #把最新(修改過)資料複寫回檔案中
    json.dump(data,file)










