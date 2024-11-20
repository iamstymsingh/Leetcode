# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None

        if root.val == p.val:
            return p
        if root.val == q.val:
            return q

        search_left = self.lowestCommonAncestor(root.left, p, q)
        search_right = self.lowestCommonAncestor(root.right, p, q)

        if not search_left:
            return search_right
        elif not search_right:
            return search_left
        else:
            return root