from typing import List

class Node:
    def __init__(self, val, children=None):
        if children is None:
            children = []
        self.val = val
        self.children = children

def ternary_tree_paths(root):
    def dfs(root, path, res):
        if all(c is None for c in root.children):
            res.append('->'.join(path) + '->' + str(root.val))
            return
        for child in root.children:
            if child is not None:
                # dfs(child, path + [str(root.val)], res)
                path.append(str(root.val))
                dfs(child, path, res)
                path.pop()
    res = []
    if root: dfs(root, [], res)
    return res

def ternary_tree_paths(root: Node) -> List[str]:
    # dfs helper function
    def dfs(root: Node, path: List[str], res: List[str]) -> None:
        # exit condition, reached leaf node, append paths to results
        if len(root.children) == 0:
            res.append("->".join(path) + "->" + str(root.val))
            return

        # dfs on each child
        for child in root.children:
            path.append(str(root.val))
            dfs(child, path, res)
            path.pop()

    res: List[str] = []
    dfs(root, [], res)
    return res

# this function builds a tree from input; you don't have to modify it
# learn more about how trees are encoded in https://algo.monster/problems/serializing_tree
def build_tree(nodes, f):
    val = next(nodes)
    num = int(next(nodes))
    children = [build_tree(nodes, f) for _ in range(num)]
    return Node(f(val), children)