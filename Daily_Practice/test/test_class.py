# -*- coding: utf-8 -*-  
__author__ = 'zhougy'
__date__ = '2018/9/20 下午2:53'

'''
类：属性，方法

属性：数据
按照数据所有者分类
    ---- 对象成员数据（self）
    ---- 类成员数据 (静态成员数据，类成员数据 Class)

'''


class People(object):
    counter = 0

    def __init__(self, name, age=20):
        self._name = name
        self.__age = age
        # 每次初始化的时候计算器加1
        People.counter += 1

    def eat(self):
        print(f"total {self.counter} go to eat")

    # 将方法变成属性使用
    @property
    def get_age(self):
        return self.__age

    # 对mage方法的设置
    @get_age.setter
    def set_age(self, age):
        if not isinstance(age, int):
            raise Exception('your input is not int.')
        if age > 100 or age < 0:
            raise Exception("你输入的年龄不符合")
        # 不用return ？？？为啥 相当于在mage前检验 由mage方法返回
        self.__age = age

    # 类方法 传入类 拥有类的属性
    @classmethod
    def go_fun(cls):
        print(f"today, we has {cls.counter} peple go to fun.")

    # 静态方法 不用传入参数 相当于独立的方法 可以调用类的属性和方法
    @staticmethod
    def play():
        print(f"today, we have {People.counter} people go to play")


class Star(People):

    def __init__(self, name, age, jiemu):
        """
        继承People类的Start类
        """
        # super().__init(name, age)
        People.__init__(self, name, age)
        self.__jiemu = jiemu

    def perform(self):
        print(f"{self._name} 开始表演 {self.__jiemu}！")


star_list = [
    ('刘德华', 50, '忘情水'),
    ('梁朝伟', 52, '演戏'),
    ('沈腾', 38, '搞笑'),
]

# 多用列表推导式  遍历列表中的元祖 注意遍历格式 元素数量对应
p_list = [Star(star_name, age, jiemu) for (star_name, age, jiemu) in star_list]

print(f"今天总共邀请了 {Star.counter} 个明星")

# 调用perform方法
[p.perform() for p in p_list]
if __name__ == '__main__':
    tom = People('tom', 20)
    # method.setter用法报错！！两次都报错
    tom.set_age(-2)
    print(tom.get_age)
