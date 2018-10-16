"""
polymorphic    多态
    继承person类的man、woman、gay等类展现出了不同的形态，这就叫多态。
binding        动态绑定
    子类复写的父类的方法，子类对象在调用它的时候会调用离它最近的方法，就叫动态绑定。

"""

"""
需求:
    面向对象的思维实现以下:
    <1> 构建写一个英雄的类，并为其赋予战斗和防守的方法
    <2> 分别构建战士、法师、射手的类 重写对应的战斗和防守的方法
    <3> 构建一直军队 并且用命令控制自己的军队
    
"""


# 创建Hero类
class Hero(object):

    def __init__(self, name):
        self.name = name

    def attack(self):
        print('英雄进攻')

    def defend(self):
        print('英雄防守')


class Tank(Hero):

    # 重写构造方法 添加
    def __init__(self, name, corporeity):
        # 从父类对象选择性继承name
        super().__init__(name)
        self.corporeity = corporeity

    def attack(self):
        print('蒙多想去哪儿就去哪儿')

    def defend(self):
        print('蒙多觉得你是个大娘们,%s' % self.corporeity)


class Wizard(Hero):

    def __init__(self, name, magic):
        super().__init__(name)
        self.magic = magic

    def attack(self):
        print('知识来源于分解，小心%s' % self.magic)

    def defend(self):
        print('遍地的哀嚎之声')


class Archer(Hero):

    # rewrite the construction method
    def __init__(self, name, weapon):
        super().__init__(name)
        self.weapon = weapon

    def attack(self):
        print('我的%s 可不会手下留情的' % self.weapon)

    def defend(self):
        print('小心！瞄准')


if __name__ == '__main__':
    army = []
    # 实例化军队各个兵种
    tank = Tank('蒙多', '振奋铠甲')
    wizard = Wizard('黑暗小法师', '能量爆裂')
    archer = Archer('皮城女警', '狙击枪')
    # 将各个展示添加到对应规模中去
    army.append(tank)
    army.append(wizard)
    army.append(archer)

    # 接收军队指令
    command = input('请输入进军指令:')
    if command == 'The army attack':
        for hero in army:
            hero.attack()
    elif command == 'Tank Defend':
        for hero in army:
            if isinstance(hero, Tank):
                hero.defend()
    elif command == 'Show your magic ! Wizard':
        for hero in army:
            if isinstance(hero, Wizard):
                hero.attack()
    elif command == 'Snipe your enemy':
        for hero in army:
            # isinstance : 用来判断对象是否属于哪一类 此处用来判断对象是否为类的实例
            if isinstance(hero, Archer):
                hero.attack()
    else:
        print('Unknown Command')
