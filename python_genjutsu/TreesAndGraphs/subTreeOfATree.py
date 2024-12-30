

# Given two binary trees root and subroot determine if subroot is a subtree 
# of root
# A subtree of a binary tree that consists of a node in the three and its descendants

# Identical tree check: To see if two trees are identical we can traverse
# both trees at the same time and compare at the same time

# subtree checl to check if tree1 is a subtree of tree2 we can traverse tree1 
# treate each node as root of a subtree, then use identical check to see if theyre
# the same

from typing import Optional, List

class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


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
