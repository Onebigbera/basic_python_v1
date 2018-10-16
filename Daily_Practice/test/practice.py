# -*-coding:utf-8 -*-
"""
create on Monday july 30 19:34:55 2018
@author:Black Jone

"""


# class Person(object):
#     name = ''
#     age = 0
#     __weight = 0
#
#     # 构造函数 在生成对象时调用
#     def __init__(self, name, age, weight):
#         # 给类的属性重新赋值
#         self.name = name
#         self.age = age
#         # 注意用法
#         self.__weight = weight
#
#     # 构析函数 释放对象时使用
#     def __del__(self):
#         pass
#
#     #  打印 转换
#     def __repr__(self):
#         pass
#
#     # 按照索引赋值
#     def __setitem__(self, key, value):
#         pass
#
#     # 按照索引取值
#     def __getitem__(self, item):
#         pass
#
#     # 获取长度
#
#     def __len__(self):
#         name_del = self.name.__len__()
#         print(name_del)
#
#     # 比较长度
#     def __cmp__(self):
#         pow_age = self.age.__pow__(2)
#         print(pow_age)
#
#     # 函数调用
#     def __call__(self, *args, **kwargs):
#         pass
#
#     # 加法
#     def __add__(self):
#         adds = self.age.__add__(self.__weight)
#         print(adds)
#
#     # 减法
#     def __sub__(self, other):
#         pass
#
#     # 乘法
#     def __mul__(self, other):
#         pass
#
#     # 取余数
#     def __mod__(self, other):
#         pass
#
#     # 求成方
#     def __pow__(self, power, modulo=None):
#         pass
#
#     def information(self):
#         # 注意参数是怎么样传递的
#         return "hello!everyone!i'm %s,i'%s years old,and i'm %s pound" % (self.name, self.age, self.__weight)
#
#
# if __name__ == '__main__':
#     person = Person('TOM', 25, 65)
#     print(person.information())
#     print(person.__class__)
#     print(person.__repr__())
#
#     infor = person.information()
#     cmp = person.__cmp__()
#     lens = person.__len__()
#     adds = person.__add__()
#     print('doc is %s' % person.__doc__)
#     print('dir is %s' % person.__dir__)
#     print('delatter is %s' % person.__delattr__)
#     print('gt is %s' % person.__getitem__)
#     print('hash is %s' % person.__hash__)
#     print('init is %s' % person.__init__)
#     print('new is %s' % person.__new__)
#     print(infor)
#     print(cmp)
#     print(adds)


# 不要同时用
# class Person(object):
#     tall = 180
#     hobbies = []
#
#     def __init__(self, name, age, weight):
#         self.name = name
#         self.age = age
#         self.weight = weight
#
#     def infoma(self):
#         print('%s is %s weights %s' % (self.name, self.age, self.weight))
#
#
# print(Person.__name__)
# print(Person.__doc__)
# print(Person.__bases__)
# print(Person.__dir__)
# print(Person.__module__)
# print(Person.__class__)

# test class_methods
class Person(object):
    # 定义属性 - 定义默认属性
    # name = '孙悟空'
    # age = '6596'
    # money = 64645

    # 构造方法 在类被实例化的时候自动调用
    def __init__(self, name, age, money):
        self.name = name
        self.age = age
        self.money = money

    # Build a method for the class
    def tell(self):
        print("i'm %s,%s years old,and has %s" % (self.name, self.age, self.money))


# .super()  usage
class Bastard(Person):
    Bad_hobby = None

    def __init__(self, name, age, money, bad_hobby):
        # 子类继承父类构造方法中的属性| .__init__保护方法需要加上去 超级构造方法 *****重点*****
        super().__init__(name, age, money)
        print('A bastard was created!')
        # 子类扩展的自身属性
        self.bad_hobby = bad_hobby

    # 设置不良行径方法
    def set_hobby(self, hobby):
        # 使用self时 相当于已经使用了构造方法已经将属性进行了绑定
        self.bad_hobby = hobby

    # 重写父类的方法 | 复写父类的方法
    def tell(self):
        print('I have just change the method of parents,Set %s' % self.bad_hobby)

    def do_it(self):
        print('what i like is to show love to everyone %s' % self.bad_hobby)


if __name__ == '__main__':
    Gide = Bastard('怪盗基德', 25, 544, 'drunk')
    Gide.tell()
    Gide.do_it()