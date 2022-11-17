#定義類別與類別屬性(封裝在類別中的變數和函式)
class IO: #定義一個類別IO有兩個屬性
    supportedsrcs=["console","file"] #屬性一supportedsrcs
    def read(src): #屬性二read
        if src not in IO.supportedsrcs:
            print("not supported")
        else:
            print("read from",src) 

#使用類別:類別名稱.屬性名稱 =>取得資料
print(IO.supportedsrcs) #印出列表
IO.read("file") #呼叫類別中的函式
IO.read("internet")

""""""""""""
#定義類別與實體物件、實體屬性
#Point 實體物件的設計:平面座標上的點p1和p2
class Point:
    def __init__(self,x,y): #定義初始化函式:__init__(self,參數1,參數2)。參數可不寫，其他固定
        self.x=x #此實體物件包含x和y兩個實體屬性
        self.y=y
p1=Point(3,4) #建立第一個實體物件，放入變數p1中/呼叫初始化函式
print(p1.x,p1.y)
p2=Point(5,6) #建立第二個實體物件，放入變數p2中
print(p2.x,p2.y)


#Fullname 實體物件設計:分開紀錄姓、名資料的全名
class Fullname:
    def __init__(self):
        self.first="kevin"
        self.last="ho"
name1=Fullname() #不用打self
print(name1.first,name1.last)

class fullname: #改成有彈性的寫法
    def __init__(self,firs,las):
        self.firs=firs
        self.las=las
name1=fullname("kevin","ho")
print(name1.firs,name1.las)
name2=fullname("ken","chen")
print(name2.firs,name2.las)


#實體方法(函式)
class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    #定義實體方法(可以有很多個)
    def show(self):
        print(self.x,self.y)
    def distance(self,targetx,targety):
        return ((self.x-targetx)**2+(self.y-targety)**2)**0.5
p=Point(3,4)
p.show() #呼叫實體方法
result=p.distance(0,0) #計算座標3,4與座標0,0的距離
print(result)
#File 實體物件設計: 包裝檔案讀取的程式
class file:
    def __init__(self,name): #定義初始化函式，有兩個實體屬性
        self.name=name
        self.file=None #尚未開啟檔案，初期是None
    def open(self): #定義open方法:open一個檔案放到self.file裡面
        self.file=open(self.name,mode="r",encoding="utf-8")
    def read(self): #定義read方法:讀取並回傳剛剛得到的檔案物件self.file
        return self.file.read()
#讀取第一個檔案
f1=file("data1.txt") #建立實體物件放在f1
f1.open() #利用f1代表實體物件呼叫實體方法:跑def open那段code
data=f1.read() #接著呼叫另一個實體方法:跑def read那段code
print(data)
#讀取第二個檔案
f2=file("data2.txt")
f2.open()
data=f2.read()
print(data)


