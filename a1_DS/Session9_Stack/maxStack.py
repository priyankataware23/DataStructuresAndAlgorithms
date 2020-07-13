class maxStack:
    def __init__(self)->None:
        self.stack=[]
        self.max_stack=[]
        self.size=0

    def push(self,x:int)->None:
        if not self.max_stack:
            self.max_stack.append(x)
        else:
            if self.max_stack[-1]<=x:
                self.max_stack.append(x)
        self.stack.append(x)
        self.size+=1

    def pop(self)->None:
        if (self.stack or self.max_stack) and self.max_stack[-1]==self.stack[-1]:
            self.max_stack.pop()
        else:
            self.stack.pop()
            self.size-=1

    def getMax(self)->int:
        return self.max_stack[-1]

    def top(self)->int:
        return self.stack[-1]

    def getSize(self)->int:
        return self.size

def main():
    m=maxStack()
    m.push(10)
    m.push(5)
    m.push(-1)
    m.push(0)
    print("max: ",m.getMax())
    print("top_element: ", m.top())
    print("stack_size: ", m.size)
    m.pop()
    print("-------")
    m.push(-5)
    m.push(15)
    print("max: ",m.getMax())
    print("top_element: ", m.top())
    print("stack_size: ", m.size)

if __name__=="__main__":
    main()
