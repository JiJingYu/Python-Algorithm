# 1086. Tree Traversals Again
# 20:59 pm

"""
Sample Input:

6
Push 1
Push 2
Push 3
Pop
Pop
Push 4
Pop
Pop
Push 5
Push 6
Pop
Pop

Sample Output:

3 4 2 6 5 1

"""

from collections import deque


class TreeNode():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


stack = []

N = int(input())
preorder = []
inorder = []
for i in range(2 * N):
    line = input().split()
    op = line[0]
    if op == "Push":
        val = int(line[1])
        stack.append(val)
        preorder.append(val)
    if op == "Pop":
        val = stack.pop()
        inorder.append(val)

def buildTree(preorder, inorder):
    # pre: VLR
    # inorder: LVR
    if inorder:
        v = TreeNode(preorder[0])
        v_ind = inorder.index(v.val)
        v.left = buildTree(preorder[1:v_ind+1], inorder[:v_ind])
        v.right = buildTree(preorder[v_ind+1:], inorder[v_ind+1:])
        return v
root = buildTree(preorder, inorder)

res = []

def dfs(root):
    if not root:
        return
    dfs(root.left)
    dfs(root.right)
    res.append(root.val)

dfs(root)
print(" ".join(map(str, res)))