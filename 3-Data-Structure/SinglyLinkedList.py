class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        print(f'Inserted {data} at the beginning')
        
    def insert_at_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node= self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
        print(f'Inserted {data} at the end')
        
    def delete_node(self,key):
        temp = self.head
        if temp is not None:
            if temp.data == key:
                self.head = temp.next
                temp = None
                print(f'Deleted {key} from the linked List')
        prev = None
        while temp is not None:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next
        if temp == None:
            print(f'{key} not found in the linked list')
            return
        prev.next = temp.next
        temp = None
        print(f'Deleted {key}')
    
    def search(self,key):
        current = self.head
        while current:
            if current.data == key:
                return current
            current = current.next
        return None
    
    def traverse(self):
        current = self.head
        while current:
            print(current.data,end=" -> ")
            current = current.next
        print("NONE")
        
        
Ll = LinkedList()
Ll.insert_at_beginning(10)    
Ll.insert_at_end(30)    
Ll.insert_at_end(40)    
Ll.traverse()
Ll.delete_node(10)
Ll.traverse()    
result = Ll.search(30)
if result:
    print(f'Elements {result.data} found')
else:
    print(f'Element not found') 
            

     
