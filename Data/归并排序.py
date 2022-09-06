#nlogn
def merge_sort(li,low,mid,high):
    i,j=low,mid+1
    ltmp=[]
    while i<=mid and j<=high:
        if li[i]<li[j]:
            ltmp.append(li[i])
            i+=1 
        else:
            ltmp.append(li[j])
            j+=1
    while i<=mid:
        ltmp.append(li[i])
        i+=1
    while j<=high:
        ltmp.append(li[j])
        j+=1
    li[low:high+1]=ltmp
    

li=[1,3,8,2,4]
merge_sort(li,0,2,4)
print(li)

def merge(li,low,high):
    if low<high:
        mid=(low+high)//2
        merge(li,low,mid)
        merge(li,mid+1,high)
        merge_sort(li,low,mid,high)


merge(li,0,len(li)-1)
print(li)

