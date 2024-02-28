# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left_depth = self.get_depth(root.left)
        right_depth = self.get_depth(root.right)
        if left_depth == right_depth:
            # If left subtree and right subtree have the same depth,
            # then the left subtree is a perfect binary tree.
            # So we can simply count the nodes in the left subtree,
            # add the root node and recurse on the right subtree.
            return (1 << left_depth) + self.countNodes(root.right)
        else:
            # If left subtree and right subtree have different depths,
            # then the right subtree is a perfect binary tree with one level less.
            # So we can simply count the nodes in the right subtree,
            # add the root node and recurse on the left subtree.
            return (1 << right_depth) + self.countNodes(root.left)
    
    def get_depth(self, node: TreeNode) -> int:
        depth = 0
        while node:
            depth += 1
            node = node.left
        return depth