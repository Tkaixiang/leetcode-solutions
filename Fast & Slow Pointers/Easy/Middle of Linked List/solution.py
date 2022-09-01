# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        walking = head
        running = head
        
        while (running != None and running.next != None):
            walking = walking.next
            running = running.next.next
            
            # =====Jumping Order=====
            # Walking: 1 (head),2,3
            # Running: 1 (head),3,5 (running.next == None)
            
            # Walking: 1,2,3,4
            # Running: 1,3,5,None (running == None)
        
        return walking