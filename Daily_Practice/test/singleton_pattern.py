"""
singleton pattern ：单例模式
    一种常见的软件设计模式，该模式的主要目的在程序运行时某个类的实例只能存在一个。因此当在系统中某个类只能出现一个实例时，这时就需要用到单例模式
    当系统中某个类有大量实例时，对系统的能存资源有极大的消耗。例如:某些配置相关的实例
    实现单例模式的几种方式
    1.使用模块实现
    2.使用装饰器实现
    3.使用类实现
    4.基于创建类的__new__方法实现
    5.基于metaclass方式实现

"""
# 1.使用模块实现
"""
    其实，Python 的模块就是天然的单例模式，因为模块在第一次导入时，会生成 .pyc 文件(以c语言编译)，当第二次导入时，就会直接加载 .pyc 文件，而不会再次执行模块代码。因此，我们只需把相关的函数和数据定义在一个模块(.py文件)中，就可以获得一个单例对象了。如果我们真的想要一个单例类，可以考虑以下方法：
    <1> 单独创建一个.py模块
    <2> 将上面的代码保存在文件 mysingleton.py 中，要使用时，直接在其他文件中导入此文件中的对象，这个对象即是单例模式的对象 直接导入即可

from xxx import singleton
"""


# 创建类
class Singleton(object):
    def foo(self):
        pass


# 实例化对象
singleton = Singleton()

# 使用装饰器实现
"""
    在多线程情况下使用会存在问题 资源抢占问题

"""


# 用装饰器实现单例模式 保证类的实例只能唯一
def singleton_pattern(cls):
    _instance = {}

    def _singleton_pattern(*args, **kwargs):
        # _instance是一个字典，in|not in 默认判断为字典的key
        if cls not in _instance:
            _instance[cls] = cls(*args, **kwargs)
            # 返回包含实例的字典_instance
        return _instance

    return _singleton_pattern


# 装饰器装饰类 给类添加限制也可以的  其实类和函数一样都是实现固定功能 此处就是使类称为单例
@singleton_pattern
class A(object):
    a = 1

    def __init__(self, x=0):
        self.x = x


a1 = A(2)
a2 = A(3)

# 使用类的方法实现
"""
    无法支持多线程，不能保证数据安全
"""


class SinglePattern(object):

    # 每次实例化时都睡眠一秒
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs
        import time
        time.sleep(1)
        # pass

    @classmethod
    def instance(cls, *args, **kwargs):
        if not hasattr(SinglePattern, '_instance'):
            # 类的动态绑定属性  将类的实例化对象动态绑定为类的属性_instance  类的属性绑定
            SinglePattern._instance = SinglePattern(*args, **kwargs)
            # 返回类的实例 单实例
        return SinglePattern._instance


import threading


def task(arg):
    # 类方法
    obj = SinglePattern.instance()
    print(obj)


# for i in range(10):
#     t = threading.Thread(target=task, args=[i, ])
#     t.start()

"""
    解决方法 加锁 运行速度降低，保证了数据安全
    这样就差不多了，但是还是有一点小问题，就是当程序执行时，执行了time.sleep(20)后，下面实例化对象时，此时已经是单例模式了，但我们还是加了锁，这样不太好，再进行一些优化，把instance方法，改成下面的这样就行：
"""

import time
import threading


class SingleCase(object):
    # 进程锁
    _instance_lock = threading.Lock()

    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs
        time.sleep(1)

    @classmethod
    def instance(cls, *args, **kwargs):
        # 如果SingleCase 没有单实例
        if not hasattr(SingleCase, '_instance'):
            # 给单实例类 上锁
            with SingleCase._instance_lock:
                if not hasattr(SingleCase, '_instance'):
                    SingleCase._instance = SingleCase(*args, **kwargs)
        # 返回单实例  _instance是很重要的单例标识    此时SingleCase 已经有了._instance属性(动态绑定) 如果有了._instance属性 直接返回已经有的
        return SingleCase._instance

"""
     优化的instance方法
     @classmethod
     def instance()
"""


def test(arg):
    obj = SingleCase.instance()
    print(obj)


for i in range(10):
    # 开线程
    t = threading.Thread(target=test, args=[i, ])
    t.start()
time.sleep(10)
obj = SingleCase.instance()
print(obj)
# 验证单例对象是否发生了改变
