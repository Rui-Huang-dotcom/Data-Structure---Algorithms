class Stack:
    def __init__(self) :
        self.stack=[]
    def push(self,element):
        self.stack.append(element)
    def pop(self):
        return self.stack.pop()
    def get_top(self):
        if len(self.stack) > 0:
            return self.stack[-1]
        else:
            return None
    def is_empty(self):
        return self.stack==[]
    def size(self):
        return len(self.stack)


x=list('(){')
print(x)
y=[]
z={'(':')','[':']','{':'}'}
for i in x:
    y.append(i)
    if len(y)>1:
        if y[-1]==z[y[-2]]:
            y.pop()
            y.pop()
if len(y)==0:
    print(True)
else:
    print(False) 







        
