class Student(object):
    def __init__(self,id,name,age):
        self.id=id
        self.name=name
        self.age=age
 
    def __str__(self):
        return "学号:{}--姓名:{}--年龄{}".format(self.id,self.name,self.age)
    __repr__ = __str__
    
    '''
    __repr__ = __str__ 使用时可保证在控制台>>> print() 时 任然输出
    学号:111--姓名:Bob--年龄18
    '''
 
s=Student(111,"Bob",18)
print(s)


class S():
    def __init__(self,name,age,classnum) :
        self.name=name
        self.age=age
        self.classnum=classnum
    def __str__(self) -> str:
        return self.name
    def sort_age(a,b):
        return a.age-b.age
    def class_and_age(a,b):
        if a.classnum!=b.classnum:
            return a.classnum-b.classnum
        return b.age-a.age


 
    