from math import inf

class Node:
    def __init__(self, val, left=None,right=None):
        self.val = val
        self.right = right
        self.left = left

def max_tree_depth(root:Node) -> int:
    def dfs(root):
        if not root:
            return 0
        
        return max(dfs(root.left), dfs(root.right)) + 1
        # number of nodes in longest path of current subtree = max number of nodes of its two subtress + 1 current node
    return dfs(root) -1 if not root else 0

def build_tree(nodes, f):
    val = next(nodes)
    if val == "x":
        return None
    
    left = build_tree(nodes, f)
    right = build_tree(nodes, f)

    return Node(f(val), left,right)


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
        
        cur = Node(int(val))
        cur.left = dfs(nodes)
        cur.right = dfs(nodes)
        return cur
    
    return dfs(iter(s.split()))

def visibleTree(root:Node) -> int:
    def dfs(root, maxSofar):
        if not root:
            return 0
        
        total = 0

        if root.val >= maxSofar:
            total +=1

            total += dfs(root.left, max(maxSofar,root.val))
            total += dfs(root.right, max(maxSofar,root.val))
            
            return total
        
    return dfs(root, -inf)

def inOrderTraversal(root:Node) -> None:
    if root is None:
        inOrderTraversal(root.left)
        inOrderTraversal(root.right)

def dfs1(root, target):
    if root is None:
        return None
    
    if root.val == target:
        return root
    
    left = dfs1(root.left, target)

    if left is not None:
        return left
    
    return dfs1(root.right, target) or dfs1(root.left, target)

def tree_height(tree):
    if tree is None:
        return 0 
    lHeight = tree.height(tree.left)
    rHeight = tree.height(tree.right)

    if lHeight is -1 or rHeight is -1:
        return -1
    
    if abs(lHeight - rHeight) > 1:
        return -1
    
    return max(lHeight, rHeight) +1


def is_same(tree1, tree2):
    if tree1 is None and tree2 is None:
        return True
    if tree1 is None or tree2 is None:
        return False
    
    return (tree1.val == tree2.val and is_same(tree1.left, tree2.left)) and is_same(tree1.right, tree2.right) 

def subOfTree(root: Node, sub_root: Node) -> bool:
    if not root:
        return False
    
    return is_same(root, sub_root) or subOfTree(root.left,sub_root) or subOfTree(root.right, sub_root)



    