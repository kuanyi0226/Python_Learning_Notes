from selenium import webdriver #協助操控瀏覽器
from selenium.webdriver.common.keys import Keys #讓我們能使用鍵盤上的按鍵去操控網頁(像是Enter鍵)
Path = "C:/chromedriver_win32/chromedriver.exe" #斜線反過來
import time #引入時間，才不會一執行就馬上關閉網頁
from selenium.webdriver.common.by import By #import以下三行，讓explicit wait得以運作
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome(Path) #選擇瀏覽器
driver.get("https://www.letao.com.tw/") #前往目標網址
#print(driver.title) #印出網站名稱

search= driver.find_element_by_name("p") #對搜尋欄按檢查，找到搜尋欄的名字(位置)
search.send_keys("中島みゆき") #在搜尋欄打字
search.send_keys(Keys.RETURN) 
element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "title"))
    )
titles= driver.find_elements_by_class_name("title") #找到標題的class，把全部標題存到titles列表中
for title in titles:
    print(title.text)

#time.sleep(5) #在網站停留五秒
#driver.quit() #把chromedriver關掉