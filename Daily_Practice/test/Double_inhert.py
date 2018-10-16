"""
单独的.py文件就是一个模块
有多个.py文件和__init__.py文件组成的集体就是模块，在__init__.py文件未创建之前，导入出错
多个模块组成的功能集合称之为框架
"""
from test.practice import Person


class Man(Person):

    def tell(self):
        print('一点寒芒先到，随后抢出如龙！我乃%s，今年%s了！' % (self.name, self.age))

    def roar(self):
        print('即使敌众我寡，末将也能从万军丛中取敌将首级！')


class Woman(Person):

    def tell(self):
        print('断剑重铸之日，骑士归来之时,我乃{},年芳{}'.format(self.name, self.age))

    def cute(self):
        print('我也是需要人关怀的嘛！')


# 定义一个继承两个类的类
class Gay(Man, Woman):
    pass


if __name__ == '__main__':
    man = Man('赵信', 32, 1000)
    man.tell()
    man.roar()

    woman = Woman('瑞文', 18, 10000)
    woman.tell()
    woman.cute()

    # 继承了Man&Woman两个类的类同时具有了两个类的方法，所以其既能咆哮，也能撒娇！& 如果两个类中拥有相同的方法，则会按照顺序继承。
    gay = Gay('库克', 56, 12145)
    gay.tell()
    gay.roar()
    gay.cute()
