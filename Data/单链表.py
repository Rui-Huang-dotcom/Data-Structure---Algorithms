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
        while a != None:
            print(a.elem,end=", ")
            a=a.next                   
        print("\n")
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


ll=SingleLinklist()

ll.add(0)
ll.add(1)
ll.add(2)
ll.add(3)
ll.remove(0)
ll.travel()

