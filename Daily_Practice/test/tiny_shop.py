"""
    字典是python中用到最多而且最领灵活的数据类型，灵活运行字典储存数据能够增加数据的处理效率和优化程序。

"""

"""
项目需求:
    1.启动程序时，用户输入零钱，打印商品列表
    2.用户通过商品编号购买商品
    3.用户选择商品后，系统会根据用户余额是否充足来显示对应消息或者继续购买
    4.用户可以随时退出购买系统终止购买,打印用户购买消费情况
"""

# 储存商品信息的字典
commodities = {
    'Time': 1,
    'Love': 1,
    'Health': 1,
    'Great personality': 1,
    'Knowledge': 1,
    'Persist': 1,
    'Friendship': 1,
    'Brave': 1,
    'End': 0,

}
# 得到商品和商品价格的对应关系的列表 将字典类型数据转换为列表类型列表中的元素为元祖 [('Time',1),('Love',1),('Health',1)...('Brave',1)]
commodity_list = list(commodities.items())


def show_purchase():
    # 打印多行
    print("""
    *********欢迎来到有穷商店*********
    1.%s  %s
    2.%s  %s
    3.%s  %s
    4.%s  %s
    5.%s  %s
    6.%s  %s
    7.%s  %s
    8.%s  %s
    9.%s  %s
    *********欢迎您再次光临**********
    """ % (commodity_list[0][0], commodity_list[0][1],
           commodity_list[1][0], commodity_list[1][1],
           commodity_list[2][0], commodity_list[2][1],
           commodity_list[3][0], commodity_list[3][1],
           commodity_list[4][0], commodity_list[4][1],
           commodity_list[5][0], commodity_list[5][1],
           commodity_list[6][0], commodity_list[6][1],
           commodity_list[7][0], commodity_list[7][1],
           commodity_list[8][0], commodity_list[8][1],
           ))





def purchase():
    # 启动购买系统
    while True:
        change = eval(input("请输入你的零钱: "))
        if change <= 0:
            print('余额不足，请充值！')
            # 余额不足 跳到充值界面
            break
        else:
            # 定义初始单个商品价格
            # single_price = 0
            # 定义总消费
            total_cost = 0
            while total_cost < change:
                order = eval(input('请输入商品购买序号: '))
                # 用户输入退出键 购买过程终止
                if order == 9:
                    break
                else:
                    if change - total_cost < commodity_list[order - 1][1]:
                        # 余额不足 购买强迫终止
                        break
                    # 余额充足 继续购买
                    else:
                        total_cost += commodity_list[order - 1][1]
            print('尊敬的客户，你本次一共消费%s人生币 ,还剩%s人生币 ，欢迎你下次光临！' % (total_cost, (change - total_cost)))


if __name__ == "__main__":
    show_purchase()
    purchase()
