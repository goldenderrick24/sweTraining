
from typing import Optional, List

class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inOrderTraversal(self, root: Optional[Node]) -> List[int]:
    res = []
    stack = []
    cur = root

    while cur or stack:
        while cur:
            stack.append(cur)
            cur = cur.left
        
        cur = stack.pop()
        res.append(cur.val)
        cur = cur.right
    return res