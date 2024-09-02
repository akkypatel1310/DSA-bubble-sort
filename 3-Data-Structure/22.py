class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
            print(f"Inserted {key} as root node.")
        else:
            self._insert(self.root, key)

    def _insert(self, node, key):
        if key < node.key:
            if node.left is None:
                node.left = Node(key)
                print(f"Inserted {key} to the left of {node.key}.")
            else:
                self._insert(node.left, key)
        else:
            if node.right is None:
                node.right = Node(key)
                print(f"Inserted {key} to the right of {node.key}.")
            else:
                self._insert(node.right, key)

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        if node is None:
            return False

        if key == node.key:
            return True
        elif key < node.key:
            return self._search(node.left, key)
        else:
            return self._search(node.right, key)

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        if node is None:
            return node

        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            # Node with only one child or no child
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            # Node with two children: Get the inorder successor
            temp = self._min_value_node(node.right)
            node.key = temp.key
            node.right = self._delete(node.right, temp.key)

        return node

    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.key, end=" ")
            self.inorder(node.right)

    def preorder(self, node):
        if node:
            print(node.key, end=" ")
            self.preorder(node.left)
            self.preorder(node.right)

    def postorder(self, node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.key, end=" ")

    def level_order(self):
        if not self.root:
            print("Empty tree")
            return

        queue = [self.root]
        while queue:
            node = queue.pop(0)
            print(node.key, end=" ")

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

# Example usage
bst = BinarySearchTree()
bst.insert(50)
bst.insert(30)
bst.insert(70)
bst.insert(20)
bst.insert(40)
bst.insert(60)
bst.insert(80)

print("Inorder traversal: ", end="")
bst.inorder(bst.root)
print()

print("Preorder traversal: ", end="")
bst.preorder(bst.root)
print()

print("Postorder traversal: ", end="")
bst.postorder(bst.root)
print()

print("Level order traversal: ", end="")
bst.level_order()
print()

print("Searching for 40:", bst.search(40))
print("Searching for 25:", bst.search(25))

bst.delete(20)
print("Inorder traversal after deletion of 20: ", end="")
bst.inorder(bst.root)
print()

bst.delete(30)
print("Inorder traversal after deletion of 30: ", end="")
bst.inorder(bst.root)
print()

bst.delete(50)
print("Inorder traversal after deletion of 50: ", end="")
bst.inorder(bst.root)
print()
