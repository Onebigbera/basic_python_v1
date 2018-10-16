# -*- coding: utf-8 -*-
"""
    列举几个列子，通过对比查看使用super()方法继承时的用法
"""

# **********显示地调用父类方法**********
# class SuperClass(object):
#     def act(self):
#         print("Super Class act method ...")
#
#
# class SubClass(SuperClass):
#     def act(self):
#         SuperClass.act(self)  # 显式地调用父类方法 传统父类方法调用
#         print("SubClass act method ...")


#
# if __name__ == '__main__':
#     sub = SubClass()
#     sub.act()


# **********python2x和python3x中使用差*************
"""
    super()方法只能在py3.x中使用，py2.x必须要指明类名
"""

# class SuperClass(object):
#     def act(self):
#         print("Super Class act method ...")
#
#
# class SubClass(SuperClass):
#     def act(self):
#         super().act()
#         # super(SubClass,self).act()     # py2.x 调用父类，过于复杂，这个可以正常执行
#         print("SubClass act method ...")

# if __name__ == '__main__':
#     sub = SubClass()
#     sub.act()


# **********super在多继承中的使用******************
# class A(object):
#     def act(self):
#         print("call A act method ....")
#
#
# class B(object):
#     def act(self):
#         print("call B act method ....")
#
#
# class C(B, A):  # 搜索的顺序会从B开始搜索，B存在act方法则调用并返回，不再继续搜索
#     def act(self):
#         super().act()
#
#
# if __name__ == '__main__':
#     c = C()
#     c.act()


# ************super()不支持算术运算符*******************
# class E(object):
#     def __getitem__(self, item):
#         print("call E __getitem__ method ...")
#
#
# class F(E):
#     def __getitem__(self, item):
#         print('call F __getitem__ method ..')
#         E.__getitem__(self, item)
#         super().__getitem__(item)
#         super()[item]       # 不支持运算符操作，'super' object is not subscriptable
#
# def test_opr():
#     f = F()
#     f[2]
#
# if __name__ == '__main__':
#     test_opr()


# ************在运行时可以改变类的继承树()**************
# class X(object):
#     def m1(self):
#         print("call X method")
#
#
# class Y(object):
#     def m1(self):
#         print("call Y method")
#
#
# class Z(X):
#     def m1(self):
#         super().m1()
#
#
# def test_z():
#     z = Z()
#     z.m1()
#     print("change Z class base for Y ....")
#     Z.__bases__ = (Y,)   # 作用类似于让Z类继承Y类
#     z.m1()
#
#
# if __name__ == '__main__':
#     test_z()


# *************继承方法探究**********************
"""
能够在多继承中按照广度优先的继承树搜索关系链来有序地调用与父类相同名称的方法，且在每个子类拥有super的都会执行父类方法
"""

#
# class IA(object):
#     def __init__(self):
#         print("call IA init ...")  # 基类IA没有super()，没有意义
#
#
# class IB(IA):
#     def __init__(self):
#         print("call IB init ....")
#         super().__init__()
#
#
# class IC(IA):
#     def __init__(self):
#         print("call IC init ....")
#         super().__init__()
#
#
# class ID(IC, IB):
#     def __init__(self):
#         print("call ID init ...")
#         super().__init__()
#
#
# def test_ID():
#     d = ID()
#     print(ID.mro())
#
#
# if __name__ == '__main__':
#     test_ID()


# *******************************
"""
在父类没有使用super()情况下，在子类中将使用类的继承树搜索方式来匹配父类方法，找到并返回调用，不再继续往下搜索
"""


# class P1(object):
#     def __init__(self):
#         print("call P1 init ...")
#
#
# class P2(object):
#     def __init__(self):
#         print("call P2 init ...")
#
#
# # 以下两种方式等价
# # class S(P2, P1):
# #     pass  # 默认调用父类的构造方法,如果有定义的话并且子类没有调用super()将不会调用父类方法
#
#
# class S(P2, P1):
#     def __init__(self):
#         super().__init__()
#
#
# if __name__ == '__main__':
#     S()

