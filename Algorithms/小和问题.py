def smallSum(li,low,high):
    
    if low==high:
        return 0
    mid=(low+high)//2
    return smallSum(li,low,mid)+smallSum(li,mid+1,high)+merge(li,low,mid,high)

def merge(li,low,mid,high):
    l,r=low,mid+1
    result=[]
    sum=0
    while l<= mid and r<=high:
        if li[l]<li[r]:
            
            sum=sum+li[l]*(high-r+1)
            result.append(li[l])
            l+=1
        else:
            result.append(li[r])
            r+=1

    while r<=high:
        result.append(li[r])
        r+=1

    while l<=mid:
        result.append(li[l])
        l+=1
    for x in range(len(result)):
        li[x+low]=result[x]
    
    return sum

li=[1,3,4,2,5]
print(smallSum(li,0,4))

# def merge1(li,low,mid,high):
#     x=[]
#     sum=0
#     i,j=low,mid+1
#     while i<=mid and j<=high:
#         if li[i]<li[j]:
#             sum=sum+li[i]*(high-j+1)
#             x.append(li[i])
#             i+=1
#         else:
#             x.append(li[j])
#             j+=1
#     while i<=mid:
#         x.append(li[i])
#         i+=1
    
#     while j<=mid:
#         x.append(li[j])
#         j+=1
#     for a in range(len(x)):
#         li[low+a]=x[a]

#     return sum

# def sum1(li,low,high):
#     if low==high:
#         return 0
#     mid=(low+high)//2
#     return sum1(li,low,mid)+sum1(li,mid+1,high)+merge1(li,low,mid,high)
