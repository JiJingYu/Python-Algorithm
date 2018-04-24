# 20:26 to 20:46
from collections import deque


class TreeNode():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


N = int(input())
postorder = [int(x) for x in input().split()]
inorder = [int(x) for x in input().split()]


def foo(postorder, inorder):
    # postorder: LRV
    # inorder: LVR
    if inorder:
        v = TreeNode(postorder[-1])
        v_ind = inorder.index(v.val)
        v.left = foo(postorder[:v_ind], inorder[:v_ind])
        v.right = foo(postorder[v_ind: -1], inorder[v_ind+1:])
        return v


root = foo(postorder, inorder)

q = deque()
q.append(root)
res = []
while q:
    node = q.popleft()
    res.append(node.val)
    if node.left:
        q.append(node.left)
    if node.right:
        q.append(node.right)

print(" ".join(map(str, res)))

"""
7
2 3 1 5 7 6 4
1 2 3 4 5 6 7
"""
