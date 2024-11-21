# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return []

        paths = []
        self.getPaths(root, paths, "")
        return paths

    def getPaths(self, root: Optional[TreeNode], path: List[str], temp: str) -> None:
        if not root:
            return 

        temp += str(root.val)
        temp += "->"
        if not root.left and not root.right:
            temp = temp[:-2]
            path.append(temp)
            return

        self.getPaths(root.left, path, temp)
        self.getPaths(root.right, path, temp)
