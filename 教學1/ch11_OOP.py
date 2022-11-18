"一、封裝"
"private 在名稱前加兩個底線__"

"@property decorator"
"""
class Person(object):

    def __init__(self, name, age):
        self._name = name
        self._age = age

    #getter方法
    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    # 修改器 - setter方法
    @age.setter
    def age(self, age):
        self._age = age

    def play(self):
        if self._age <= 16:
            print('%s正在玩盪鞦韆.' % self._name)
        else:
            print('%s正在賭博.' % self._name)



person = Person('小明', 12)
person.play()
person.age = 22
person.play()
# person.name = '大明'  # AttributeError: can't set attribute
"""


"__slots__"
class Person:
    __slots__ = ('_name', '_age', '_gender')

    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    def play(self):
        if self._age <= 16:
            print('%s正在玩飞行棋.' % self._name)
        else:
            print('%s正在玩斗地主.' % self._name)

def main():
    person = Person('王大锤', 22)
    person.play()
    person._gender = '男'
    # AttributeError: 'Person' object has no attribute '_is_gay'
    # person._is_gay = True