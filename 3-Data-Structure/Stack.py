class Stack:
    def __init__(self,max_size):
        self.stack = []
        self.max_size = max_size
    
    def push(self,element):
        if self.is_full():
            print("Stack is full")
            return
        self.stack.append(element)
        print(f'Element {element} pushed in stack')
    
    def pop(self):
        if self.is_empty():
            print('stack is empty')
            return None
        return self.stack.pop()
    
    def peek(self):
        if self.is_empty():
            print('Stack is empty')
            return None
        return self.stack[-1]
    
    def is_empty(self):
        return len(self.stack) == 0
    
    def is_full(self):
        return len(self.stack) == self.max_size
    
stack = Stack(5)
stack.push(10)
stack.push(20)
print("top element",stack.peek())
print("popped element",stack.pop())
print("stack is empty",stack.is_empty())    
