"""
stack:堆栈数据结构
"""
# 创建一个栈
# In [1]: s = []
# # 往栈内添加一个元素
# In [2]: s.append(1)
# In [3]: s
# Out[3]: [1]
# # 删除栈内的一个元素
# In [4]: s.pop()
# Out[4]: 1
# In [5]: s
# Out[5]: []
# # 判断栈是否为空
# In [6]: not s
# Out[6]: True
# In [7]: s.append(1)
# In [8]: not s
# Out[8]: False
# # 获取栈内元素的数量
# In [9]: len(s)
# Out[9]: 1
# In [10]: s.append(2)
# In [11]: s.append(3)
# # 取栈顶的元素
# In [12]: s[-1]
# Out[12]: 3
"""
需求：
    假如表达式中允许包含三中括号()、[]、{}，其嵌套顺序是任意的，例如：

正确的格式

{()[()]},[{({})}]
错误的格式

[(]),[()),(()}
编写一个函数，判断一个表达式字符串，括号匹配是否正确
思路

创建一个空栈，用来存储尚未找到的左括号；
便利字符串，遇到左括号则压栈，遇到右括号则出栈一个左括号进行匹配；
在第二步骤过程中，如果空栈情况下遇到右括号，说明缺少左括号，不匹配；
在第二步骤遍历结束时，栈不为空，说明缺少右括号，不匹配；
"""
# !/use/bin/env python
# _*_ coding:utf-8 _*_
LEFT = {'(', '[', '{'}  # 左括号
RIGHT = {')', ']', '}'}  # 右括号


def match(expr):
    """
    :param expr: 传过来的字符串
    :return: 返回是否是正确的
    """
    global brackets
    stack = []  # 创建一个栈
    for brackets in expr:  # 迭代传过来的所有字符串
        if brackets in LEFT:  # 如果当前字符在左括号内
            stack.append(brackets)  # 把当前左括号入栈
        elif brackets in RIGHT:
            pass  # todo
    if not stack or not 1 <= ord(brackets) - ord(stack[-1]) <= 2:
        # 如果当前栈为空，()]
        # 如果右括号减去左括号的值不是小于等于2大于等于1
        return False  # 返回False
        stack.pop()  # 删除左括号
    return not stack  # 如果栈内没有值则返回True，否则返回False


result = match('[(){()}]')
print(result)
