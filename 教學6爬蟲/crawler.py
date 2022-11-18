#抓取PTT電影版的網頁原始碼(HTML)
import urllib.request as req
url="https://www.ptt.cc/bbs/movie/index.html"
#建立一個Request物件，附加Request Headers的資訊:讓網頁端信任讓我們連線
request=req.Request(url, headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36"
}) #記得打user-agent
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")


#解析原始碼，取得每篇文章標題
import bs4 #讓美味湯協助解析HTML格式文件
root=bs4.BeautifulSoup(data,"html.parser") #root代表該網站
titles=root.find_all("div",class_="title") #尋找class="title"的div標籤 #div為網站內的標籤
for title in titles:
    if title.a != None: #如果標題包含a標籤(本文沒有被刪除)，印出來
        print(title.a.string) #string為a標籤後的文字
    