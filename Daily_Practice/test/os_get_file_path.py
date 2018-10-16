"""
    os模块常用方法和一个具体应用实例


"""
import os

# 获取当前工作目录的绝对路径  get current working directory   | F:/pycharm/pycharm_code/Daily_Practice/test
print(os.getcwd())

# os.listdir(path)  返回一个指定的文件夹包含的文件和文件夹的名称的列表
print(os.listdir(os.getcwd()))

# 获取文件的绝对路径
# os.path.abspath(file_name)

# 判断一个路径是否存在 返回Boolean
# os.path.exists(path=path)

# 判断是否为文件夹 返回Boolean
# os.path.isdir()

# 判断对应路径下是否为文件 返回Boolean
# os.path.isfile(path=path)

#  遍历目录树
# os.walk()

# 应用场景
"""
需求：
    遍历指定的文件夹，并且找出改文件夹下所有的.py模块
"""

# 设置要查询的路径 按照规范命名
FILE_PATH = 'F:/Pycharm/pycharm_code/Daily_Practice'


# 并不完善 要查找的文件路径不够灵活
def getfile(dirname):
    # 得到目录下面的文件和目录的列表
    file_list = os.listdir(dirname)
    # 定义一个接收py文件的列表
    PYFileList = []
    # 遍历目标目录的下一级文件 | 得到 文件 和 目录
    for name in file_list:
        # 拼凑出文件的路径 | 字符串拼接的方法
        filepath = FILE_PATH + '/' + name
        # 判断该路径对应的是否为文件 并且是否是.py文件
        if os.path.isfile(filepath) and name.endswith('.py'):
            # 将该py模块添加到文件夹中
            PYFileList.append(name)
        # 如果是不是以.py结尾的文件
        elif os.path.isfile(filepath) and not name.endswith('.py'):
            print('这不是个py模块')
        # 如果路径对应为一个目录
        elif os.path.isdir(filepath):
            # 将目录中存在的py模块添加到存放模块的列表中
            # 这样去理解 编程就是从右往左看
            # PYFileList = getfile(filepath) + PYFileList
            PYFileList += getfile(filepath)
    # 返回存放py模块的列表 函数返回什么很重要 递归函数
    return PYFileList


pyfiles = getfile(FILE_PATH)
for file in pyfiles:
    print(file)
