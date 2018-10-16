"""
    copy  deepcopy
      深浅拷贝   深拷贝是值拷贝，浅拷贝是引用拷贝
      内存机制与程序的存储机制相关
    迭代器  Iterator
    生成器
"""
from copy import copy, deepcopy
from pickle import loads, dumps


a = [1, 2, 3]
b = [a] * 3

# 拷贝
c = copy(b)

# 深拷贝
d = deepcopy(b)

# 咸菜帮
e = loads(dumps(b, 4))

b[1].append(999)
c[1].append(999)
d[1].append(999)
e[1].append(999)

print(b)
print(c)
print(d)
print(e)

"""
    迭代器模拟费波列数列
    斐波数列
    0，1, 1，2，3，5，8，13...
    迭代器、生成器得好处：
        节省内存、懒性求值
"""


# 自定义一个迭代器 实现斐波那数列
class Fib(object):
    # 初始化设定最大上限
    def __init__(self, max):
        self.x = 0
        self.y = 0
        self.max = max

    # 内置迭代方法
    def __iter__(self):
        return self

    # 返回下一个值得方法
    def __next__(self):
        n_next = self.y
        # 此程序核心部分 建立起斐波列逻辑关系
        self.x, self.y = self.y, self.x + self.y
        # 如果还在设定范围中 返回n_next
        if self.max > n_next:
            return n_next
        else:
            raise StopIteration()


# 需求: 自定义一个生成器函数，实现斐波那契数列

def fib(max):
    x = 0
    y = 1
    while y < max:
        yield y
        x, y = y, x + y


for i in fib(9):
    print(i)
