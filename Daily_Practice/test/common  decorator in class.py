"""
面向对象中常见的几种装饰器
    @property
        内置 该装饰器会把对象的方法变为属性来调用
    注意: 第一个age(self)是get方法，用@property装饰，@get_age(self, age)是set方法，用@get_age.setter装饰器，注意用此两个装饰器装饰的函数名称必须一致
    @get_age.setter是前一个@property装饰器的副产品，而且是在调用get_age函数时才会起作用。

    @staticmethod
        功能：
            将被装饰的函数从类中分离出来，该函数不能访问类的属性，简单的说可以将函数理解为一个独立的函数，不允许使用.self。
            @staticmethod 就是将该被装饰的函数与类脱离关系，该函数不能用self 传参，需要和普通函数一样传参。
            @staticmethod 既可以有实例化的对象来调用，也可以由对象来调用

    @classmethod
        被@staticmethod装饰的函数既可以被类调用也可以被对象调用
        class C:
          @classmethod
          def f(cls, arg1, arg2, ...):
              ...

    It can be called either on the class (e.g. C.f()) or on an instance
    (e.g. C().f()).  The instance is ignored except for its class.

"""


class Student(object):

    def __init__(self, name, age, major):
        self.name = name
        # __attr 保护属性   &&  _attr私有属性
        self._age = age
        self.major = major

    @property
    def get_age(self):
        return self._age

    #  没进入 get_age.setter函数  setter方法未生效
    @get_age.setter
    def get_age(self, age):

        # 验证输入的age类型  isdigit()检查字符串是否只由数字组成
        if isinstance(age, int):
            self._age = age
            return
        if isinstance(age, str) and age.isdigit():

            self._age = int(age)

        else:
            raise ValueError("age is illegal")

    # 删除_age
    @get_age.deleter
    def get_age(self):
        del self._age

    def get_name(self, name):
        self.name = name
        return name

    @staticmethod
    def have_breakfast(name, food):
        print('%s is having his breakfast %s' % (name, food))

    @classmethod
    def learning(cls):
        print('jack is learning hard')


# class Bar(object):
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age


"""
__repr__  用于显示对象的内存地址  面向程序员  如果想在所有环境下都统一显示的话，可以虫偶__repr__方法
__str__   用于显示对象的内存地址  面向用户

"""

# 专有方法
# def __str__(self):
#     print('this str')
#     return '名称为%s age%s' % (self.name, self.age)


# repr 代理人 字符串 打印对象的内存地址
# def __repr__(self):
#     print('this repr')
#     return '%s %d' % (self.name, self.age)


if __name__ == '__main__':
    #  实例化对象
    tom = Student(name='tom', age=30, major='python')
    # 调用get_age 方法 重新设置对象的年龄 这时就会调用装饰器@get_age.setter
    tom.get_age = '21'

    # @staticmethod 用法
    # 直接传参，不需要self介入
    # 通过实例化的对象调用
    tom.have_breakfast('jack', 'bread')
    # 通过类调用
    Student.have_breakfast('Marry', 'noodles')

    # @classmethod 方法使用
    # 通过实例化的对象调用
    tom.learning()
    # 通过类调用
    Student.learning()
    print(tom.get_age)

    # jack = Bar('jack', 18)
    # print(jack)
    # print(jack.__repr__())
    # print(repr(jack))


# method classmethod staticmethod

class Test(object):
    x = 123

    def __init__(self):
        self.y = 456

    def bar1(self):
        print('Hello world')

    @classmethod
    def bar2(cls):
        print('Bad world')

    @staticmethod
    def bar3():
        print('=========')

    def foo1(self):
        print(self.x)
        print(self.y)
        self.bar1()
        self.bar2()
        self.bar3()

    @classmethod
    def foo2(cls):
        print(cls.x)
        print(cls.y)
        cls.bar1()
        cls.bar2()
        cls.bar3()

    @staticmethod
    def foo3(obj):
        print(obj.x)
        print(obj.y)
        obj.bar1()
        obj.bar2()
        obj.bar3()


if __name__ == '__main__':
    t = Test()
    t.foo1()
    t.foo2()
    # t.foo3()
