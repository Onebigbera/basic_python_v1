# -*- coding:utf-8 -*-
"""
从本实例中可以看出代码实际运行的顺序和自己的猜测还是有去别的 :
    通过打断点发现，其运行顺序为: A-->B-->BASE-->B-->A 呈现出单线回路型执行
"""
class Base:
    def __init__(self):
        print('Base.__init__')


class A(Base):
    def __init__(self):
        super().__init__()
        print('A.__init__')


class B(Base):
    def __init__(self):
        super().__init__()
        print('B.__init__')


class C(A, B):
    def __init__(self):
        super().__init__()  # Only one call to super() here
        print('C.__init__')


c = C()

