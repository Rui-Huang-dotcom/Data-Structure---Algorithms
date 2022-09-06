from mimetypes import init
from collections import deque

class BiTreeNode:
    def __init__(self,data) :
        self.data=data
        self.l=None
        self.r=None

a=BiTreeNode("A")
b=BiTreeNode("B")
c=BiTreeNode("C")
d=BiTreeNode("D")
e=BiTreeNode("E")
f=BiTreeNode("F")
g=BiTreeNode("G")

e.l=a
e.r=g
a.r=c
c.l=b
c.r=d
g.r=f

def a(x):
    if x:
        print(x.data,end=' ')
        a(x.l)
        a(x.r)
   
def b(x):
    if x:
        b(x.l)
        print(x.data,end=' ')
        b(x.r)

def c(x):
    if x:
        c(x.l)
        c(x.r)
        print(x.data,end=' ')
# a(e)
# print("\n")
# b(e)


def d(x):
    queue=deque()
    queue.append(x)
    while len(queue)>0:
        x=queue.popleft()
        print(x.data,end=' ')
        if x.l:
            queue.append(x.l)
        if x.r:
            queue.append(x.r)

d(e)