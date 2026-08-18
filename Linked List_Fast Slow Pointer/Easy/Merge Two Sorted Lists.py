# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        # 0. Edge Cases
        if list1 is None:
            return list2
        if list2 is None:
            return list1

        # 1. Start with initial node
        new_head = None
        probe1 = list1
        probe2 = list2
        if list1.val < list2.val:
            new_head = list1
            # First node of list1 used, move to next
            probe1 = probe1.next
        else:
            new_head = list2
            probe2 = probe2.next
            
        probe_head = new_head

        # 2. Merge
        while (probe1 is not None and probe2 is not None):
            if probe1.val < probe2.val:
                # Insert probe1 node first
                probe_head.next = probe1
                probe1 = probe1.next
            else:
                probe_head.next = probe2
                probe2 = probe2.next
            
            print("Current probe_head", probe_head.val)
            probe_head = probe_head.next
        
        # 3. Merge leftovers (only 1 of these loops will run)
        while (probe1 is not None):
            probe_head.next = probe1
            probe1 = probe1.next
            probe_head = probe_head.next
        while (probe2 is not None):
            probe_head.next = probe2
            probe2 = probe2.next
            probe_head = probe_head.next
        
        return new_head
                
