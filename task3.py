class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def preorder_traversal(root):
    sum = 0
    if root:
        sum = sum + root.val
        print(root.val)
        preorder_traversal(root.left)
        preorder_traversal(root.right)
    return sum

# Створення дерева
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Прямий обхід:")
print(preorder_traversal(root))