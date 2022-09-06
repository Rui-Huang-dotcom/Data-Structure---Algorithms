li=[3,1,10,20,15,21,9,11,]

def getleast(li):
    if li[0]<li[1]:
        return li[0]
    elif li[-1]<li[-2]:
        return li[-1]
    else:
        l,r=0,len(li)-1
        while l<=r:
            mid=(l+r)//2
            if li[mid-1]>li[mid]<li[mid+1]:
                return li[mid]
            else:
                r=r-1

print(getleast(li))