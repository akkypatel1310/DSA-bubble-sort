class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None
        
    def insert_at_beginning(self,data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
        
        else:
            last_node = self.head
            while last_node.next != self.head:
                last_node = last_node.next
            new_node.next = self.head
            last_node.next = new_node
            self.head = new_node
        print(f'inserterd {data} at the beginning')
        
    def insert_at_end(self,data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
        else:
            last_node = self.head
            while last_node.next != self.head:
                last_node = last_node.next
            last_node.next = new_node
            new_node.next = self.head
        print(f'inserted {data} at the end')
    
    def delete_node(self,key):
        if not self.head:
            print('The list is empty')
            return
        current = self.head
        prev = None
        
        if current.data == key:
            if current.next == self.head:
                self.head = None
                print(f'Deleted {key} from the linked list')
                return
            last_node = self.head
            while last_node.next != self.head:
                last_node = last_node.next
            self.head = current.next
            last_node.next = self.head
            print(f'Deleted {key} froom the linked list')
            return
        while current.next != self.head:
            prev = current
            current = current.next
            if current.data == key:
                prev.next = current.next
                print(f'Deleted {key} from the linked list')
                return
        print(f'{key} not found')
        
    def search(self,key):
        if not self.head:
            return None
        current = self.head
        while True:
            if current.data == key:
                return current
            current = current.next
            if current == self.head:
                break
        return None
    
    def traverse(self):
        if not self.head:
            print('The List Is Empty')
            return
        current = self.head
        while True:
            print(current.data, end="->")
            current = current.next
            if current == self.head:
                break
        print("head")
        
cll = CircularLinkedList()
cll.insert_at_beginning(10)
cll.insert_at_end(30)
cll.insert_at_end(40)
cll.traverse()
cll.delete_node(30)
cll.traverse()