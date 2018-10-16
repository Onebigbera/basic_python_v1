# _*_ coding:utf-8 _*_
"""
 Thread: 线程
 进程：
    程序运行的基本单元，最小单位。

 线程：

 协程：


"""

# 进程示范
from multiprocessing import Process
import time
import random


def talk(name):
    print('%s is talking' % name)
    time.sleep(random.randint(1, 3))
    print('%s has finished his talk ' % name)


# window系统中，起进程的操作一定要放在main函数中
if __name__ == "__main__":
    # 获取进程实例
    p1 = Process(target=talk, args=('Alex',))
    p2 = Process(target=talk, args=('Tom',))
    p3 = Process(target=talk, args=('Mike',))
    p4 = Process(target=talk, args=('Rich',))

    # 将每个单独的线程放进列表中
    p_list = [p1, p2, p3, p4]
    # 遍历列表
    for p in p_list:
        p.start()

    # 主进程只有在各个子进程结束完毕后，才会向下执行
    for p in p_list:
        p.join()

"""
    演示一个对比加锁和不加锁对进程影响的案例
"""
import threading
import time

# 实例化锁对象
lock = threading.Lock()
num = []


# 加了进程锁的函数
def test1(n):
    # 让锁生效
    lock.acquire()
    # 向列表中添加
    num.append(n)
    print(num)
    # 开锁 锁释放
    lock.release()


# 不加进程锁的函数
def test(n):
    num.append(n)
    print(num)


def main():
    for i in range(10):
        # 执行不加锁的程序
        # th = threading.Thread(target=test, args=(i,))
        # 执行加了锁的程序
        th = threading.Thread(target=test1, args=(i,))
        th.start()


if __name__ == '__main__':
    main()
