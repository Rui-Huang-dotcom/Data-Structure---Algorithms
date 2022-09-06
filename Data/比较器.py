import functools
class Student():
    def __init__(self,name,age,classnum) :
        self.name=name
        self.age=age
        self.classnum=classnum
    def __str__(self) :
        return self.name
	# 年龄按照从小到大排序
    # 第一个参数在前
    def sort_age(a,b):
        return a.age-b.age
	    # 先按照班级排好，再按照年龄从大到小排好  
    def class_and_age(a,b):
        if a.classnum!=b.classnum:
            return a.classnum-b.classnum
        return b.age-a.age
    

a=Student('111',19,3)
b=Student('222',20,2)
c=Student('333',31,1)

res=[a,b,c]
for i in res:
    print('before',i)
print('-----------------------------'*2)
res=sorted(res,key=functools.cmp_to_key(Student.sort_age))
for i in res:
    print('after',i)
print('-----------------------------'*2)
res=sorted(res,key=functools.cmp_to_key(Student.class_and_age))
for i in res:
    print('after2',i)

