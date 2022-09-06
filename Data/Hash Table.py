from re import S
class ListNode:
    def __init__(self,elem) :
        self.elem=elem
        self.next=None

class SingleLinklist:
    def __init__(self,node=None) :
        self.__head=node

    def is_empty(self):
        return self.__head==None

    def travel(self):
        a=self.__head
        b=[]
        while a != None:
            b.append(a.elem)
            a=a.next       
            print(b)
                        
        
    def length(self):
        count=0
        a=self.__head
        while a!=None:
            count+=1
            a=a.next
        return count

    def add(self,item):
        """头插法"""
        a=ListNode(item)
        if self.is_empty():
            self.__head=a
        else:
            a.next=self.__head
            self.__head=a

    def append(self,item):
        """尾插法"""
        b=ListNode(item)
        if self.is_empty():
            self.__head=b
        else:
            a=self.__head
            while a.next!=None:
                a=a.next
            a.next=b
    def __repr__(self):
        return str(self.travel())
    def insert(self,pos,item):
        if pos<=0:
            self.add(item)
        elif pos>(self.length()-1):
            self.append(item)
        else:
            count=0
            a=self.__head
            i=ListNode(item)
            while count!=pos-1:
                count+=1
                a=a.next
            b=a.next
            i.next=b
            a.next=i

    def search(self,item):
        a=self.__head
        while a!=None:
            if item==a.elem:
                return True
            a=a.next
        return False
   
    def remove(self,item):
        cur=self.__head
        pre=None
        while cur!=None:
            if cur.elem==item:
                if cur==self.__head: #判断是否为头节点
                    self.__head=cur.next
                else:
                    pre.next=cur.next
                break
            else:
                pre=cur
                cur=cur.next
    

class HashTable:
    def __init__(self,size=10) :
        self.size=size
        self.T=[SingleLinklist() for i in range(self.size)]

    def h(self,k):
        return k % self.size

    def insert(self,a):
        i=self.h(a)

        self.T[i].append(a)
    def travel(self):
        for i in range(self.size):
         
            ht.T[i].travel()
            print("\n")


ht=HashTable()

ht.insert(0)
ht.insert(1)
ht.insert(11)


ht.travel()



