"1.字串運算"
s="hell\"o" #跳脫:引號前加斜線(與外面的引號做區隔)
print(s)

t="hello\nworld" #換行:亦可以用三個引號(python限定)
print(t)

q="""hello
world"""
print(q)

u="hello"*3+"world"
print(u)

"2.對字串中的字元做操作"
s="hello"
print(s[2]) #字串會對內容字元作編號(索引)，從0開始算起
print(s[1:4]) #顯示從開頭到結尾(不包含結尾)
print(s[1:]) #從開頭顯示到最後一個字
print(s[:4]) #不給結尾顯示前面所有字

"3.判斷字串是否含某元素"
print('he' in s) #True

"4.其他字串函式"
str1 = 'hello, world!'
# 計算長度
print(len(str1)) # 13

# 字串首字大寫
print(str1.capitalize()) # Hello, world!
# 字串每個單字的首字大寫
print(str1.title()) # Hello, World!
# 字串全部變大寫
print(str1.upper()) # HELLO, WORLD!

# 找子字串位置method1
print(str1.find('or')) # 8
print(str1.find('shit')) # -1
# 找子字串位置method2: 但找不到子字串時會發生異常
# print(str1.index('or'))
# print(str1.index('shit'))

# 是否以...開頭
print(str1.startswith('He')) # False
print(str1.startswith('hel')) # True
# 是否以...結尾
print(str1.endswith('!')) # True

# 將字符串以指定的寬度居中，在兩側填充指定的字符
print(str1.center(50, '*'))
# 將字符串以指定的寬度靠右放置左測填充指定的字符
print(str1.rjust(50, ' '))

str2 = 'abc123456'
# 是否由數字組成
print(str2.isdigit())  # False
# 是否由字母組成
print(str2.isalpha())  # False
# 是否由字母、數字組成
print(str2.isalnum())  # True

str3 = '  jackfrued@126.com '
print(str3)
# 修剪左右兩側空白
print(str3.strip())

"5.字串格式輸出"
a, b = 5, 10
print('{0} * {1} = {2}'.format(a, b, a * b))
#python 3.6後，較精簡
print(f'{a} * {b} = {a * b}')
