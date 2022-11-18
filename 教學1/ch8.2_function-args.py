#參數可以有預設資料
def power(base,exp=0): #開方預設為0
    print(base**exp) #**為次方
power(2,3)
power(2) #因為沒打開方為多少，因此預設為0


#參數的名稱對應"順序"可以改
def divide(n1,n2):
    print(n1/n2)
divide(4,2)
divide(n2=4,n1=2)


#不定參數數量:在參數名稱前加*，資料會以Tuple(有序不可動列表)來處理
def avg(*number):
    print(number)
avg(1,3)
avg(1,5,7,-22)

def avg(*number): #算平均數
    sum=0
    for n in number:
        sum+=n
    print(sum/len(number))
avg(1,3,5,7,9)
