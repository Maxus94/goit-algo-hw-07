class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def preorder_traversal(root):
    sum = 0
    if root:
        sum = sum + root.val
        print("Значення =", root.val)
        sum = sum + preorder_traversal(root.left)
        sum = sum + preorder_traversal(root.right)
    return sum

# Створення дерева
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.right.right = Node(6)
root.right.left = Node(8)
root.right.right = Node(9)

print("Сума значень =", preorder_traversal(root))