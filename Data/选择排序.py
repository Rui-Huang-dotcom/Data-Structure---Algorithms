def select_sort(li):
    for i in range(len(li)-1):
        for x, y in enumerate(li):
            z = min(li[i:])
            if y == z:
                li[i], li[x] = li[x], li[i]
        print(li)


li = [3, 4, 2, 10, 5, 6, 8, 11, 9, 1]
# select_sort(li)
# print(li)


def select_sort_1(li):
    for i in range(len(li)-1):
        min_loc = i
        for j in range(i+1, len(li)):
            if li[j] < li[min_loc]:
                min_loc = j
        li[i], li[min_loc] = li[min_loc], li[i]


x = [3, 4, 2, 10, 5, 6, 8, 11, 9, 1]
select_sort_1(x)
print(x)

