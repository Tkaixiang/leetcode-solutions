# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/description/?envType=study-plan-v2&envId=top-interview-150
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:        
        current_node = head
        prev_safe_node = None
        safe_head = None
        while current_node:
            # 1. Iterate through Linked List

            # 2. For each node, iterate next links until we get a diff number
            probe = current_node
            probe = probe.next
            is_duplicate = False
            while probe:
                if (probe.val != current_node.val): # 3. Keep going next until we see a different number
                    break
                is_duplicate = True
                probe = probe.next
            # "probe" is now the next DIFFERENT number

            # ==== Trial and error design ====
            # Quite a few edge cases here:
            # 1. safe_head -> When the head itself is a duplicate and we start at a later node
            # 2. prev_safe_node -> 
            # - Replacement doesnt work here since:
            # - If the ending node is a chain of duplicates, we have nothing to replace
            # - Use a method of pointing the prev_safe_node to the next safe_node (or "none")
            if (is_duplicate):
                if (prev_safe_node):
                    prev_safe_node.next = probe
                current_node = probe
            else:
                prev_safe_node = current_node
                if not safe_head:
                    safe_head = current_node
                current_node = current_node.next
                
        

        return safe_head

                