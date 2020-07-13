class designStack_Min:
    def __init__(self):
        self.stack = []
        self.min_stack = []
        self.size = 0


    def push(self,x:int)->None:
        if not self.min_stack==0:
            self.min_stack.append(x)
        else:
            if x<=self.min_stack[-1]:
                self.min_stack.append(x)
        self.stack.append(x)
        self.size+=1

    def pop(self)->None:
        if (self.stack or self.min_stack) and (self.stack[-1]==self.min_stack[-1]):
            self.min_stack.pop()

        self.stack.pop()
        self.size-=1

    def getMin(self)->int:
        return self.min_stack[-1]

    def top(self)->int:
        return self.stack[-1]

def main():
    m= designStack_Min()
    m.push(5)
    m.push(10)
    print("min: ",m.getMin())
    print("top_element: ", m.top())
    print("stack_size: ", m.size)
    print("-------")
    m.push(-5)
    m.push(15)
    print("min: ",m.getMin())
    print("top_element: ", m.top())
    print("stack_size: ", m.size)

if __name__ == "__main__":
    main()

