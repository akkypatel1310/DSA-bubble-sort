class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
        
class DoubleLinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_beginning(self,data):
        new_node = Node(data)
        new_node.next = self.head
        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node
        print(f'inserted {data} at beginning')
        
    def insert_at_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
        new_node.prev = last_node
        print(f'inserted {data} at the end')
        
    def delete_node(self,key):
        current = self.head
        if current is not None and current.data == key:
            self.head = current.next
            if self.head:
                self.head.prev = None
            current = None
            print(f'deleted {key} from the linked list')
            return
        while current is not None:
            if current.data == key:
                break
            current = current.next
        if current is None:
            print(f'{key} not found in the linked list')
            return
        if current.prev is not None:
            current.prev.next = current.next
        current = None
        print(f'deleted {key} from the linked list')
        
    def search(self,key):
        current = self.head
        while current is not None:
            if current.data == key:
                return current
            current = current.next
        return None
    
    def traverse_forward(self):
        current = self.head
        while current:
            print(current.data,end=" -> ")
            current = current.next
        print("None")
    
    def traverse_backward(self):
        current = self.head
        if not current:
            return
        while current.next:
            current = current.next
        while current:
            print(current.data,end=" -> ")
            current = current.prev
        print("NONE")
        
dll = DoubleLinkedList()
dll.insert_at_beginning(10)
dll.insert_at_end(20)
dll.insert_at_end(30)
dll.traverse_forward()
dll.traverse_backward()
dll.delete_node(20)
dll.traverse_forward()
result = dll.search(30)
if result:
    print(f'Element {result.data} found in linked list')
else:
    print("Not Found")
