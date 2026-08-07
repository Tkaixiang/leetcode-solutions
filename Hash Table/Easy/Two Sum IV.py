# https://leetcode.com/problems/two-sum-iv-input-is-a-bst/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverseTree(self, node, k, hash_table):
        if not node:
            return False
        
        if k - node.val in hash_table:
            return True

        hash_table[node.val] = 1
        return self.traverseTree(node.left, k, hash_table) or self.traverseTree(node.right,  k, hash_table)


    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        hash_table = {}
        # Similiar to twoSum (1)
        # 1. Traverse BST
        # 2. Record node values
        # 3. Find a matching recorded node == remainder of sum needed
        return self.traverseTree(root, k, hash_table)

