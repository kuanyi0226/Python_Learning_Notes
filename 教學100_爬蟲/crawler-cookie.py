#抓取PTT八卦版的網頁原始碼(HTML)
import urllib.request as req
def getdata(url):
    request=req.Request(url, headers={
        "cookie":"over18=1", #因為八卦版有18禁確認的畫面阻擋我們直接連接網站，故多這一條code告訴網站我們已經按過18禁確認了
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36"
    })
    with req.urlopen(request) as response:
        data=response.read().decode("utf-8")


    #解析原始碼，取得每篇文章標題
    import bs4 
    root=bs4.BeautifulSoup(data,"html.parser") 
    titles=root.find_all("div",class_="title") #找標題
    for title in titles:
        if title.a != None:  #如果有a標籤就印出來
            print(title.a.string) 

    #找下一頁的超連結
    nextlink=root.find(("a"),string="‹ 上頁") #找到內文是‹ 上頁的a標籤
    return nextlink["href"]

#主程序:利用迴圈不斷抓取下一頁的標題
pageURL="https://www.ptt.cc/bbs/Gossiping/index.html" #八卦版原始碼
count=0
while count<3: #抓3頁標題
    pageURL="https://www.ptt.cc"+getdata(pageURL) #到下一頁，並再跑一次上面抓標題的程式
    count+=1