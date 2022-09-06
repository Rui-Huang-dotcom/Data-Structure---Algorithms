class ListNode:
    def __init__(self,elem) :
        self.elem=elem
        self.next=None
        self.pre=None

class DoubleLinklist:
    def __init__(self,node=None) :
        self.head=node

    def is_empty(self):
        return self.head==None

    def travel(self):
        a=self.head
        while a != None:
            print(a.elem,end=" ")
            a=a.next                   
        print("\n")
    def length(self):
        count=0
        a=self.head
        while a!=None:
            count+=1
            a=a.next
        return count
    
    def search(self,item):
        a=self.head
        while a!=None:
            if item==a.elem:
                return True
            a=a.next
        return False
    
    def add(self,item):
        node=ListNode(item)
        if self.is_empty():
            self.head=node
        else:
            node.next=self.head
            
            self.head=node
            self.head.pre=node

    def append(self,item):
        node=ListNode(item)
        if self.is_empty():
            self.head=node
        else:
            cur=self.head
            while cur.next!=None:
                cur=cur.next
            cur.next=node
            node.pre=cur

    def insert(self,pos,item):
        if pos<=0:
            self.add(item)
        elif pos>(self.length()-1):
            self.append(item)
        else:
            count=0
            a=self.head
            i=ListNode(item)
            while count!=pos-1:
                count+=1
                a=a.next
            
            i.next=a.next
            a.next.prev=i
            a.next=i

    def remove(self,item): 
        cur=self.head
        pre=None
        while cur!=None:
            if cur.elem==item:
                if cur==self.head: #判断是否为头节点

                    self.head=cur.next
                    cur.next.pre=None
                elif cur.next==None:
                    pre.next=None

                else:
                    pre.next=cur.next
                    cur.next.pre=pre
                break
            else:
                
                pre=cur
                cur=cur.next



ll=DoubleLinklist()

ll.append(2)
ll.add(9)
ll.insert(7,0)
# ll.remove(9)
ll.append(1)
ll.travel()
ll.remove(0)
# ll.append(2)
ll.travel()