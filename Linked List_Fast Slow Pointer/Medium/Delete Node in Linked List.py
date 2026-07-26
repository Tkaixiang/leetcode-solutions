# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """

        # Since we can't modify the pointer of the prev node
        # We can instead take the next node and "delete" the next node (de-reference it)
        # Guaruntee: NOT the last node, so we can always take the next node
        node.val = node.next.val # Next node's value
        node.next = node.next.next # Next node's pointer, skip next node
        