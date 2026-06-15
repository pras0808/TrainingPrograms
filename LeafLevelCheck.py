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
        if values[i] != "N":
            curr.left = Node(int(values[i]))
            q.append(curr.left)
        i += 1
        if i < len(values) and values[i] != "N":
            curr.right = Node(int(values[i]))
            q.append(curr.right)
        i += 1
    return root

leaf_level = -1

def check(node, level):
    global leaf_level

    if not node:
        return True
    if not node.left and not node.right:
        if leaf_level == -1:
            leaf_level = level
        return level == leaf_level

    return check(node.left, level + 1) and check(node.right, level + 1)

values = input("Enter tree nodes level-wise (use N for null): ").split()
root = build_tree(values)
print(1 if check(root, 0) else 0)
