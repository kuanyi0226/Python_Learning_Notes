"一、生成式(Comprehension): list, set, dictionary, tuple"
"有序可變動列表List"
print("List")
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
print("Tuple---------------------------------")
#若更換其資料:產生錯誤
people=(3,6,9)
print(people)

"Set(集合)的運算"
print("Set---------------------------------")
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
print("Dictionary---------------------------------")
dic={"apple":"蘋果","bug":"蟲蟲"}
dic["apple"]="小蘋果" #更改字典
print(dic["apple"]) #打key跑出value

print("apple" in dic) #判斷key是否在字典中(而非value)

del dic["apple"] #刪除字典中的鍵值對(key-value pair)

dic={x:x*2 for x in [3,4,5]} #x是從列表來的:把3,4,5乘以2 /從列表資料產生字典
print(dic)

#Practice: 用股價超過100的創造新字典
stocks1 = {
    'AAPL': 191.88,
    'GOOG': 1186.96,
    'IBM': 149.24,
    'ORCL': 48.44,
    'ACN': 166.89,
    'FB': 208.09,
    'SYMC': 21.29
}

stocks2 = {key: value for key, value in stocks1.items() if value > 100}
print(stocks2)


"二、更多資料結構、演算法"
"Heap: 最大最小堆排序"
import heapq

print("Heap---------------------------------")
list1 = [34, 25, 12, 99, 87, 63, 58, 78, 88, 92]
list2 = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]
print(heapq.nlargest(3, list1)) #list1中前三大的
print(heapq.nsmallest(3, list1)) #list1中前三小的
print(heapq.nlargest(2, list2, key=lambda x: x['price'])) #list2中price前兩大的
print(heapq.nlargest(2, list2, key=lambda x: x['shares'])) #list2中shares前兩大的

"itertools"
print("itertools---------------------------------")
import itertools
# 产生ABCD的全排列
itertools.permutations('ABCD')
# 产生ABCDE的五选三组合
itertools.combinations('ABCDE', 3)
# 产生ABCD和123的笛卡尔积
itertools.product('ABCD', '123')
# 产生ABC的无限循环序列
itertools.cycle(('A', 'B', 'C'))


"collections"
"""常用的工具类：
namedtuple：命令元组，它是一个类工厂，接受类型的名称和属性列表来创建一个类。
deque：双端队列，是列表的替代实现。Python中的列表底层是基于数组来实现的，而deque底层是双向链表，因此当你需要在头尾添加和删除元素时，deque会表现出更好的性能，渐近时间复杂度为$O(1)$。
Counter：dict的子类，键是元素，值是元素的计数，它的most_common()方法可以帮助我们获取出现频率最高的元素。Counter和dict的继承关系我认为是值得商榷的，按照CARP原则，Counter跟dict的关系应该设计为关联关系更为合理。
OrderedDict：dict的子类，它记录了键值对插入的顺序，看起来既有字典的行为，也有链表的行为。
defaultdict：类似于字典类型，但是可以通过默认的工厂函数来获得键对应的默认值，相比字典中的setdefault()方法，这种做法更加高效。"""
print("collections---------------------------------")
from collections import Counter

words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around',
    'the', 'eyes', "don't", 'look', 'around', 'the', 'eyes',
    'look', 'into', 'my', 'eyes', "you're", 'under'
]
counter = Counter(words) 
print(counter.most_common(3)) #找出現最多次(前三多)的







