"""
    单例模式的推荐使用方式
    下面将演示用__new__方法实现的单例方式
    这种方法实现的单例模式，以后实例化对象时，和平时实例化对象方法一样，obj = Singleton()
"""

import threading


class Singleton(object):
    # 给线程加锁 赋值给私有属性 实例锁
    _instance_lock = threading.Lock()

    def __init__(self):
        pass

    def __new__(cls, *args, **kwargs):
        # 判断创建的对象是否有私有属性
        if not hasattr(Singleton, '_instance'):
            # 打开实例锁？？？？？
            with Singleton._instance_lock:
                if not hasattr(Singleton, '_instance'):
                    # 创建对象的时候动态绑定_instance私有属性
                    Singleton._instance = object.__new__(cls)
        # 返回私有属性_instance
        return Singleton._instance


# 实例化两个对象
obj1 = Singleton()
obj2 = Singleton()
print(obj1, obj2)


def task(arg):
    obj = Singleton()
    print(obj)


for i in range(10):
    t = threading.Thread(target=task, args=[i, ])
    t.start()
