# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        if not root:
            return []

        paths = []
        self.getPaths(root, paths, "")
        sum = 0
        for path in paths:
            sum += int(path, 2)
        return sum

    def getPaths(self, root: Optional[TreeNode], path: List[str], temp: str) -> None:
        if not root:
            return 

        temp += str(root.val)
        if not root.left and not root.right:
            path.append(temp)
            return

        self.getPaths(root.left, path, temp)
        self.getPaths(root.right, path, temp)

    