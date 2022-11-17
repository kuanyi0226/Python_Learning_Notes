n=0
while n<5:
    if n==3:
        break #強制停止迴圈
    print(n) #印出迴圈中的n
    n+=1
print("最後n=",n) #印出迴圈結束後的n #加,印出多種格式


n=0
for x in [0,1,2,3]: #此時x用來控制迴圈的次數
    if x%2==0: 
        continue #若x為偶數，則該數跳過以下程式，強制回到迴圈
    print(x) #印出x等於多少時n能夠+1
    n+=1
print(n)



sum=0
for n in range(11):
    sum+=n
else: #迴圈結束前執行以下程式
    print(sum) #印出0加到10的結果


#找出整屬平方根
#輸入9得到3，輸入11得到"沒有整數平方根"
n=input("輸入一個正整數:")
n=int(n)
for i in range(n+1): #i從0~n
    if i*i==n:
        print("有正整數根",i)
        break
    else:
        print("沒有正整數平方根")
