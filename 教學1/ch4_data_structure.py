"有序可變動列表List"
grades=[12,60,15,70,90]
print(grades) #[12,60,15,70,90]

grades[0]=55 #更新資料:把第一個位置(0號位置)改成55
print(grades) #[55, 60, 15, 70, 90]

grades[1:4]=[] #連續刪除(1號到4號)
print(grades) #[55, 90]

grades=grades+[30,40] #串接列表
print(grades) #[55, 90, 30, 40]

print(len(grades)) #取得列表的長度length = 4

data=[[3,4,5],[9,6,8]] #巢狀列表
print(data[0][2]) #顯示第一個子列表的第一個數字 = 5
data[0][0:2]=[5,5,5] #把第一個子列表的3,4改成個5
print(data) #[[5, 5, 5, 5], [9, 6, 8]]

#添加、移除元素
list1 = [1, 3, 5, 7, 100]
# 添加元素
list1.append(200)
list1.insert(1, 400)
print(list1) # [1, 400, 3, 5, 7, 100, 200]

# 判斷元素是否在列表中，如果存在就刪除該元素
if 3 in list1:
	list1.remove(3)
if 1234 in list1:
    list1.remove(1234)
print(list1) #[1, 400, 5, 7, 100, 200]

# 從指定位置刪除元素
list1.pop(0)
list1.pop(len(list1) - 1)
print(list1) #[400, 5, 7, 100]
# 清空列表元素
list1.clear()
print(list1) # []


"有序不可變動列表 Tuple(元組)"
#若更換其資料:產生錯誤
people=(3,6,9)


"Set(集合)的運算"
s1={3,4,5}
print(10 not in s1) #10是否在s1裡面
s2={4,5,6,7}

s3=s1&s2 #交集
s3=s1|s2 #聯集
s3=s1-s2 #差集:s1減去與s2有重疊的部分
s3=s1^s2 #反交集:取s1及s2不重疊的部分
print(s3)

s=set("Hello") #set(字串) :把字串拆解成集合(不重複，無順序)
print(s)
print("H" in s) #H有沒有在字串裡面


"Dictionary(字典)的運算:key-value配對"
dic={"apple":"蘋果","bug":"蟲蟲"}
dic["apple"]="小蘋果" #更改字典
print(dic["apple"]) #打key跑出value

print("apple" in dic) #判斷key是否在字典中(而非value)

del dic["apple"] #刪除字典中的鍵值對(key-value pair)

dic={x:x*2 for x in [3,4,5]} #x是從列表來的:把3,4,5乘以2 /從列表資料產生字典
print(dic)


