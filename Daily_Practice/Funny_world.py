import os

# print(os.name)
# print(os.listdir())
# os.mkdir('test')
# os.makedirs('test/hello')
# os.makedirs('funny/test')
# os.rmdir('funny/test')
# os.rmdir('test/hello')
# os.rmdir('funny')
# print(os.getcwd())
# print(os.walk(os.getcwd()))
# walk_result = os.walk(os.getcwd())
# for file in walk_result:
#     print(file)
# 目录和路径差别
# 获取当前工作目录
# print(os.getcwd())
# 获取当前工作路径
# print(os.path.abspath('funny_world.py'))
# print(os.path.split(os.path.abspath('funny_world.py')))
# print(os.path.basename(os.path.abspath('funny_world.py')))
# print(os.path.exists(os.getcwd()))
# print(os.path.exists(os.path.abspath('funny_world.py')))
# print(os.path.join('hello', 'world'))
# print(os.path.isdir(os.getcwd()))
# print(os.path.isdir(os.path.abspath('funny_world.py')))
# print(os.path.isfile('funny_world.py'))
# print(os.path.getsize('funny_world.py'))
# print(os.path.getsize(os.path.abspath('funny_world.py')))
import time


# 获取时间戳格式时间  表示从1970年1月1日都现在为止经历的秒数
# print(time.time())
# print(os.path.getatime('funny_world.py'))
# print(os.path.getmtime('funny_world.py'))
# print(os.path.getctime('funny_world.py'))
# print(type(time.time()))
# print(time.localtime())
# print(time.localtime(154515456))
# print(time.gmtime())
# print(time.localtime())
# print(time.mktime(time.localtime()))
# print(time.time())
# print(time.ctime())
# print(time.asctime())
# print(time.asctime(time.gmtime()))
# print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
# print(time.strptime(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()),'%Y-%m-%d %H:%M:%S'))
# print(time.sleep(5))
# print(time.clock())

class Fib2(object):
    def __init__(self, n):
        # 自带属性 a b count | 传入属性n
        self.a = 0
        self.b = 1
        self.n = n
        # 计算器 计算天数
        self.count = 0

    # 返回自身
    def __iter__(self):
        return self

    def __next__(self):
        res = self.a
        # 逻辑部分 递归函数
        self.a, self.b = self.b, self.a + self.b
        # 计算超出需求 抛出异常
        if self.count > self.n:
            raise StopIteration
        self.count += 1
        # 每次调用next()函数后计算都会累加1
        return res


print(list(Fib2(3)))



