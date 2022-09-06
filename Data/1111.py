import collections
s = ( "bananas")
dict=collections.Counter(s)
print(dict)
li=list(dict.values())
li.sort(reverse=True)
x,y=0,0
for i in li:
    if i % 2!=0:
        x+=i-1
        y=1
    elif i % 2 == 0:
        x+=i
print(x+y)


    
        
                        

