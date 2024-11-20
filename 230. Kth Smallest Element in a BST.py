# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        out = self.inorder(root)
        return out[k-1]

    def inorder(self, root) -> List[int]:
        if not root:
            return []

        stack, out = [], []
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            
            root = stack.pop()
            out.append(root.val)
            root = root.right
        return out