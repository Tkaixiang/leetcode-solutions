# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# https://leetcode.com/problems/binary-tree-right-side-view/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def explore(self, level: int, node: TreeNode, results: List[int]):
        if not node:
            return None

        # 1. We will always travel RIGHT FIRST
        # So, right-most nodes will always get FIRST DIPS on the array entry of their level (index 0 == level 0)
        # If the array entry is already taken, it means a right-most node has been added, and we should ignore
        if len(results) <= level:
            # Right node hasn't taken this spot yet
            results.append(node.val)

        rightResult = self.explore(level + 1, node.right, results)
        leftResult = self.explore(level + 1, node.left, results)

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # At each level, we want to find the RIGHT MOST node
        results = []

        self.explore(0, root, results)
        return results
