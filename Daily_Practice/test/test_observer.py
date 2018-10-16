# -*-coding: utf-8 -*-
"""
哨兵模式 分发模式
采用MVC设计思维实现观察者模式   backlog
应用场景模拟: 个人订阅报纸，报社有信息更新，都会发布，每个订阅的人都会收到信息更新
设计模式是面向对象编程的思维的提炼和模板化，要向深入理解面向对象的设计思想，需要学习设计模式
学习设计模式，是写出高质量代码的必备素质，使用设计模式，理解面向对象，使代码更具可读性，更易拓性和可维护性。
"""


class Subscriber(object):
    """
    订阅者，订阅消息 接收通知
    """

    def __init__(self):
        # 定义订阅者列表 __subscribers 是内部定义的类的私有属性
        # 类的属性也不一定非得在__init__中有形参 属性可以分为:自带属性 和 传入属性
        # 自带私有属性__subscribers为一个空列表
        self.__subscribers = list()

    # 定义添加订阅人员的方法(列表添加的方法.append())
    def subscribe(self, subscriber):
        """
        订阅操作 观察者进行订阅
        :param subscriber: 订阅者
        :return:
        """
        # 订阅者列表中添加订阅者
        self.__subscribers.append(subscriber)

    # 定义退订的方法(移除订阅者的方法)(列表中移除的方法.remove())
    def unsubscribe(self, subscriber):
        """
        取消订阅
        :param subscriber:
        :return:
        """
        # 列表中移除方法
        self.__subscribers.remove(subscriber)

    def notify(self, *args, **kwargs):
        """
        遍布订阅者列表 每一个订阅者接收信息  自定义的.recv()方法 接收不定长度参数和关键字参数
        # 通知 消息有更新
        :param args:
        :param kwargs:
        :return:
        """
        for subscriber in self.__subscribers:
            # 是subscriber类在前 超类中用到了子类的方法.recv()
            subscriber.recv(*args, **kwargs)

    def publish(self, msg):
        """
        # 发布消息
        :param msg:
        :return:
        """
        # 发布消息
        self.notify(msg)


# 定义一个继承订阅者的类
class NewsAgency(Subscriber):
    """
    新闻社
    """

    def __init__(self, name='news_agency'):
        """

        :param name：默认为news_agency 子类自身的属性
        """
        self.__name = name
        # py3中超类初始化方法
        # 如果要继承超类的属性 写在__init__()方法中  超类初始化
        # super().__init__()
        Subscriber.__init__(self)

    # 定义新闻社发布消息的方法
    def news_publish(self, msg):
        print(f"news_agency:{self.__name} 要开始发布新闻......")
        self.publish(msg)


class Student(object):
    def __init__(self, name):
        """
        initialize 要传入的接收者的类
        :param name:
        """
        self.__name = name

    # 学生类的接收消息的方法
    def recv(self, data):  # data是我的得到发布数据
        print(f"学生:{self.__name} 收到了  ---》 {data}")


class Teacher(object):
    def __init__(self, name):
        self.__name = name

    def recv(self, data):  # data是我的得到发布数据
        print(f"老师:{self.__name} 发布了 ---》 {data}")


"""代理模式"""


class Manager(object):

    def __init__(self, name):
        self.__name = name
        # 代理模式---此处的类变量是其他类的实例(非传入属性)
        self.__news = NewsAgency()
        # 存放所有订阅的人
        self.__observer_list = list()

    def register(self, subscriber):
        # 注册  将订阅者添加到订阅者李彪中
        self.__observer_list.append(subscriber)

    def subscribe(self):
        """
        遍历观察者列表 调用对象的.subscribe方法 向.__subscribers列表中添加对象
        :return:
        """
        [self.__news.subscribe(subscriber) for subscriber in self.__observer_list]

    def publish(self, msg):
        """
        notify news
        :param msg:
        :return:
        """
        self.__news.publish(msg)


Msg_List = [
    'tom is a cute cat',
    'jack is a lovely dog!'
]

if __name__ == '__main__':
    # 实例化一个管理者
    pet_manager = Manager('pet dealer')
    # 向接收者列表中添加对象
    pet_manager.register(Student('george'))
    pet_manager.register(Student('COCO'))
    pet_manager.register(Teacher('Devin'))
    # 将接收者添加到Manager的列表中
    pet_manager.subscribe()
    # 由Manager(代理) --> Subscriber(人员集合部)--->Student|Teacher调用recv方法 看起来就是Manager托管代理
    [pet_manager.publish(msg=msg) for msg in Msg_List]
