from collections import deque

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def build_tree(values):
    if not values or values[0] == "N":
        return None
    root = Node(int(values[0]))
    q = deque([root])
    i = 1
    while q and i < len(values):
        curr = q.popleft()
        if i < len(values) and values[i] != "N":
            curr.left = Node(int(values[i]))
            q.append(curr.left)
        i += 1
        if i < len(values) and values[i] != "N":
            curr.right = Node(int(values[i]))
            q.append(curr.right)
        i += 1
    return root

def merge_trees(t1, t2):
    if not t1:
        return t2
    if not t2:
        return t1
    t1.data += t2.data
    t1.left = merge_trees(t1.left, t2.left)
    t1.right = merge_trees(t1.right, t2.right)
    return t1

def inorder(root):
    if not root:
        return
    inorder(root.left)
    print(root.data, end=" ")
    inorder(root.right)

print("Enter tree1:")
t1_vals = input().split()

print("Enter tree2:")
t2_vals = input().split()

t1 = build_tree(t1_vals)
t2 = build_tree(t2_vals)

merged = merge_trees(t1, t2)

print("Inorder of merged tree:")
inorder(merged)
