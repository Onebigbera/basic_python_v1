# 冒泡排序

'''
原理
冒泡排序(Bubble Sort)是一种简单的排序算法。它重复地走访过要排序的数列，一次比较两个元素，
如果他们的顺序错误就把他们交换过来。走访数列的工作是重复地进行直到没有再需要交换，
也就是说该数列已经排序完成。这个算法的名字由来是因为越小的元素会经由交换慢慢“浮”到数列的顶端。

步骤
冒泡排序算法的运作如下：

比较相邻的元素。如果第一个比第二个大，就交换他们两个。
对每一对相邻元素作同样的工作，从开始第一对到结尾的最后一对。这步做完后，最后的元素会是最大的数。
针对所有的元素重复以上的步骤，除了最后一个。
持续每次对越来越少的元素重复上面的步骤，直到没有任何一对数字需要比较。
'''
def bubble_sort(array):
    length = len(array)
    for i in range(length-1):
        for j in range(length-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array
print(bubble_sort([3,1,4,2]))


# 选择排序
'''
原理
选择排序（Selection sort）是一种简单直观的排序算法。 它的工作原理大致是将后面的元素最小元素一个个取出然后按顺序放置。

步骤
在未排序序列中找到最小（大）元素，存放到排序序列的起始位置，
再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾。
重复第二步，直到所有元素均排序完毕。
'''
def select_sort(array):
    length = len(array)
    for i in range(length):
        min_index = i
        for j in range(i+1, length):
            if array[j] < array[min_index]:
                min_index = j
        array[min_index], array[i] = array[i], array[min_index]
    return array
print(select_sort([3,1,4,2]))



# 快速排序
'''原理
快速排序使用分治法（Divide and conquer）策略来把一个序列（list）分为两个子序列（sub-lists）。

步骤
从数列中挑出一个元素，称为”基准”（pivot），
重新排序数列，所有元素比基准值小的摆放在基准前面，
所有元素比基准值大的摆在基准的后面（相同的数可以到任一边）。
在这个分区结束之后，该基准就处于数列的中间位置。这个称为分区（partition）操作。
递归地（recursive）把小于基准值元素的子数列和大于基准值元素的子数列排序。
'''
def quick_sort(array):
    if len(array) < 2:
        return array
    pivot = array[0]
    less = [i for i in array[1:] if i <= pivot]
    greater = [i for i in array[1:] if i > pivot]
    return quick_sort(less) + [pivot] + quick_sort(greater)

print(quick_sort([3,1,2,4]))




# 插入排序
'''
原理
插入排序（Insertion Sort）是一种简单直观的排序算法。它的工作原理是通过构建有序序列，
对于未排序数据，在已排序序列中从后向前扫描，找到相应位置并插入。

步骤
从第一个元素开始，该元素可以认为已经被排序
取出下一个元素，在已经排序的元素序列中从后向前扫描
如果该元素（已排序）大于新元素，将该元素移到下一位置
重复步骤3，直到找到已排序的元素小于或者等于新元素的位置
将新元素插入到该位置后
重复步骤2~5
'''
def insert_sort(array):
    length = len(array)
    for i in range(1, length):
        temp = array[i]
        j = i-1
        while j >=0 and array[j] > temp:
            array[j+1], array[j] = array[j], temp
            j -= 1
    return array
print(insert_sort([3,1,4,2]))