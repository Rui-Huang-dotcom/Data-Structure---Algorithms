nums=[2,0,2,1,1,0]
x=1

def a(nums):

    i,a,b,j=0,0,len(nums)-1,1
    while i<= b:
        if i<=b and nums[i]>j:
            nums[i],nums[b]=nums[b],nums[i]
            b-=1
        if i<=b and nums[i]<j:
            nums[i],nums[a]=nums[a],nums[i]
            a+=1
            i+=1
        if i<=b and nums[i]==j:
            i+=1
    return nums
   
print(a(nums))






    