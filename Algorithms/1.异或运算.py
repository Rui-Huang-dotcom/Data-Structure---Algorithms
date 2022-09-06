
# x,y=2,3
# print(x)
# print(y)

# # 异或运算交换两个变量
# x=x^y
# y=x^y
# x=x^y
# print(x)
# print(y)
# 异或运算的性质
# 1. 0^n=n n^n=0
# 2. a^b=b^a

# 找出一组数中一个出现奇数次的数
x=[3,2,3,3,3,3,1,2]
a=0
for i in x:
    a^=i
print(a)
b=0
for i in x:
    c=(bin(i))
    if int(c[-1])==1:
        b^=i
print(b)
print(str(a^b)+" "+str(b))





