goods=[(60,10),(100,20),(120,30)]
goods.sort(key=lambda x:x[0]/x[1],reverse=True)

def fractional_backpack(goods,w):
    dict={}
    for i, (prize,weight) in enumerate(goods):
        if w>= weight:
            dict[prize]=1
            w-=weight
        else:
            dict[prize]=w/weight
            break
    return dict

print(fractional_backpack(goods,50))
print(1)