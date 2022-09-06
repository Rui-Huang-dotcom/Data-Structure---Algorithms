def count_sort(li,max_count=13):
    count = [0 for _ in range(max_count+1)]
    for val in li:
        count[val]+=1
    li.clear()
    for ind,val in enumerate(count):
        for i in range(val):
            li.append(ind)

li=[11,2,4,4,4,5,1,2,5]
count_sort(li)
print(li)