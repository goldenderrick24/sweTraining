from typing import Optional

# Definition for a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_tree(nodes, f):
    val = next(nodes)
    if val == "x":
        return None
    left = build_tree(nodes, f)
    right = build_tree(nodes, f)
    return TreeNode(f(val), left, right)

def format_tree(node):
    if node is None:
        yield "x"
        return
    yield str(node.val)
    yield from format_tree(node.left)
    yield from format_tree(node.right)

def find(tree, val):
    if tree is None:
        return False
    if tree.val == val:
        return True
    elif tree.val < val:
        return find(tree.right, val)
    else:
        return find(tree.left, val)

def insert(tree, val):
    if tree is None:
        return TreeNode(val)
    if tree.val < val:
        tree.right = insert(tree.right, val)
    elif tree.val > val:
        tree.left = insert(tree.left, val)
    return tree

def lca_on_bst(bst: TreeNode, p: int, q: int) -> int:
    if p < bst.val and q < bst.val:
        return lca_on_bst(bst.left, p, q)
    elif p > bst.val and q > bst.val:
        return lca_on_bst(bst.right, p, q)
    else:
        return bst.val

def lca(root: TreeNode, node1: TreeNode, node2: TreeNode) -> TreeNode:
    if not root:
        return None

    # case 2 in above figure
    if root in (node1, node2):
        return root

    left = lca(root.left, node1, node2)
    right = lca(root.right, node1, node2)

    # case 1
    if left and right:
        return root

    # at this point, left and right can't be both non-null since we checked above
    # case 4 and 5, report target node or LCA back to parent
    if left:
        return left
    if right:
        return right

    # case 3, not found return null
    return None
    
def serialize(root):
    res = []

    def dfs(root):
        if not root:
            res.append("x")
            return
        res.append(root.val)
        dfs(root.left)
        dfs(root.right)

    dfs(root)
    return " ".join(res)

def deserialize(s):
    def dfs(nodes):
        val = next(nodes)
        if val == "x":
            return None
        cur = TreeNode(int(val))
        cur.left = dfs(nodes)
        cur.right = dfs(nodes)
        return cur

    # create an iterator that returns a token each time we call `next`
    return dfs(iter(s.split()))

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # Helper function to validate BST using range constraints
        def validate(node: Optional[TreeNode], low: float, high: float) -> bool:
            if not node:  # Base case: empty tree or subtree is valid
                return True
            
            # Check if the current node's value violates the BST property
            if not (low < node.val < high):
                return False
            
            # Recursively validate the left and right subtrees
            return (validate(node.left, low, node.val) and
                    validate(node.right, node.val, high))
        
        # Start recursion from the root node with infinite bounds
        return validate(root, float('-inf'), float('inf'))
