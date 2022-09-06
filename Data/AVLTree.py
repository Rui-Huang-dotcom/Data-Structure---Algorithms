from mimetypes import init
from BST import BiTreeNode,BST

class AVLNode(BiTreeNode):
    def __init__(self, data):
        super().__init__(data)
        self.bf=0 #balanced factor

class AVLTree(BST):
    def __init__(self, li=None):
        super().__init__(li)

    def rotate_left(self,p,c):
        s2=c.l
        p.r=s2
        if s2:
            s2.p=p
        c.l=p
        p.p=c

        p.bf,c.pf=0,0
        return c

    def rotate_right(self,p,c):
        s2=c.r
        p.l=s2
        if s2:
            s2.p=p
        c.r=p
        p.p=c

        p.bf,c.pf=0,0
        return c

    def rotate_right_left(self,p,c):
        g=c.l
        
        s3=g.r
        c.l=s3
        if s3:
            s3.p=c
        g.r=c
        c.p=g

        s2=g.l
        p.r=s2
        if s2:
            s2.p=p
        g.l=p
        p,p=g

        if g.bf>0:
            c.bf,p.bf=0,-1
        elif g.bf<0:
            c.bf,p.bf=0,1
        else:
            p.bf,c.pf=0,0

        return g

    def rotate_left_right(self,p,c):
        g=c.r
        s2=g.l
        c.r=s2
        if s2:
            s2.p=c
        g.l=c
        c.p=g

        s3=g.r
        p.l=s3
        if s3:
            s3.p=p

        g.r=p
        p.p=g

        if g.bf>0:
            c.bf,p.bf=-1,0
        elif g.bf<0:
            c.bf,p.bf=1,0
        else:
            p.bf,c.pf=0,0

        return g

    def insert_no_rec(self,val):
        # 1.和BTS一样
        p=self.root
        if not p: #空树
            self.root=BiTreeNode(val)
            return 
        while True:
            if val>p.data:
                if p.r:
                    p=p.r
                else: 
                    p.r=BiTreeNode(val)
                    p.r.p=p
                    node=p.r
                    break
            elif val<p.data:
                if p.l:
                    p=p.l
                else:
                    p.l=BiTreeNode(val)
                    p.l.p=p
                    node=p.r
                    break
            else:
                return
        # 2.更新balance factor
        while node.p:
            if node.p.l==node:



