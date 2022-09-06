from collections import deque
class BiTreeNode:
    def __init__(self,data) :
        self.data=data
        self.l=None
        self.r=None
        self.p= None

class BST:
    def __init__(self,li=None) :
        self.root=None
        if li:
            for val in li:
                self.insert_no_rec(val)
    
    def insert(self,node,val):
        if not node:
            node=BiTreeNode(val)
        elif node.data<val:
            node.r=self.insert(node.r,val)
        else:
            node.l=self.insert(node.l,val)

    def insert_no_rec(self,val):
        p=self.root
        if not p:
            self.root=BiTreeNode(val)
            return 
        while True:
            if val>p.data:
                if p.r:
                    p=p.r
                else: 
                    p.r=BiTreeNode(val)
                    p.r.p=p
                    return
            elif val<p.data:
                if p.l:
                    p=p.l
                else:
                    p.l=BiTreeNode(val)
                    p.l.p=p
                    return
            else:
                return

    def search(self,val):
        p=self.root
        while p:
            if val>p.data:
                if p.r:
                    p=p.r
                else:
                    return False
            elif val<p.data:
                if p.l:
                    p=p.l
                else:
                    return False
            else:
                return p

    def remove(self,val):
        x=self.search(val)
        if x.p.l==x:
            if not x.l and not x.r:
                x.p.l=None
            elif not x.l:
                x.p.l=x.r
                x.r.p=x.p
            elif not x.r:
                x.p.l=x.l
                x.l.p=x.p
            else:
                min=x.r
                while min.l:
                    min=min.l
                x.data=min.data
                if min.r:
                    x.r=min.r
                    min.r.p=x
                else:
                    x.r=None


        if x.p.r==x:
            if not x.l and not x.r: #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                x.p.r=None
            elif not x.l:
                x.p.r=x.r
                x.r.p=x.p
            elif not x.r:
                x.p.r=x.l
                x.l.p=x.p
            else:
                min=x.r
                while min.l:
                    min=min.l
                x.data=min.data
                if min.r:
                    x.r=min.r
                    min.r.p=x
                else:
                    x.r=None



    def a(self,x):
        if x:
            print(x.data,end=' ')
            self.a(x.l)
            self.a(x.r)
    
    def b(self,x):
        if x:
            self.b(x.l)
            print(x.data,end=' ')
            self.b(x.r)

    def c(self,x):
        if x:
            self.c(x.l)
            self.c(x.r)
            print(x.data,end=' ')
    def d(self,x):
        queue=deque()
        queue.append(x)
        while len(queue)>0:
            x=queue.popleft()
            print(x.data,end=' ')
            if x.l:
                queue.append(x.l)
            if x.r:
                queue.append(x.r)
tree=BST([4,6,7,9,2,1,3,5,8])    
tree.remove(6)
tree.a(tree.root)
print("\n")
tree.b(tree.root)
print("\n")
tree.c(tree.root)
print("\n")
tree.d(tree.root)


