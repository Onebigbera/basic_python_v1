"""
    当程序发生错误而我们并不希望程序停止时，这是我们就需要用到异常处理机制来实现。
    异常处理机制
    except ： 除去；除
        Format
            try：
                process
            except 错误类型 as e :
                process
            except 错误类型 as e :
                process
            except 错误类型 as e :
                process
            ...
            else:
                process
            finally:
                process (无论try语句是否由错误都会被执行的finally语句)

    python 中的错误就是class， 所有的错误都继承了BaseException类，我们在捕获吃的时候，它捕获了改类型的错误，并且还把它的子类一网打尽。
    有些错误无法捕获 比如说内存错误，如果我们想开辟一块新的内存空间，那就必须先释放一部分内存


"""

# 基本报错 捕捉错误
try:
    print(3 / 0)
except ZeroDivisionError as e:
    print('除数不能为零')
print('hello beautiful word!')

# 没有出错时 正常运行
try:
    print(3 / 1)
except ZeroDivisionError as e:
    print('ZeroDivisionError')
else:
    print('success worked')
finally:
    print('hello word')

# 程序中出现错误太多，也可以不使用任何错误代码,在except后面接多个异常
try:
    print(3 / 0)
except (NameError, ZeroDivisionError):
    print('程序异常')

# 可以直接捕获BaseException类 程序按照顺序从上到下执行
try:
    print(5 / 0)
except BaseException as e:
    print(e)
except ZeroDivisionError as e:
    print(e, 1)


# 跨越多层级调用
def func1(num):
    print(1 / num)


def func2(num):
    func1(num)


def main():
    func2(0)


try:
    main()
except ZeroDivisionError as e:
    print(e)
