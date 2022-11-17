"數字運算"
#x=3/6=0.5 (小數除法)
#x=3//6=0 (整數除法)
#x=2**3=8 (次方)
#x=7%3=1(取餘數)
x=2+3
x=x+1 #變數有先後,先看等號後(x=5)
print(x)

"字串運算"
s="hell\"o" #跳脫:引號前加斜線(與外面的引號做區隔)
print(s)

t="hello\nworld" #換行:亦可以用三個引號(python限定)
print(t)

q="""hello
world"""
print(q)

u="hello"*3+"world"
print(u)

"對字串中的字元做操作"
s="hello"
print(s[2]) #字串會對內容字元作編號(索引)，從0開始算起
print(s[1:4]) #顯示從開頭到結尾(不包含結尾)
print(s[1:]) #從開頭顯示到最後一個字
print(s[:4]) #不給結尾顯示前面所有字
