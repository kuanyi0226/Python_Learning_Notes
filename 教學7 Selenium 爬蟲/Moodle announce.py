from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
Path = "C:/chromedriver_win32/chromedriver.exe" 
import time 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome(Path) 
driver.get("https://moodle.ncku.edu.tw/message/output/popup/notifications.php") 
driver.implicitly_wait(10) #等待頁面跳轉完畢

driver.find_element_by_xpath('//*[@id="page-wrapper"]/nav/ul[2]/li[2]/div/span/a').click() #點擊登入按鈕

search= driver.find_element_by_name("username") #找到帳號輸入框
search.send_keys("C34104032") #輸入帳號
search= driver.find_element_by_name("password") #找到密碼輸入框
search.send_keys("Kevin@0226") #輸入密碼
search.send_keys(Keys.RETURN) #登入! 到達"通知"頁面



