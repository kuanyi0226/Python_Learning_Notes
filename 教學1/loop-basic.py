#while迴圈

#n=1 
#while True: True的T要大寫
#    print(n)
#    n+=1     無窮迴圈

n=1
while n<=5: #n=6時為false，停止迴圈
    print(n)
    n+=1 

n=1
sum=0 #紀錄累加的結果，從1加到10
while n<=10:
    sum=sum+n
    n+=1
print(sum) #不在迴圈內，印出迴圈結果


#for迴圈
for x in [3,5,1]: 
    print(x) #固定結構for in ，依序印出list內的數字

for x in "hello":
    print(x)

for x in range(5): #搭配range會自動生成一個連續list。range(5)=[0,1,2,3,4,5]
    print(x)

for x in range(2,4):#包頭不包尾，注意是打,而不是:
    print(x)

sum=0
for x in range(1,10001):
    sum+=x #注意先前假設的變數是x，而不是n
print(sum)

