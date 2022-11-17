import mysql.connector

connection = mysql.connector.connect(host='localhost',
                                    port='3306',
                                    user='root',
                                    password='Kevin@0226',
                                    database='sql_tutorial') #連接資料庫時，可以先直接連到需要的資料庫

cursor = connection.cursor()

# 取的部門表格所有資料
cursor.execute('SELECT * FROM `branch`;')

records = cursor.fetchall()
for r in records:
    print(r)

cursor.close()
connection.close()