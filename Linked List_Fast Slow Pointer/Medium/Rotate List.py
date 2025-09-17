# https://leetcode.com/problems/rotate-list/description/?envType=study-plan-v2&envId=top-interview-150
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:  # No rotation needed for length <= 1 LLs
            return head

        # 1. Find the length of the LL - we only need to rotate by the reminder of the length
        probe = head
        length = 1
        while probe.next:  # We stop at the last node
            length += 1
            probe = probe.next

        # 2. Create a tail to the last node
        tail = probe
        actual_rotations_required = k % length
        if actual_rotations_required == 0:
            return head

        # 3. We only need to the LENGTH - actual_rotations_required portion of the LL to the front
        probe = head
        for x in range(length - actual_rotations_required - 1):
            # Get to the node that is actual_rotations_required from the END of the LL
            probe = probe.next

        new_head = probe.next
        probe.next = None
        tail.next = head
        head = new_head

        return head
