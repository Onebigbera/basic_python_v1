"""
    protected variable 保护变量 以单下划线开头的变量叫做保护变量，只有类对象和子类对象才能访问到这些变量。
        _protected_attr


    private property 私有属性 私有成员，表示只有类对象自己能访问，连子类对象不能访问到这个数据
        __private_attr :
            <1> 两个下划线开头，声明该属性为私有，不能在内的外部被直接使用或者直接访问。
            <2> 在类内部的方法中使用时，使用self.__private_attr进行调用该私有属性。
        __private_method :
            <1> 使用两个下划线开头，声明该方法为私有方法，不能再类的外部调用。
            <2> 在类的内部调用时要用到self.__private_method方法

"""


class Girl(object):
    name = 'jerry'
    _age = 20
    __money = 500

    def __init__(self, name, age, money):
        # 公开属性
        self.name = name
        self._age = age
        # 私有属性
        self.__money = money

    # 定义共有方法
    @property
    def get_name(self):
        return self.name

    # 设置私有方法
    def __set_money(self, money):
        # 更改金钱属性
        self.__money = money

    # 设置公有方法设置私有方法
    def set_money(self, money):
        # 返回调用后的私有方法(函数)
        return self.__set_money(money)

    # 设置公有方法访问私有属性
    def get_money(self):
        print('money : %s' % self.__money)
        return '卡内金额:%s' % self.__money

    # 设置保护方法
    def _set_age(self, age):
        print('%s' % age)
        self._age = age

    # 通过公有方法设置保护方法
    def set_age(self, age):
        return self._set_age(age)

    # 通过公有方法访问保护属性
    def get_age(self):
        print('i am %s years old' % self._age)
        return self._age


if __name__ == '__main__':
    jinks = Girl('jinks', 18, 800)
    # 加了装饰器的公有方法
    print(jinks.get_name)
    jinks.get_money()
    # 更改了金额
    # jinks.set_money(600)
    # # 再次打印金额
    # jinks.get_money()

    # 能够执行 但是会隐形报错
    # jinks._set_age(50)
    # 公有方法设置保护方法
    jinks.set_age(60)
    jinks.get_age()
