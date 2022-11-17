#集合的運算
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

#字典的運算:key-value配對
dic={"apple":"蘋果","bug":"蟲蟲"}
dic["apple"]="小蘋果" #更改字典
print(dic["apple"]) #打key跑出value

print("apple" in dic) #判斷key是否在字典中(而非value)

del dic["apple"] #刪除字典中的鍵值對(key-value pair)

dic={x:x*2 for x in [3,4,5]} #x是從列表來的:把3,4,5乘以2 /從列表資料產生字典
print(dic)

