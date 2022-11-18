import re

#re模組: 處理複雜字串，可應用於爬蟲

"ex1 驗證輸入用戶名和號碼是否有效並給出對應的提示訊息"
#用戶名必須由字母、數字或下畫線構成且長度在 6 ~ 20 個字元之間，號碼是 5 ~ 12 個數字且第一位不能是 0。
def main1():
    username = input('請輸入用戶名: ')
    number = input('請輸入號碼: ')
    # match函數的第一個參數是正規表示式字串或正規表示式對象
    # 第二個參數是要跟正規表示式做匹配的字串
    m1 = re.match (r'^[0-9a-zA-Z_]{6,20}$', username)
    if not m1:
        print('請輸入有效的用戶名')
    m2 = re.match (r'^[1-9]\d{4,11}$', number)
    if not m2:
        print('請輸入有效的號碼')
    if m1 and m2:
        print('你輸入的訊息是有效的!')

if __name__ == '__main__':
    main1()


"ex2 從一段文字中提取出手機號碼"
import re

def main2():
    # 創建正規表示式對象 
    pattern = re.compile(r'(?<=\D)09[0-9]{8}(?=\D)')
    sentence = '''
    重要的事情說 0123456789 遍，Andy 的手機號碼是 0912345678，
    不是 0912456789，也不是 110 或 119，Alan 的手機號碼才是 0912456789。
    '''
    # 查詢所有匹配並保存到一個列表中
    mylist = re.findall(pattern, sentence)
    print(mylist)
    print('----------------')
    # 利用迭代器取出匹配對象並獲得匹配的内容
    for temp in pattern.finditer(sentence):
        print(temp.group())
    print('----------------')
    # 利用 search 函數指定搜索位置找出所有匹配
    m = pattern.search(sentence)
    while m:
        print(m.group())
        m = pattern.search(sentence, m.end())

if __name__ == '__main__':
    main2()


"ex3 替換字串中的不良內容"
def main3():
    sentence = '你是笨蛋? Fuck!!! shit!!!'
    purified = re.sub('fuck|shit|笨蛋',
                    '*', sentence, flags = re.IGNORECASE)
    print(purified)  

if __name__ == '__main__':
    main3()


"ex4 拆分長字串"
def main4():
    poem = '床前明月光，疑是地上霜。舉頭望明月，低頭思故鄉。' #string
    sentence_list = re.split(r'[，。, .]', poem) #list
    while '' in sentence_list:
        sentence_list.remove('')
    print(sentence_list)  
if __name__ == '__main__':
    main4()