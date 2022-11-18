#定義函式:def 函式名(參數名): 。參數讓函式有彈性，可不寫
def multiply():
    print(3*4)
#呼叫函式:函式被定義，但沒被呼叫，內部程式碼就不會執行
multiply()


def multiply(n1,n2):
    print(n1*n2)
value=multiply(5,6) #有彈性
print(value) #定義函式時沒有回傳值，因此印出none


def multiply(n1,n2):
    print(n1*n2)
    return n1*n2 #定義回傳值:後面可以加任何東西，包括字串、布林值等等
value=multiply(5,8)#跳進去定義函式，並回傳n1*n2
print(value)

def multiply(n1,n2):
    return n1*n2
value=multiply(6,5)+multiply(8,9) #各自跳回定義函式，並回傳各自相乘值 #(5*6)+(8*9)
print(value)


#函式的包裝(函式最大的用途:避免不斷重複寫同樣的程式，同樣的邏輯可重覆利用)
def calculate(n1,n2):
    sum=0
    for x in range(n1,n2+1): #迴圈:n1~n2
        sum+=x #等同於sum=sum+x
    print(sum)
R=input("輸入第一數")
R=int(R)
S=input("輸入第二數")
S=int(S)
calculate(R,S)



    

