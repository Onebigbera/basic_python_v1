"""
re regular 正则表达式
     re.match(pattern, string, flags=0)  扫描整个字符串，返回从起始位置的匹配
     re.search(pattern, string, flags=0)  扫描整个字符串，并返回第一个成功的匹配
    re.findall(pattern, string, flags=0)  返回整个字符串，斌返回结果--列表
    re.sub   匹配字符串中特定的字符串并将其转换为指定的字符串
    re.subn  返回一个元祖 第一个元素为被替换后的字符串 第二个元素为被替换的次数

    \d    数字     digital
    \D    非数字
    \w    字母 数字 下划线
    \W    非字母 非数字 非下划线
    \s    空格     space
    \S    非空格
    [] 单个元素匹配 匹配中括号中的任意一个元素
    [a-z]
    [A-Z]
    [0-9]
    [^]   取反
    ^  $  匹配开头和结尾
    *     匹配0-多次
    ？    匹配0-1 次
    +     匹配1-  次
    {n}   匹配指定的次数  eg : {3} 匹配三次
    {1，3} 匹配1， 2， 3 次
    a|b|d|e|   管道匹配




"""
import re

#
# string = 'www.google.com'
# result = re.match('www', string=string)
# # print(result)
#
# # 匹配样板在匹配母版中的索引
# print(re.match('www', 'www.google.com').span())
#
# # 未匹配到则返回None
# print(re.match('www', 'ww.google.com'))
#
# # 判断是否从开头开始匹配
# print(re.match('www', 'google.www.com'))
#
# # 是否区分大小写
# print(re.match('www', 'wwW.google.com'))
#
# # 设置flags 匹配是忽略大小写
# print(re.match('www', 'wwWw.google.com', flags=re.I).span())
#
# # re.search()
# print(re.search('www', 'www.google.com').span())
#
# 返回第一个成功的匹配
# print(re.search('test', 'this is a test, test how re work').span())

# 匹配所有，返回迭代器  列表
# print(re.findall('love', 'this word suppose to be full love, people love in friendship, kinship and romance'))

a = 'jfasdjdsadsfsajffa67sdad08//878AGF/GT'
# 找出字符串中所有的 'jf'
print(re.findall(r"jf", a))

# 匹配后面跟着 'f' 的 'j'
print(re.findall(r"(j)f", a))

# 匹配前面有 'j' 的 'f'
print(re.findall(r"j(f)", a))

# 匹配所有[a-z]范围里的小写字母
print(re.findall(r"[a-z]", a))

# 取出所有的非小写字母
print(re.findall(r"[^a-z]", a))

# 匹配管道中所有 可以多管道
print(re.findall(r"a|b|d|", 'dsafadbdaafhwejlabjba'))

# re.sub 匹配字符串中特定的字符串并将其转换为指定的字符串
b = 'tom is a very very kind man '

# 匹配指定字符串中的字符串 并将其替换为指定的字符串
print(re.sub(r"(very)", "nice", b))

# 打印其类型
print(type(re.sub(r"(good)", "nice", b)))

# 返回一个元祖 第一个元素为被替换后的字符串 第二个元素为被替换的次数
print(re.subn(r"(very)", "so", b))  # ('tom is a so so kind man ', 2)
print(type(re.subn(r"(very)", "so", b)))



