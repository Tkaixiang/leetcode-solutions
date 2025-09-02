# https://leetcode.com/problems/house-robber/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def __init__(self):
        self.memo = []

    def to_rob_or_not(self, nums: List[int], house_index):
        if house_index >= len(nums):
            return 0  # Out of range

        if self.memo[house_index] != -1:
            return self.memo[house_index]

        result = max(
            self.to_rob_or_not(nums, house_index + 2) + nums[house_index],
            self.to_rob_or_not(nums, house_index + 1),
        )
        # (2)       /\ Rob the current house and go to +2 house                     /\ Don't rob the current house and go to +1
        self.memo[house_index] = result
        return result

        # (3) The above is enough to work but, we get TIME LIMIT EXCEEDED GRRRR
        # We need, memoisation!
        # Example: [1,8,3,6,10,7,4]
        #               1
        #        ✅/       \❌
        #         3         8
        #      ✅/ \❌  ✅/ \❌
        #       10  6      6   3
        #        ✅/ \ ✅/ \
        # Left Branches -> We choose to rob that house ✅
        # Right Branches -> We choose to NOT rob that house ❌
        #
        # Notice: the pattern repeats? the same "Choose [1,6]" and choose[1,6]
        # BUT: How do we memoise this... path!!??
        # - We need not! Notice that for every to_rob_or_not(i),
        # - if we start at i, we can only pick THE ELEMENTS TO THE RIGHT
        # - so regardless of path taken, to_rob_or_not(i) is always the SAME VALUE

    def rob(self, nums: List[int]) -> int:
        # (Most Dynamic Programming problems use 2 states, or what does dp[i] mean?)
        # 1. Starting from the left-most house (n), we have 2 choices:
        # - Rob n, or don't rob n
        # - If we rob n, we have to go n+2 next
        # - If we don't rob n, we should go n+1 next
        # - So, dp[i] means, what is the max amount of money we can rob starting at house i
        # This relationship can be translated to the recursive function above (2)

        if len(nums) == 0:
            return 0

        self.memo = [-1] * len(nums)

        return self.to_rob_or_not(nums, 0)
