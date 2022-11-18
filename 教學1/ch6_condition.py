#判斷式
#x=input("請輸入數字:") #取得字串形式的使用者輸入
#x=int(x) #將字串型態轉換成數字型態，才能比較大小
#if x>100: #回傳布林值
#    print("大於100")
#elif x>50:
#    print("大於50")
#else:
#    print("小於50")

#四則運算
n1=int(input("請輸入數字一:"))
n2=int(input("請輸入數字二:"))
#print(n1*n2)
op=input("請輸入運算:+,-,*,/")
if op=="+":
    print(n1+n2)
elif op=="-":
    print(n1-n2)
elif op=="*":
    print(n1*n2)
elif op=="/":
    print(n1/n2)
else:
    print("不支援運算")

    