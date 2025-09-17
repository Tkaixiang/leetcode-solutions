# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/description/?envType=study-plan-v2&envId=top-interview-150
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(self, node, arr_nodes):
        if not node:
            return

        arr_nodes.append(node)
        self.traverse(node.left, arr_nodes)
        self.traverse(node.right, arr_nodes)

    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        arr_nodes = []
        self.traverse(root, arr_nodes)  # Get list of nodes in preorder traversal
        for x in range(0, len(arr_nodes) - 1, 1):
            node = arr_nodes[x]
            node.left = None
            node.right = arr_nodes[x + 1]
