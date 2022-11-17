#有序可變動列表List
grades=[12,60,15,70,90]
print(grades)

grades[0]=55 #更新資料:把第一個位置(0號位置)改成55
print(grades)

grades[1:4]=[] #連續刪除(1號到4號)
print(grades)

grades=grades+[30,40] #串接列表
print(grades)

print(len(grades)) #取得列表的長度length

data=[[3,4,5],[9,6,8]] #巢狀列表
print(data[0][2]) #顯示第一個子列表的第一個數字
data[0][0:2]=[5,5,5] #把第一個子列表的3,4改成個5
print(data)

#有序不可變動列表 Tuple
#若更換其資料:產生錯誤
people=(3,6,9)
