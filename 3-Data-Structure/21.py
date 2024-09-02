class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        new_node = Node(data)
        if not self.root:
            self.root = new_node
            return

        queue = [self.root]
        while queue:
            node = queue.pop(0)

            if not node.left:
                node.left = new_node
                break
            else:
                queue.append(node.left)

            if not node.right:
                node.right = new_node
                break
            else:
                queue.append(node.right)
        print(f"Inserted {data} into the binary tree.")

    def search(self, key):
        if not self.root:
            return False

        queue = [self.root]
        while queue:
            node = queue.pop(0)
            if node.data == key:
                return True

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return False

    def delete(self, key):
        if not self.root:
            print("The tree is empty.")
            return

        key_node = None
        queue = [self.root]

        while queue:
            node = queue.pop(0)

            if node.data == key:
                key_node = node

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        if key_node:
            x = node.data
            self._delete_deepest(node)
            key_node.data = x
            print(f"Deleted {key} from the binary tree.")
        else:
            print(f"{key} not found in the binary tree.")

    def _delete_deepest(self, del_node):
        queue = [self.root]
        while queue:
            node = queue.pop(0)
            if node is del_node:
                node = None
                return
            if node.right:
                if node.right is del_node:
                    node.right = None
                    return
                else:
                    queue.append(node.right)

            if node.left:
                if node.left is del_node:
                    node.left = None
                    return
                else:
                    queue.append(node.left)

    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.data, end=" ")
            self.inorder(node.right)

    def preorder(self, node):
        if node:
            print(node.data, end=" ")
            self.preorder(node.left)
            self.preorder(node.right)

    def postorder(self, node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.data, end=" ")

    def level_order(self):
        if not self.root:
            print("The tree is empty.")
            return

        queue = [self.root]
        while queue:
            node = queue.pop(0)
            print(node.data, end=" ")

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

# Example usage
bt = BinaryTree()
bt.insert(1)
bt.insert(2)
bt.insert(3)
bt.insert(4)
bt.insert(5)
bt.insert(6)
bt.insert(7)

print("Inorder traversal: ", end="")
bt.inorder(bt.root)
print()

print("Preorder traversal: ", end="")
bt.preorder(bt.root)
print()

print("Postorder traversal: ", end="")
bt.postorder(bt.root)
print()

print("Level order traversal: ", end="")
bt.level_order()
print()

print("Searching for 5:", bt.search(5))
print("Searching for 8:", bt.search(8))

bt.delete(4)
print("Level order traversal after deletion: ", end="")
bt.level_order()
print()

