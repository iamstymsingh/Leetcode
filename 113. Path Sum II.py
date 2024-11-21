# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []

        paths = []
        self.getPaths(root, paths, [], targetSum)
        return paths

    def getPaths(self, root, paths, temp, targetSum) -> None:
        if not root:
            return 

        targetSum -= root.val
        temp.append(root.val)

        if targetSum == 0 and not root.left and not root.right:
            paths.append(temp[:])
            return

        self.getPaths(root.left, paths, temp[:], targetSum)
        self.getPaths(root.right, paths, temp[:], targetSum)