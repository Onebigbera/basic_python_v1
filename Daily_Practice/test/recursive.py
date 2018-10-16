# coding = utf-8
"""
    recursive : 递归函数
        所谓的函数递归调用，就是函数可以在其声明的执行顺序之中调用执行调用其自身。
        递归函数的好处： 精简执行过程中的重复调用。

"""


# 经典的递归函数求阶乘

def factorial_foo(n):
    if n == 0 or n == 1:
        return 1
    # else:
    #     return factorial_foo(n - 1) * n
    # 注意代码优化的原则
    return factorial_foo(n - 1) * n


result = factorial_foo(5)
print(result)


# 递归函数求和 计算从 1到 100的和


def sum_foo(n):
    if n == 1:
        return 1
    return n + sum_foo(n - 1)


sum_result = sum_foo(90)
print(sum_result)


# 递归函数归纳斐波那契数列
# 斐波那契数列:1,1,2,3,5,8...


def fib_foo(n):
    if n == 1 or n == 2:
        return 1
    return fib_foo(n - 1) + fib_foo(n - 2)


rabbits = fib_foo(5)
print(rabbits)

"""
    从古老的神话故事-黄金圆盘故事中抽象出来的递归问题
        重复调用类计算问题的思维惯性
    需求：将每一步具体的圆盘移动过程模拟出来
    三根柱子: a  b  c 
        一个圆盘  a --> b   将最小的圆盘从a移到b上
        两个圆盘  a --> c   a --> b    c --> b  将a移动到c过渡，将大盘移动到b 再将小盘移动到b
        三个圆盘  a --> b   a --> c    b --> c   a --> b  c --> a  c --> b  a --> b 
        ...
        抽象出来的模型:
        步骤分解:
        一根柱子放圆盘，其余两个柱子具有等效性
        三个圆盘 :
            将两个圆盘从a移动到c   将最大的圆盘移动到b  将两个圆盘从c移动到b
        四个圆盘
            将三个圆盘从a移动到c   将最大的圆盘移动到b  将三个圆盘从c移动到b
            ...
            将n-1个圆盘从a移动到c  将最大的圆盘移动到b  将n-1个圆盘从c移动到b
        
"""


def move_disk(n, a, b, c):
    if n == 1:
        # 将圆盘从a移动到b b为放最大盘(主盘)  c为过渡
        print('%s --> %s' % (a, b))
    elif n == 2:
        # 将n-1个圆盘移动到b
        print('%s --> %s' % (a, c))
        # 移动最大片的圆盘
        print('%s --> %s' % (a, b))
        # 将n-1个圆盘从b移动到c
        print('%s --> %s' % (c, b))
    else:
        # n-1移动到过渡盘
        move_disk(n - 1, a, c, b)
        move_disk(1, a, b, c)
        move_disk(n - 1, c, b, a)


# move_disk(1, 'a', 'b', 'c')
# move_disk(2, 'a', 'b', 'c')
# move_disk(3, 'a', 'b', 'c')


# move_disk(4, 'a', 'b', 'c')


# 优化代码 简洁
# 代码还可以优化:
def disk_move(n, a, b, c):
    if n == 1:
        print(a, "--->", c)
    else:
        # n-1 从a到b
        disk_move(n - 1, a, c, b)
        # 最大盘到c c为主盘
        disk_move(1, a, b, c)
        # n-1 从 b到c
        disk_move(n - 1, b, a, c)


disk_move(3, 'a', 'b', 'c')
