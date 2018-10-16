"""
    *args 和 **kwargs 用法详解
    *   允许接收0个或者任意多个参数
    *args : Python中的可变参数，表示任意多个无名参数，类型为tuple;

    **kwargs : Python中的可变参数，表示关键字参数，类型为字典。
        ** 关键字参数允许你传入0个或者任意个含有参数名的参数，这些关键字在函数内部会自动组装成为一个字典。
        传参方式为: key = value 形式 如 ：a = 1
    使用原则一 : 使用时需将*args放在**kwargs之前，否则会有“SyntaxError: non-keyword arg after keyword arg”的语法错误


上面是在函数定义的时候写的*和**形式，那反过来，如果*和**语法出现在函数调用中又会如何呢？

他会解包参数的集合。例如，我们在调用函数时能够使用*语法，在这种情况下，它与函数定义的意思相反，他会解包参数的集合，而不是创建参数的集合。


"""


# 顺序传参
def foo(a, *args):
    # 将 args 和 *args的值和值的类型打印出来
    print(f'args:{args}; type:{type(args)}')
    # .format对于长度不限的参数会报错
    print('args:{}; type:{}'.format(args, type(args)))
    """
    # 可以将*args打印出来，但是将其用变量接收和迭代都会报SyntaxError
    # test = *args  # SyntaxError:can't use starred expression here
    # print(test)
    for i in *args:  # SyntaxError:invalid syntax
        print(i)
    """
    print(*args)
    print(*args[0])  # f d f
    # print(*args[1])  # TypeError: print() argument after * must be an iterable, not int
    print(*args[2])  # f d f


# foo(1, 'fdf', 5656, 'hello')


def calcal(*num):
    sum = 0
    for n in num:
        sum += n * n
    print(sum)


# 报错 can't multiply sequence by non-int of type 'list'  序列无法相乘
# 此时的参数为列表 自己无法相乘(相乘至少为两个因子)
# calcal([1, 2, 3, 4])
# 接收多个参数的 *args  此时参数为接收了多个元素
# calcal(1, 2, 3, 4, 5)


# **kwargs 使用案例


def key_foo(**kwargs):
    print(f'**kwargs:{kwargs}; type:{type(kwargs)}')  # {'a':1, 'b': 'hello'}  <class 'dict'>
    # print(**kwargs)           # TypeError: 'a' is an invalid keyword argument for this function


# key_foo(a=1, b='hello')


# 运行结果为 : {'a': 1, 'b': 'hello'} 明显可以看出 kwargs 在内部自动组装成为了{'a': 1, 'b': 'hello'}的字典

# *args 和 **kwargs 结合使用

def mix_use(a, *args, **kwargs):
    print(a, args, kwargs)


# 返回结果为: 1 ('a', 'hello', 'sex_lady' {'d': 'hello', 'e':2})
# mix_use(1, 'a', 'hello', 'sex_lady', d='hello', e=2)


# 定义一个人的函数
def person(name, age, **kwargs):
    print('name :%s ; age: %s; other:%s' % (name, age, kwargs))


# 注意关键字如何传参 返回结果为 ： name :Micheal ; age: 32; other:{'job': 'Engineer', 'home': 'USA', 'hobbit': 'drink'}
# person('Micheal', 32, job='Engineer', home='USA', hobbit='drink')

# *********在函数中使用，而非在函数定义中使用************
"""
上面是在函数定义的时候写的*和**形式，那反过来，如果*和**语法出现在函数调用中又会如何呢？

他会解包参数的集合。例如，我们在调用函数时能够使用*语法，在这种情况下，它与函数定义的意思相反，他会解包参数的集合，而不是创建参数的集合。 
"""


# 元祖解包 在元祖参数前加*
def func(a, b, c, d):
    print(a, b, c, d)


test_tuple = (1, 2, 3, 4)


# 需要在元祖前加上 * 代表传多个参数 解包参数 否则只当是一个参数 函数因子数量相等
# func(*test_tuple)


def cal(*num):
    sum = 0
    for n in num:
        sum += n * n
    print(sum)
    return sum


# 先解包:解包成多个元素对象，在被*args接收  先分解 再整合的思想
# cal(*test_tuple)


# 字典解包
def unlock_dict(name, **kwargs):
    print('name:%s; others:%s' % (name, kwargs))


info = {'job': 'account', 'age': 28, 'change': 500}
# 将字典关键字传入的方法 加**
unlock_dict('jerry', **info)
# 相当于将其解包为job=account,age=28,change=500
unlock_dict("mike", job='doctor', age=28, wife='marry')
#  也是先解包成字典(key=value)形式 再将字典整合传入
"""
    结论:
        在函数调用时，*会以单个元素的形式解包一个元祖，使其成为独立的参数。 --- 每一个元祖元素都是一个参数。
        在函数调用时，**会以key/value形式解包一个字典，使其中成为独立的关键字参数。--- 每一个键值对都是一个参数。
"""
