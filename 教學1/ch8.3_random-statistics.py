"""隨機模組"""
import random
data=random.choice([1,4,5,6,8])#從列表中隨機選取"1"個資料
print(data)

data=random.sample([1,4,5,6,8],3)#從列表中隨機選取"3"個資料
print(data)

data=[1,4,5,6,8]
random.shuffle(data)#"就地"隨機調換順序(直接更改列表)
print(data)

data=random.random() #取得0~1之間的隨機亂數
print(data)

data=random.uniform(0.0,5.0)#取得0~5間的隨機亂數，每數機率相等
print(data)

data=random.normalvariate(100,10) #取得常態分布亂數:平均數100，標準差10，大部分資料位於90~110
print(data)


"""統計模組"""
import statistics as stat 
data=stat.mean([1,2,3,4]) #平均數
data=stat.median([1,2,3,4]) #中位數
data=stat.stdev([1,2,3,4]) #標準差
print(data)
