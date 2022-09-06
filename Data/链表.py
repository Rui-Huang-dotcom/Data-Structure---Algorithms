class Node:
    def __init__(self,item) :
        self.item=item
        self.next=None

a=Node(1)
b=Node(2)
a.next=b

def create_linklist(li):
    head=Node(li[0])
    for i in li[1:]:
        node=Node(i)
        node.next=head
        head=node
    return head


def create_linklist_tail(li):
    head=Node(li[0])
    tail=head
    for i in li[1:]:
        node=Node(i)
        tail.next=node
        tail=node
    return head


def print_linklist(lk):
    while lk:
        print(lk.item,end=',')
        lk=lk.next
# lk=create_linklist_tail([1,2,3,6,8])
# print(lk.item)
# print_linklist(lk)

