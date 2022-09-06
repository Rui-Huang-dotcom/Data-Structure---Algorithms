a=[[1,4],[3,5],[0,6],[5,7],[3,9],[5,9],[6,10],[8,11],[8,12],[2,14],[12,16]]
d=[]
for i in range(len(a)-1):
    # b=[]
    # c=a[i]
    # b.append(c)
    # while i<(len(a)-1):

    #     if a[i+1][0]>c[1]:
    #         b.append(a[i+1])
    #         c=a[i+1]
    #     else:
    #         i+=1
    # if d==[]:
    #     d.append(b)
    # elif len(b)>len(d[0]):
    #     d.pop()
    #     d.append(b)
    d=[a[0]]
    for i in range(1,len(a)):
        if a[i][0]>=d[-1][1]:
            d.append(a[i])
print(d)
# x=(d.sort(key=lambda x:len(x)))
# print(x)