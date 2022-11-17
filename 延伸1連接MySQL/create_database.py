from sqlite3 import Cursor
import mysql.connector #先安裝mysql。 下方輸入: pip install mysql-connector-python

connection = mysql.connector.connect(host='localhost',
                                    port='3306',
                                    user='root',
                                    password='Kevin@0226') #連接資料庫

cursor= connection.cursor() #我們要開始使用了

#創建資料庫
#cursor.execute("CREATE DATABASE `qq`;")

# 取得所有資料庫名稱
#cursor.execute("SHOW DATABASES;") #回傳資料
#records = cursor.fetchall() #讀取回傳資料(列表)
#for r in records:
#     print(r) 
#寫一個迴圈印出回傳的列表資料(一筆一筆)


# 選擇資料庫
#cursor.execute("USE `sql_tutorial`;") #使用這個資料庫


# 創建表格
#cursor.execute('CREATE TABLE `qq`(qq INT);')

cursor.close()
connection.close() #退出執行