# -*- coding: utf-8 -*-
"""
    正常境况下，当我们定义了一个class，创建了一个class的实例对象后，我们可以给该实例绑定任何属性和方法，这就是动态与语言的灵活性。
    但是当我们想要限定Student的属性怎么办？比如:只允许对Student限制只能添加girlfriend和parents属性？
    为了达到限制的目的，python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该class的能添加的属性
    使用了__slots__方法后，可以大大节省该对象所占用的空间  减少内存消耗
    如果不是使用普通语句访问属性，可以使用以下函数 -


- getattr(obj，name [，default]) - 访问对象的属性。
- hasattr(obj，name) - 检查属性是否存在。
- setattr(obj，name，value) - 设置一个属性。如果属性不存在，那么它将被创建。
- delattr(obj，name) - 删除一个属性。

下面是一此使用示例 -

    hasattr(emp1, 'salary')    # Returns true if 'salary' attribute exists
    getattr(emp1, 'salary')    # Returns value of 'salary' attribute
    setattr(emp1, 'salary', 7000) # Set attribute 'salary' at 7000
    delattr(emp1, 'salary')    # Delete attribute 'salary'



"""

__author__ = 'gorge'
__date__ = '2018/9/5'


class Student(object):
    # 将变量自带的和能够扩展的属性和方法都限制在__slots__对应的元祖中
    __slots__ = ('girlfriend', 'hobbit', 'name', 'age', 'action')

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        print(f'{self.name} is running ')


if __name__ == '__main__':
    tom = Student('tom', 23)
    # 动态添加属性
    tom.girlfriend = 'Lila'
    # 动态绑定方法 将其方法对象赋值给绑定的方法对象
    # tom.friend = 'gorge' # Student has no attribute 'friend'
    tom.action = tom.run
    # 打印tom的女朋友
    print(tom.girlfriend)
    # 让tom行动
    tom.action()
print(__name__)

# @property 装饰器使用
# class Student(object):
#
#     @property
#     def score(self):
#         return self._score
#
#     @score.setter
#     def score(self, value):
#         if not isinstance(value, int):
#             raise ValueError('score must be an integer!')
#         if value < 0 or value > 100:
#             raise ValueError('score must between 0 ~ 100!')
#         self._score = value
#
# tom = Student()
# tom.score = 60
# print(tom.score)
# jack = Student()
# # 超过setter范围的分数
# # jack.score = 200
# # print(jack.score)
# print(tom.__dict__)  # 包含该类的命名空间的字典
# print(tom.__doc__)   # 文档说明字符串
# print(Student.__name__) # 类名
# print(Student.__module__) # 定义类的模块名称
# print(Student.__bases__) # 一个包含基类的空元祖，按照它们在基类列表中出现的顺序

# 重载运算符

class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return 'Vector (%d, %d)' % (self.a, self.b)

    def __add__(self, other):
        # 返回一个实例化的对象
        return Vector(self.a + other.a, self.b + other.b)


v1 = Vector(2, 10)
v2 = Vector(5, -2)
print(v1 + v2)
