"""
    python中type除了能够返回给予对象的类型外，还有什么其他功能呢？？
"""


class Person(object):
    def __init__(self):
        pass


person = Person()
print(type(person))  # <class '__main__.Person'>
print(type(Person))  # <class 'type'>
"""
  我们使用了class定义了类，然后实例化person
  观察person的类型，它的类型指向Person
  那么Person的类型呢？居然是指向type!!!
  猜测:Person类是由type来定义的？？
"""
Per = type('Person', (), {'author': 'fighter'})
print(Per.author)  # fighter
print(type(Per))  # <class 'type'>

"""
  可以看大，type需要三个函数,可以理解为:
  第一个参数: 类名，
  第二个参数: 继承，
  第三个参数: 私有化
  但是当定义有私有函数呢？

"""


def func(name):
    print(f'name:{name}')


stu = type('Student', (), {'name': func})
stu.name('tom')
"""
  通过先定义函数，然后再用type定义类
  其中:name为私有函数名
  那么问题又来了，如何继承呢？？
"""
human = type('Human', (object,), {'age': 20})
man = type('Man', (human,), {'age': 21})
print(man.age)
print(type(man))  # <class 'type'>
"""
注意看第二个继承的不是Human ,而是'实例化的'human,其类型为type
"""
