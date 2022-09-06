class Node:
    def __init__(self,name,type='dir') :
        self.name=name
        self.type=type
        self.children = []
        self.parent=None

    def __repr__(self) -> str:
        return self.name

class FileSystemTree:
    def __init__(self):
        self.root=Node("/")
        self.now=self.root

    def mkdir(self,name):
        if name[-1]!="/":
            name+="/"
        node=Node(name)
        self.now.children.append(node)
        node.parent=self.now

tree=FileSystemTree()
tree.mkdir("var")
print(tree.root.name)
