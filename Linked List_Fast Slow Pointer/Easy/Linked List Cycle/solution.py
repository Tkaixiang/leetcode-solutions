# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# https://leetcode.com/problems/linked-list-cycle/
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        nextLink = head
        
        # =====Walker + Runner Solution=====
        # Walker steps by 1 link at a time
        # Runner steps by 2 links at a time
        # Runner and walker will meet at some point if there is a cycle
        
        walker = head
        runner = head
        # Needs to be runner.next to ensure runner.next.next doesn't error out
        # Only need to check runner as it is faster than walker always
        while (runner != None and runner.next != None):
            walker = walker.next
            runner = runner.next.next
            
            if (walker == runner):
                return True
        
        return False