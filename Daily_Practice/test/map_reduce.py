"""
  map 函数和 reduce函数是python中功能强大的映射数据处理模型
  map 函数为内部函数
  class map(object):

    map(func, *iterables) --> map object

    Make an iterator that computes the function using arguments from
    each of the iterables.  Stops when the shortest iterable is exhausted.
    除数值外，其他5中常见数据类型都是可以迭代对象(iterator)

    reduce 函数为从外部导入 functools导入

    def reduce(function, sequence, initial=None): # real signature unknown; restored from __doc__

    reduce(function, sequence[, initial]) -> value

    Apply a function of two arguments cumulatively to the items of a sequence,
    from left to right, so as to reduce the sequence to a single value.
    For example, reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) calculates
    ((((1+2)+3)+4)+5).  If initial is present, it is placed before the items
    of the sequence in the calculation, and serves as a default when the
    sequence is empty.
    reduce(func, sequence)
    fn函数必须为两个参数，reduce辉先作用前两个参数，再把结果和下一个参数传到下一个函数中 逐渐积累
    L = [a, b, c, d]
    f = func(x, y)
    reduce(func, L)
    func(a, b) --> func(func(a, b), c)-->func(func(func(a,b),c),d)


"""

# map()函数应用场景
# 常量大写
from functools import reduce

# 将字符串转化为整型
DIGITIZATION = {
    '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
}

STRING_SET = {}
for key, value in DIGITIZATION.items():
    STRING_SET[value] = key
print(STRING_SET)


def digitization(char):
    return DIGITIZATION[char]


list1 = ['3', '5', '7']
result = map(digitization, list1)  # result 为<map result> 可迭代对象
for i in result:
    print(i)

# reduce() 应用场景

"""
 需求：
  将字符串 '23214546' 转变为数字 23214546
"""
STRING = '23214546'
num_set = map(digitization, STRING)


def decimal(a, b):
    return a * 10 + b


final = reduce(decimal, map(digitization, STRING))

print(final)
print(type(final))

"""
需求：
 将整型数字 1234567转变成字符型'1234567'
"""

num_list = [1, 2, 3, 4, 5, 6, 7]


def string(num):
    return STRING_SET[num]


def add_str(str1, str2):
    return str1 + str2


num_result = reduce(add_str, map(string, num_list))
print(num_result)
print(type(num_result))

# map reduce 结合lambda匿名函数 filter过滤函数等完成对字符串特定的操作 map reduce 也只有和lambda函数结合使用时，才能显示出其神通广大。
"""
  需求：
    给定一列数字字符串，要求求出字符串中按照升序排列的全偶数最小数。

"""
# 注意对数据处理的层次关系
# reverse为True 排列顺序为降序 默认为升序

LIST = '23123290438547'
great = reduce(lambda x, y: x * 10 + y, filter(lambda x: x % 2 == 0, sorted(list(map(int, LIST)), reverse=False)))
print(great)

"""
  需求：
    将下列的字符串数字转化为最大的奇数
"""

# 将分散的字符串进行合并的方法 | ''.join()
a = ['hello', 'word']
print(''.join(a))

AMAZING = ['34324', '425435', '90823495']
INTERESTING = reduce(lambda x, y: 10 * x + y,
                     filter(lambda x: x % 2 == 1, sorted(list(map(int, ''.join(AMAZING))), reverse=True)))
print(INTERESTING)
