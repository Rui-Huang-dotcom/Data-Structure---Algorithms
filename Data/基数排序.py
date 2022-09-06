def radix_sort(li):
    max_mum=max(li)
    i=0
    while 10 ** i <= max_mum:
        buckets=[[] for _ in range (10)]
        for var in li:
            j=(var//10 ** i)%10
            
            buckets[j].append(var)

        li.clear()
        for buc in buckets:
            li.extend(buc)

        i+=1

li=[45,14,42,49,26,74]
radix_sort(li)
print(li)
