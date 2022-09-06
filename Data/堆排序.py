def sift(li, low, high):
    """_summary_

    Args:
        li (_type_): _列表_
        low (_type_): _堆的根结点位置_
        high (_type_): _对的最后一个元素的位置_
    """
    i = low  # i是最开始的根结点
    j = 2*i+1  # j是左孩子 右孩子 2*i+2 父 (i-1)//2
    tmp = li[low]  # 存堆顶
    while j <= high:  # 当j存在时
        if j+1 <= high and li[j+1] > li[j]:  # 如果右孩子存在且大于左孩子
            j += 1  # j指向右孩子
        if li[j] > tmp:
            li[i] = li[j]
            i = j  # 往下走
            j = 2*i+1
        else:
            li[i] = tmp
            break
    else:
        li[i] = tmp 


def heap_sort(li):
    for i in range((len(li)-2)//2, -1, -1):
        print(i)  # i是建立堆时堆的调整的部分跟的下标
        sift(li, i, len(li)-1)  # 堆建立完成
    for i in range(len(li)-1, -1, -1):  # i指向当前堆的最后一个元素
        li[0], li[i] = li[i], li[0]
        sift(li, 0, i-1)  # i-1是新的high


x = [10, 9, 8, 6, 5, 4, 3, 1, 2]
x.append(11)
for i in range((len(x)-2)//2, -1, -1):
        print(i)  # i是建立堆时堆的调整的部分跟的下标
        sift(x, i, len(x)-1)
        print(x)

# import heapq
# heapq.heapify(x)
# print(x)
# for i in range(len(x)-1):
#     print(heapq.heappop(x),end=',')