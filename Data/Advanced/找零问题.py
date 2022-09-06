dict={}
nums=[100,50,20,5,1]

def charge(nums,money):
    for i in nums:
        
        dict[i]=money//i
        money=money%i
    return max(dict.keys(),key=dict.get)

print(charge(nums,356))  
