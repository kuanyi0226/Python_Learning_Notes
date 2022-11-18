a = int(input('a = '))
b = int(input('b = '))
print('%d + %d = %d' % (a, b, a + b))
print('%d - %d = %d' % (a, b, a - b))
print('%d * %d = %d' % (a, b, a * b))
print('%d / %d = %f' % (a, b, a / b))
print('%d // %d = %d' % (a, b, a // b))#商
print('%d %% %d = %d' % (a, b, a % b)) #mod: %只有一個表示佔位符；%%才是百分比符號
print('%d ** %d = %d' % (a, b, a ** b)) #次方

#Practice: 攝氏華氏轉換
degree = int(input('攝氏輸入1;華氏輸入2: '))
currT = float(input('輸入溫度數值: '))

if(degree == 1):
    print('%.1f攝氏度 = %.1f華氏度' % (currT, currT*1.8+32))
elif(degree == 2):
    print('%.1f華氏度 = %.1f攝氏度' % (currT, (currT-32)/1.8))
else:
    print('Wrong input format')
