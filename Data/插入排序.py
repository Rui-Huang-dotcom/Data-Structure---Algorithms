# def insert_sort(li):
#     for i in range(1, len(li)):
#         x = li[i]
#         j = i-1
#         while j >= 0 and li[j] > x:
#             li[j+1] = li[j]
#             j -= 1
#         li[j+1] = x
#         print(li)




# 简单
def insert_sort(li):
    for i in range(1,len(li)):
        x=li[i]
        while li[i-1]>x and i>=1:
            li[i]=li[i-1]
            i-=1
        li[i]=x


li = [3, 4, 2, 10, 5, 6, 8, 11, 9, 1]
insert_sort(li)
print(li)