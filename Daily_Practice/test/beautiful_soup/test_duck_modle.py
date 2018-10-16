# -*- coding:utf-8 -*-
"""
当看到一只鸟走起来像鸭子、游泳起来像鸭子、叫起来也像鸭子，那么这只鸟就可以被称为鸭子.
我们并不关心对象是什么类型，到底是不是鸭子，只关心行为、只关心行为！！
在python中，有很多file-like的东西，比如StringIO,GzipFile,socket。它们有很多相同的方法，我们把它们当作文件使用。
多个类 有相同的方法 按照特定的对象(类)去处理  将鸡、鸭子、鸟儿、大鹅都按照鸭子的方法去处理
"""
__author__ = 'george'
__date__ = '2018/10/4'


class Duck(object):
    def quack(self):
        print(' i am a duck')


class Bird(object):
    def quack(self):
        print(' i am a bird')


class Dog(object):
    def quack(self):
        print(' i am a dog')


def in_the_forest(duck):
    duck.quack()

duck = Duck()
bird = Bird()
dog = Dog()
[in_the_forest(x) for x in [duck, bird, dog]]
