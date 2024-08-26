class Queue:
    def __init__(self,max_size):
        self.queue = []
        self.max_size = max_size
    
    def enqueue(self,element):
        if self.is_full():
            print("Queue if FULL")
            return
        self.queue.append(element)
        print(f"Element {element} enqued")
    
    def dequeue(self):
        if self.is_empty():
            print("Queue is EMPTY")
            return None
        return self.queue.pop()
    
    def peek(self):
        if self.is_empty():
            print("Queue is EMPTY")
            return None
        return self.queue[0]
    
    def is_empty(self):
        return len(self.queue) == 0
    
    def is_full(self):
        return len(self.queue) == self.max_size
    
queue = Queue(5)
queue.enqueue(10)
queue.enqueue(20)
print("Front Element ",queue.peek())
print("Dequeued Element ",queue.dequeue())
print("Queue is Empty ",queue.is_empty())
print("Queue is Full ",queue.is_full())

            
            
