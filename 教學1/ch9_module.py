#載入sys模組(內建的)並取得資訊
import sys
print(sys.platform) #印出作業系統
print(sys.maxsize) #印出整數型態最大值
print(sys.path) #印出搜尋模組的路徑列表:import模組時，模組必須在路徑中，否則import失敗


#載入module資料夾(剛剛建的)中的geometry.py模組
#若module資料夾跟本程式不在同個路徑，重新定義module資料夾的路徑:在模組搜尋路徑中"新增搜尋路徑"
sys.path.append("modules")

import geometry #improt 模組名
result=geometry.distance(1,1,5,5) #模組名.模組內函式名
print(result)
result=geometry.slope(1,2,5,6)
print(result)