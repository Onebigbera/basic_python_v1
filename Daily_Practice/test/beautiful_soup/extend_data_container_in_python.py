# -*- coding: utf-8 -*-
"""
  除了我们使用的那些基础的数据结构，python中还包括其他的模块提供的数据结构，有时候甚至比基础的数据结构还强大。

"""

__author__ = 'george'
__date__ = '2018/9/5'

# deque 类
from collections import deque

# 创0建一个deque
q = deque(range(5), maxlen=5)  # deque([0, 1, 2, 3, 4], maxlen=5)
print(q)
for i in q:
    print(i)
q.append(5)
print(q) # deque([1, 2, 3, 4, 5], maxlen=5)
q.rotate(3)
print(q)  #  deque([3, 4, 5, 1, 2], maxlen=5)
q.appendleft(-1)
print(q) #  deque([-1, 3, 4, 5, 1], maxlen=5)
q.extendleft([11, 22, 33])
print(q) # deque([33, 22, 11, -1, 3], maxlen=5)


# Counter 类
from collections import Counter
c = Counter('hello,python, programming is a magic ')
print(c)
c.update('yes it is interesting!')
print(c)
print(c.most_common(5)) # 将出现次数最多的前几个以列表中以元祖为单位展示

# defaultdict
from collections import defaultdict
d = defaultdict(list)
print(d['a'])
d['a'].append(1)
d['a'].append(2)
d['a'].append(3)
print(d)
s = 'i love china'
d = defaultdict(int)
for k in s:
    d[k] += 1
print(d)
print(sorted(d.items()))
