# coding utf-8
# list1 = []
# list2 = list1.append(10)
# print(list2)


# list3 = list2.append(123, [])
# list4 = list3.append('a')
# print(list4)
def extendlist(val, list=[]):
    list.append(val)
    return list


list1 = extendlist(10)
list2 = extendlist(123, [])
list3 = extendlist('a')
print(list3)  # [10, 'a']
