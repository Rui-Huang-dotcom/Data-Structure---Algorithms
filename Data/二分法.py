def binary_search(li,val):
    l=0
    r=len(li)-1
    while l<=r:
        mid=(l+((r-l)>>1)) #！！！！！！！！！！！！！！！！！！！！！！
        if li[mid]==val:
            return mid
        elif li[mid]<val:
            l=mid+1
        else:
            r=mid-1
    
    return -1

x=[0,1,2,4,5,6,7]
print(binary_search(x,7))


