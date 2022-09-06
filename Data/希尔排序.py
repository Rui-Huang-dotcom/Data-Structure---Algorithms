def insert_sort_gap(li,gap):
    for i in range(gap,len(li)):
        x=li[i]
        while i>=gap and x<li[i-gap]:
            li[i]=li[i-gap]
            i-=gap
        li[i]=x

def shell_sort(li):
    d=len(li)//2
    while d>=1:
        insert_sort_gap(li,d)
        d//=2

li = [3, 4, 2, 10, 5, 6, 8, 11, 9, 1]
shell_sort(li)
print(li)