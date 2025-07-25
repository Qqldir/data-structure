# 트리의 방문(traverse)-비재귀, 스택
class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def preorder_traversal(root):
    if not root:
        return
    stack = [root]

    while stack:
        node = stack.pop()
        print(node.data, end=' ')
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

# 예시 트리
#      A
#     / \
#    B   C
#   / \
#  D   E
tree = Node('A', Node('B', Node('D'), Node('E')), Node('C'))
preorder_traversal(tree)  # 출력: A B D E C